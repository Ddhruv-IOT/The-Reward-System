from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

db_object = []

def init_db():
    print("Connecting to MongoDB Atlas...")

    # Get the database credentials from Streamlit Secrets
    db_cred = st.secrets["mongoA"]["db_cred"]
    uri = f"mongodb+srv://{db_cred}.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the MongoDb Altas server
    client = MongoClient(uri, server_api=ServerApi("1"))
    
    # Access the database and collection
    database = client["student_database"]
    collection = database["students"]

    # retrun the collection object
    return collection


db_co = []

# Find a student by name


def read_student(collection):
    print("Reading a student from the database...")
    result = collection.find_one({"name": "John Doe"})
    print(result)


if __name__ == "__main__":
    collection = init_db()
    db_co.append(collection)
    print(collection)
    # read_student(db_co[0])
    # read_student(db_co[0])
    # read_student(db_co[0])
