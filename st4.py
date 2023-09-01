# Input widget streamlit button, download_button , checkbox , radio, selectbox
import streamlit as st 
import pandas as pd
import numpy as np
import time

# st.write(time.time())

# pr = st.button("Click Me")
# st.write(pr)

# pr = st.button("Click Me")
# if pr == True:
#     st.write(time.time())

# def fn():
#     st.write(time.time())
# st.button("Click me", on_click = fn)


# 1. Download csv file

# df = pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=["col1", "col2"]
# )
# data = df.to_csv().encode("utf-8")
# st.download_button(
#     label = "Download File",
#     data = data,
#     file_name = "new_file.csv",
#     mime = "text/csv"
# )

# 2. Download txt file 

# txt = "This is a sample text."
# st.download_button(
#     label = "Download file",
#     data = txt
# )

# Download Image

# file = open("AA.jpg", "rb")
# btn = st.download_button(
#     label = "Download image",
#     data = file, 
#     file_name = "akhil.jpg",
#     mime = "image/jpg"
# )


# Checkbox

# ck = st.checkbox("I agree")
# if ck == True:
#     st.write("Agreement done...!")

# With value parameter True or False shows checkbox are checked or not 
# ck = st.checkbox("I agree", value = False)
# if ck == True:
#     st.write("Agreement done...!")
# else:
#     st.write("Agreement not done...!")

# Radio Box

# option = st.radio(
#     label = "Order your food",
#     options = ("Pizza", "Burger", "Sandwitch", "Role", "Chips"),
#     index= 2
# )
# if option == "Pizza":
#     st.write("You ordered Pizza")
# elif option == "Burger":
#     st.write("You ordered Burger")
# elif option == "Sandwitch":
#     st.write("You ordered Sandwitch")
# elif option == "Role":
#     st.write("You ordered Role")
# else:
#     st.write("You ordered Chips")

# Select Box

# option = st.selectbox(
#     label = "Where do you live ?",
#     options = ("Mosco", "California", "Japan", "Austrelia")
# )
# if option == "Mosco":
#     st.write("You live in Mosco")
# elif option == "California":
#     st.write("You live in California")
# elif option == "Japan":
#     st.write("You live in Japan")
# else:
#     st.write("You live in Austrelia")