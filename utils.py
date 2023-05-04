# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:34:16 2023

@author: Asus
"""

import streamlit as st
import requests


def md_runner(data):
    st.markdown(data, unsafe_allow_html=True)


def is_valid_link(url):
    if not url:
        st.info("Can't be blank", icon="🛑")
        return False

    try:
        response = requests.head(url)
        if response.status_code != 200:
            st.info("Unreachable", icon="🛑")
            return False
    except requests.exceptions.RequestException:
        st.info("Wrong Link", icon="⛔")
        return False

    return True


def question_template(st, question, placeholder, info_text, icon, callback=None, key=0):

    text_input = st.text_input(
        question,
        placeholder=placeholder,
        key=key
    )

    if callback and not callback(text_input):
        return "Wrong Inputs"

    st.text(f"Your Input: {text_input}")
    st.info(info_text, icon=icon)
    return text_input
