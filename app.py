# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:56:01 2023

@author: Asus
"""

import streamlit as st
from streamlit_option_menu import option_menu
from db import init_once_and_get_collection
from page1 import page1
from utils import md_runner
from admin_page import adm_page

import pickle
from pathlib import Path
import streamlit_authenticator

names = ["Ddhruv", "Ankita"]
usernames = ["ddhruv", "ankita"]

# collection = st.session_state["db_coll"]
collection = init_once_and_get_collection()
cursor =collection.find({})

# Lists to store user names, passwords, and emails
user_names = []
passwords = []
emails = []

# Iterate over the cursor and extract data
for doc in cursor:
    user_names.append(doc["name"])
    passwords.append(doc["password"])
    emails.append(doc["email"])

# Print the lists
print("User Names:", user_names)
print("Passwords:", passwords)
print("Emails:", emails)

file_pth = Path(__file__).parent / "users.pkl"

with open(file_pth, "rb") as f:
    hashes = pickle.load(f)

auth = streamlit_authenticator.Authenticate(
    user_names, emails, passwords, "RAIoT Rewards", "App989"
)

name, authentication_status, username = auth.login("Login", "main")

if authentication_status == False:
    st.error("Authentication Failed")
if authentication_status == None:
    st.warning("Please enter your credentials")
if authentication_status == True:
    if name == "Ddhruv9":
        adm_page()

    else:
        with st.sidebar:
            choose = option_menu(
                "RAIoT Rewards",
                ["About", "Level1", "Level2", "Level3", "Coming Soon!"],
                icons=["house", "camera fill", "kanban", "book", "person lines fill"],
                menu_icon="app-indicator",
                default_index=0,
            )

        if choose == "About":
            st.write(f"Hi {name}")
            md_runner("<h4>Want be on Developer Spotlight ? </h2>")
            md_runner("<h4>Complete the Challanges and Earn points!</h2>")

        if choose == "Level1":
            page1()
