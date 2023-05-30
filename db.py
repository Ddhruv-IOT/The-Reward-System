from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

# Get the database credentials from Streamlit Secrets
db_cred = st.secrets["mongoA"]["db_cred"]
uri = f"mongodb+srv://{db_cred}.mongodb.net/?retryWrites=true&w=majority"


@st.cache_resource
def init_once_and_get_collection():
    print("Connecting to MongoDB Atlas...")

    # Create a new client and connect to the MongoDb Altas server
    client = MongoClient(uri, server_api=ServerApi("1"))

    # Access the database and collection
    database = client["student_database"]
    collection = database["students"]

    # retrun the collection object
    return collection


@st.cache_data(ttl=600)
def user_general_info(_collection):
    cursor = _collection.find({})

    # Lists to store user names, passwords, and emails
    user_names = []
    passwords = []
    emails = []

    # Iterate over the cursor and extract data
    for doc in cursor:
        user_names.append(doc["name"])
        passwords.append(doc["password"])
        emails.append(doc["email"])

    return user_names, emails, passwords


@st.cache_data(ttl=600)
def read_student_name(_collection):
    # Retrieve only the names of all students
    cursor = _collection.find({}, {"name": 1, "_id": 0})
    names = [doc["name"] for doc in cursor]
    return names


def adduser(_collection, name, email, password):
    if _collection.find_one({"email": email}):
        return "emailError"

    result = _collection.insert_one(
        {"name": name, "email": email, "password": password}
    )
    return result


if __name__ == "__main__":
    db_co = init_once_and_get_collection()
    # print(read_student(db_co))
