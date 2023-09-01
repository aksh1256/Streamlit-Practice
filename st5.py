# In streamlit input widget - multiselect, slider, select_slider, text_input, number_input

import streamlit as st 
from datetime import time

# Multiselect
# option = st.multiselect(
#     label = "Which places have you been?" ,
#     options = ("Sydney", "Tokyo", "New Delhi", "Hongkong", "Paris", "Thieland") ,
#     default = ("Sydney", "Paris")
# )
# st.write(option)


# Slider
# num = st.slider(
#     label = "Your age" ,
#     min_value = 18 ,
#     max_value = 100 ,
#     value = 20 ,
#     step = 1
# )
# st.write(num)


# Range
# num1 = st.slider(
#     label = "Your age" ,
#     min_value = 18 ,
#     max_value = 100 ,
#     value = (30, 60) ,
#     step = 1
# )
# st.write(num1)


# Time-Range Slider
# visit_timing = st.slider(
#     label = "Your appoinment" ,
#     value = (time(11, 30), time(12, 45))
# )
# st.write(visit_timing)


# Select-Slider
# option = st.select_slider(
#     label = "Select the best color",
#     options = ("Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red") ,
# )
# st.write(option)


# Select-Slider-Range 
# start_color , end_color = st.select_slider(
#     label = "Select color range" ,
#     options = ("Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red") ,
#     value = ("Blue", "Orange")
# )
# st.write("From", start_color, "to", end_color)


# Text-Input 
# txt = st.text_input(
#     label = "Enter your email here" ,
#     max_chars = 20 ,
#     placeholder = "Email here"
# )
# st.write(txt)


# Text-Input-Password
# passw = st.text_input(
#     label = "Enter your Password" ,
#     max_chars = 20 ,
#     placeholder = "Password here" ,
#     type = "password"
# )
# st.write(passw)


# Number-Input 
# num = st.number_input(
#     label = "Enter your weight" ,
#     min_value = 40 ,
#     max_value = 120 ,
#     value = 65 ,
#     step = 1
# )
# st.write(num)