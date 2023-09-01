# Text_area, date_input, time_input, file_uploader, camera_input , color_pick

import streamlit as st 
import datetime
from PIL import Image
import numpy as np 
from io import StringIO

# Textarea
# txt = st.text_area(
#     label = "Write Something here..." ,
#     height = 200 ,
#     max_chars = 100 ,
#     placeholder = "Write here"
# )
# st.write(txt)


# Date Input
# dat = st.date_input("Enter Your Birthday",
#                     value = datetime.date(2002, 1, 5))
# st.write(dat)


# Time Input
# tim = st.time_input("Enter your meal time", value = datetime.time(14, 00))
# st.write(tim)


# Upload some file 
# fl = st.file_uploader(
#     label = "Upload here"
# )
# if fl:
#     st.write(fl.type)
#     if "image" in fl.type:
#         img = Image.open(fl)
#         st.write(np.array(img) .shape)
#     elif fl.type == "text/plain":
#         stringio = StringIO(fl.getvalue().decode("utf-8"))
#         string_data = stringio.read()
#         st.write(string_data)


# Take a Picture
# picture = st.camera_input("Take a pic")
# if picture:
#     img = Image.open(picture)
#     st.write(np.array(img).shape)


# Color Picker
# color = st.color_picker("Pick a color")
# if color:
#     st.write("You selected" , color)