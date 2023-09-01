# st.stop , st.form , st.set_page_config , st.echo , st.help

import streamlit as st 
import datetime

# Stop 
# email = st.text_input("Enter email")
# if not email:
#     st.warning("Enter your email please")
#     st.stop()
# st.success("Go ahead")


# Form 
# form = st.form("Basic form")
# name = form.text_input("Name")
# age = form.slider("Age", min_value=18, max_value=100, step=1)
# date = form.date_input("Birthday", value=datetime.date(2023, 9, 1))
# submmited = form.form_submit_button("Submit")
# if submmited:
#     st.write(name, age, date)


# Set Page Config 
# st.set_page_config(
#     page_title = "New app",
#     layout = "wide"
# )
# st.write("hi")


# Echo
# def summ(a, b):
#     return a+b
# with st.echo():
#     def mult(a, b):
#         return a*b 
#     a=10
#     b=20
#     su = summ(a, b)
#     mu = mult(a, b)
#     st.write(su, mu)
# st.write("This is outside")


# Help 
# st.help(datetime.time)