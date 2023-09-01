# Layout elements. st.sidebar, st.columns, st.tabs, st.expander, st.container

import streamlit as st 

# choice = st.sidebar.radio(
#     label = "Chose the option" ,
#     options = ("audio", "video") 
# )
# if choice == "audio":
#     st.audio("Sare_Jaha.mp3")
#     st.write("This is audio")
# elif choice == "video":
#     st.video("ontheway.mp4")
#     st.write("This is the video")


# Columns
# col1, col2 = st.columns([1, 3], gap="large")
# col1.audio("Sare_Jaha.mp3")
# col1.write("This is audio")
# col2.video("ontheway.mp4")
# col2.write("This is video")


# Tabs
# tab1, tab2 = st.tabs(["audio", "video"])
# tab1.audio("Sare_Jaha.mp3")
# tab1.write("This is audio")
# tab2.video("ontheway.mp4")
# tab2.write("This is video")


# Expander top-down information
# exp = st.expander("See the pic")
# exp.write("video and image")
# exp.image("AA.jpg", width=400)


# Container
# st.write("One")
# st.write("Two")
# st.write("Three")

# con = st.container()
# con.write("One")
# st.write("Two")
# con.write("Three")
# st.write("This is last")
# con.write("Last")