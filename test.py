# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:28:55 2023

@author: Asus
"""

with open("./simple_questions.txt", encoding="utf8" ) as questions:
    a1 = questions.read().split("\n\n\n")
    for t in a1:
        print(t.split("\n"))