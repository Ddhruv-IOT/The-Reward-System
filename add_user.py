import streamlit as st
import uuid


def generate_user_password():
    # Generate a UUID4
    uuid_str = str(uuid.uuid4())

    # Remove hyphens from the UUID string
    uuid_str = uuid_str.replace("-", "")

    # Extract a substring of desired length from the UUID string
    password = uuid_str[:10]  # Adjust the length as per your requirement

    return password


st.session_state["disable"] = False


def disable_form():
    st.session_state["disable"] = True


def enable_form():
    st.session_state["disable"] = False


def add_user():
    st.write("Add User here")

    with st.form("my_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Enter User name")
        with col2:
            email = st.text_input("Enter User email")
        submitted = st.form_submit_button(
            "Submit", on_click=disable_form, disabled=st.session_state["disable"]
        )

    if submitted and name and email:
        random_password = generate_user_password()
        st.write(name, email, random_password)
        # do something with the data
        enable_form()

    elif submitted and not name:
        st.error("Name cannot be empty")

    elif submitted and not email:
        st.error("Email cannot be empty")


# import pickle
# from pathlib import Path
# import streamlit_authenticator

# names = ["Ddhruv", "Ankita"]
# usernames = ["ddhruv", "ankita"]
# passwords = ["ddhruv09", "ankita12"]

# hashes = streamlit_authenticator.Hasher(passwords).generate()

# file_pth = Path(__file__).parent / "users.pkl"

# with open(file_pth, "wb") as f:
#     pickle.dump(hashes, f)
