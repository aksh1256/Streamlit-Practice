# Mutate charts, add_rows.

import streamlit as st 
import pandas as pd
import numpy as np
import random
import time

# Mutable Charts
df1 = pd.DataFrame(
    np.random.randn(10, 2),
    columns = ["col1", "col2"]
)
# my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(1, 2),
    columns = ["col1", "col2"]
)   

# my_table.add_rows(df2)

# my_chart = st.line_chart(df1)
# my_chart.add_rows(df2)

my_chart = st.line_chart(df1)
for i in range(5):
    time.sleep(1)
    df2 = pd.DataFrame(
        np.random.randn(1,2),
        columns=["col1", "col2"]
    )
    my_chart.add_rows(df2)

