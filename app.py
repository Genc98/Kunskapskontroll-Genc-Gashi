import streamlit as st
import pandas as pd

st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    return df

diagram_types = {"bar": st.bar_chart, "line": st.line_chart, "scatter": st.scatter_chart}

st.title("Diamond data analyzer")

file = st.file_uploader(label="Select a csv-file", accept_multiple_files=False, type="csv" )

if file:
    df = load_data(file)
    st.dataframe(df)
    x_data = st.selectbox(label="Select x", options=df.columns)
    y_data = st.selectbox(label="Select y", options=df.columns)
    diagram_type = st.radio(label="Select chart type", options=diagram_types.keys())
    if x_data and y_data and diagram_type:
        diagram_types[diagram_type](df, x=x_data, y=y_data, x_label=x_data.capitalize().replace("-", " "), y_label=y_data.capitalize().replace("-", " "))
    


    


