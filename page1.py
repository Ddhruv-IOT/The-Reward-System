# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:17:29 2023

@author: Asus
"""

import streamlit as st
from utils import md_runner, question_template, is_valid_link

    
def page1():
    md_runner("<h3>So, Let's begin with Starter Challanges!</h3>")  
    i = 0
    with open("./simple_questions.txt", encoding="utf8" ) as questions:
        a1 = questions.read().split("\n\n\n")
        for t in a1:
            args = (t.split("\n"))
            callback = None
            if "is_valid_link" in args:
                callback_index = args.index("is_valid_link")
                callback = is_valid_link
                args.pop(callback_index)
            question_template(st, *args, callback=callback, key=i)
            i += 1
            
    
    
   # x = question_template(st, "Enter GitHub Profile Link:", "A valid link", "5 marks", "⚠️",  1, is_valid_link)
    # md_runner(x)
   # x = question_template(st, "Enter GitHub Profile Link:", "A valid link", "5 0marks:", "⚠️",  2)
   # md_runner(x)
    # x = question_template(st, "Enter LinkedIN Profile Link:", "A valid link", 2)
    # md_runner(x)
    # x = question_template(st, "Enter StackOverflow Profile Link:", "A valid link", 3)
    # md_runner(x)
    # x = question_template(st, "Enter your gmail ID:", "A valid link", 4)
    # md_runner(x)
    
    
    
    
    