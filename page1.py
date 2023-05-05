# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:17:29 2023

@author: Asus
"""

import streamlit as st
from utils import md_runner, question_template, is_valid_link, is_keyword_present

    
def page1():
    md_runner("<h3>So, Let's begin with Starter Challanges!</h3>")  
    question_template(st, "question", "question", "question", "⛔", callback=is_valid_link, callback2=is_keyword_present, keyword="git",key=0)
    with open("./simple_questions.txt", encoding="utf8" ) as questions:
        a1 = questions.read().split("\n\n\n")
        for ix, t in enumerate(a1):
            print(ix)
            args = (t.split("\n"))
            print(args)
            
            callback = None
            if "is_valid_link" in args:
                args.pop(args.index("is_valid_link"))
                callback = is_valid_link # the function name is passed as a callback
            
            keyword = None
            callback2 = None
            if "kw:" in args:
                print("yes")
                keyword = args.pop(args.index("kw:"))
                keyword = keyword.split(":")[1]
            
            print(args)
            

            question_template(st, *args, callback=callback, key=t)
            
            