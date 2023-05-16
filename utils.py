# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:34:16 2023

@author: Asus
"""

import streamlit as st
import requests
from db import init_once_and_get_collection

collection = init_once_and_get_collection()

def md_runner(data):
    st.markdown(data, unsafe_allow_html=True)

def is_keyword_present(text, keyword):
    if keyword not in text:
        st.info(f"Invalid input for this field as keyword @ {keyword} is not found", icon="🛑")
        return False
    return True


def is_valid_link(url):
    if not url:
        st.info("Can't be blank", icon="🛑")
        return False

    try:
        response = requests.head(url)
        # if response.status_code != 999:
        #     print(response.status_code)
        #     st.info("Unreachable", icon="🛑")
        #     return False
    except requests.exceptions.RequestException:
        st.info("Wrong Link", icon="⛔")
        return False

    return True


def question_template(st, question, placeholder, info_text, icon, callback=None, callback2=None, keyword= None, key=0):

    text_input = st.text_input(
        question,
        placeholder=placeholder,
        key=key
    )

    flag = True

    if callback and not callback(text_input):
        flag = False
        return "Wrong Inputs"
    
    if callback2 and not callback2(text_input, keyword):
        flag = False
        return "Wrong Data"    

    if flag:
        st.text(f"Your Input: {text_input}")
        st.info(info_text, icon=icon)

        query = {"name": "John Doe"}
        existing_document = collection.find_one(query)

        if existing_document:
            print(flag)
            # Update the document with a new field
            new_field = {"$set": {keyword: text_input}}
            collection.update_one(query, new_field)
            print("Document updated successfully.")
        else:
            print("Document not found.")

        # Print the updated document
        updated_document = collection.find_one(query)
        print("Updated Document:")
        print(updated_document)


        return text_input
