
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from mongoCollection import student_data
from dbSecrets import db_cred

import streamlit as st
import pymongo

db_cred = st.secrets["mongoA"]["db_cred"]

uri = f"mongodb+srv://{db_cred}.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["student_database"]
collection = database["students"]

# # Insert the student document into the collection
# collection.insert_one(student_data)

# # Find a student by name
# result = collection.find_one({"name": "John Doe"})
# print(result)