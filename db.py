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


# Test function for Read operation
# Find a student by name
@st.cache_data(ttl=600)
def read_student(_collection):
    print("Reading a student from the database...")
    result = _collection.find_one({"name": "John Doe"})
    return result


def adduser(_collection, name, email, password):
    print("Adding a student to the database...")
    
    if _collection.find_one({"email": email}):
        print("Email already exists.")
        return "Email already exists."
    
    result = _collection.insert_one(
        {"name": name, "email": email, "password": password}
    )
    return result


    print("User added successfully.")
if __name__ == "__main__":
    db_co = init_once_and_get_collection()
    # print(read_student(db_co))
