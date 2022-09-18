import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to the Dashboard! 👋")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
"""
)

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

size = 100 if genre == 'Comedy' else 10


chart_data = pd.DataFrame(
    np.random.randn(size, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)