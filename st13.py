# Caching - st.cache_data , st.cache_resource

import streamlit as st 
import numpy as np 
import pandas as pd 
import time
import torch
from full_model import Net

# cache resource
# @st.cache_resource
# def load_model(data):
#     st.write("load time", time.time())
#     model = Net()
#     checkpoints = torch.load()
#     model.load_state_dict(checkpoints["model_state"])
#     return model 

# model = load_model(15)



# @st.cache_data
# def inference(data):
#     st.write("inference time", time.time())
#     return model(torch.Tensor(data))

# model = load_model()
# inp = np.random.randn(1, 1, 28, 28)
# inp = np.zeros(1, 1, 28, 28)
# out = inference(inp)
# st.write(out)
