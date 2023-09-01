# Charts in Stremlit

import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(np.random.randn(10, 2) , columns = ["prices", "diff"])

# Line Chart 
# st.line_chart(df, y=["prices"])
# st.line_chart(df, y=["diff"])

# Area_Chart
# st.area_chart(df, y = ["prices"])

# Bar_Chart
# st.bar_chart(df, y=["prices"])
# st.bar_chart(df, y=["diff"])


# Matplotlib 

# Scatter_Plot
# fig , ax = plt.subplots()
# ax.scatter(np.arange(10) , np.arange(10) ** 2)
# st.pyplot(fig)


# Histo_Plot
# fig , ax = plt.subplots()
# ax.hist(np.random.randn(100), bins = 10)
# st.pyplot(fig)


# Map_Plot
# For Mumbai and New Delhi
# place1 = pd.DataFrame({
#         "lat" : [19.07 , 28.64],
#         "lon" : [72.87 , 77.21]
# })
# st.map(place1)

# For Kolkuta and Banglore
# place2 = pd.DataFrame({
#     "lat":[22.56 , 12.97],
#     "lon":[88.36 , 77.59]
# })
# st.map(place2)

# For Mumbai, New Delhi,Kolkuta and Banglore
# places = pd.DataFrame({
#     "lat" : [19.07 , 28.64 , 22.56 , 12.97],
#     "lon" : [72.87 , 77.21 , 88.36 , 77.59]
# })
# st.map(places)