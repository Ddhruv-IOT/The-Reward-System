import streamlit as st
import uuid
import streamlit_authenticator

from db import adduser, read_student_name
from emailer import connect_SMPT, send_email, stop_SMPT
from utils import md_runner

last_email = []
_collection = st.session_state["db_coll"]
s = connect_SMPT()
st.session_state["_s"] = s


def generate_user_password():
    # Generate a UUID4
    uuid_str = str(uuid.uuid4())
    # Remove hyphens from the UUID string
    uuid_str = uuid_str.replace("-", "@")
    # Extract a substring of desired length from the UUID string
    password = uuid_str[:7]

    return password


def add_user():
    read_student_name(_collection)

    with st.form("my_form"):
        md_runner("<h3> 🔌 Add a new user 👨‍💻👩‍💻</h3>")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Enter User name")
        with col2:
            email = st.text_input("Enter User email")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not name:
            st.error("Name cannot be empty", icon="⁉️")
            return
        elif not email:
            st.error("Email cannot be empty", icon="⁉️")
            return

        elif email in last_email:
            st.error("Current and Previous email cannot be same", icon="❌")
            return
        with st.spinner("Adding new user..."):
            random_password = generate_user_password()
            last_email.append(email)
            hashes = streamlit_authenticator.Hasher([random_password]).generate()
            status = adduser(_collection, name, email, hashes[0])

            if not status:
                st.warning("Failed to add new user. Try again.", icon="⚠️")
                return
            elif status == "emailError":
                st.error("Email already exists", icon="❌")
                return
            st.success(
                f"New user added successfully, user id: {status.inserted_id}", icon="✅"
            )

            with st.spinner("Sending email to user..."):
                op = send_email(s, email, random_password)
                st.success(op, icon="✅")
                # stop_SMPT(s)
                # st.write(name, email, random_password)
                st.balloons()
