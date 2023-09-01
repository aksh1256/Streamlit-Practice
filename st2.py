# Data Display Elements
# DataFrame, Table, Metric, Json


import streamlit as st 
import numpy as np
import pandas as pd
import json

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns = ["cols" + str(i) for i in range(20)])
# st.write(df)
# st.dataframe(df, width = 200, height = 100)
