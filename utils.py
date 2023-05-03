# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:34:16 2023

@author: Asus
"""

import streamlit as st

def md_runner(data):
    st.markdown(data, unsafe_allow_html=True)


def question_template(st, question, placeholder, info_text, icon, key ):
    text_input = st.text_input(
        question,
        placeholder=placeholder,
        key=key
    )
    st.info(info_text, icon=icon)
    return text_input
