import streamlit as st
import plotly.express as px
import pandas as pd


st.header("hello world!")

medals = "./data/Country_Medals.csv"

# ---------------------------
# TASK 0: load in data
@st.cache(persist = True)

def load_data(data):
    data = pd.read_csv(data)
    return data

data = load_data(medals)
# we need to cache the output of load_data if the input doesn't change
# so that the CPU cycle is not jammed every time you move the slider/ re-run app in any way
# essentially, we don't want to reload the data every time when we perform an interaction

# at this point, you are not going to see anything after you rerun the app
# because we haven't had any output yet

# let's try to show the data here
st.write(data)

