import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from PIL import Image
st.title("What's Your Favorite Oreo?")
st.markdown("by **Meredith Wang**")

text = '<p style=" color:#7f4718; font-size: 50px;">by <b>Meredith Wang</b></p>'
st.markdown(text, unsafe_allow_html=True)