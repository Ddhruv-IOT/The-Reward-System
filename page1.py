# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:17:29 2023

@author: Asus
"""

import streamlit as st
from utils import md_runner, question_template, is_valid_link, is_keyword_present

    
def page1():
    st.write(st.session_state['key'])
    md_runner("<h3>So, Let's begin with Starter Challanges!</h3>") 

    # question_template(st, "question", "question", "question", "⛔", callback=is_valid_link, callback2=is_keyword_present, keyword="git",key=0)

    with open("./simple_questions.txt", encoding="utf8" ) as questions:
        a1 = questions.read().split("\n\n\n")
        for index, t in enumerate(a1):
            args = t.split("\n")
            
            callback = None
            if "is_valid_link" in args:
                args.pop(args.index("is_valid_link"))
                callback = is_valid_link # the function name is passed as a callback
            
            callback2 = None
            keyword = None
            if "keyword" in args:
                args.pop(args.index("keyword"))
                keyword = args.pop(-1)
                callback2 = is_keyword_present # the function name is passed as a callback
            
            question_template(st, *args, callback=callback, callback2=callback2, keyword=keyword, key=t)
            
            