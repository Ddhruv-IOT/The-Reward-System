# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 19:17:29 2023

@author: Asus
"""

import streamlit as st
from utils import md_runner, question_template

    
def page1():
    
    md_runner("<h3>So, Let's begin with Starter Challanges!</h3>")  
    x = question_template(st, "Enter GitHub Profile Link:", "A valid link", "5 marks:", "⚠️",  1)
    md_runner(x)
    x = question_template(st, "Enter GitHub Profile Link:", "A valid link", "5 0marks:", "⚠️",  2)
    md_runner(x)
    # x = question_template(st, "Enter LinkedIN Profile Link:", "A valid link", 2)
    # md_runner(x)
    # x = question_template(st, "Enter StackOverflow Profile Link:", "A valid link", 3)
    # md_runner(x)
    # x = question_template(st, "Enter your gmail ID:", "A valid link", 4)
    # md_runner(x)
    
    
    
    
    