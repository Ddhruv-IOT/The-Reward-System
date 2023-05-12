# # -*- coding: utf-8 -*-
# """
# Created on Mon Jul 10 23:28:55 2023

# @author: Asus
# """

# with open("./simple_questions.txt", encoding="utf8" ) as questions:
#     a1 = questions.read().split("\n\n\n")
#     for t in a1:
#         print(t.split("\n"))

# x = [1, '2', 3]
# z = x.pop(2)
# print(z)


# x = "abc hi kw: abc"
# if "kw:" in x:
#     print("yes")

import streamlit as st
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

st.write(st.session_state['key'])