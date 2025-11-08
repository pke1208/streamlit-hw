import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Simple Data Visualizer")

# Input fields
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Name")
with col2:
    value = st.number_input("Value", min_value=0)

# Add button
if st.button("Add Data"):
    if 'data' not in st.session_state:
        st.session_state.data = []
    st.session_state.data.append({'Name': name, 'Value': value})

# Show chart
if 'data' in st.session_state and st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    fig = px.bar(df, x='Name', y='Value')
    st.plotly_chart(fig)
else:
    st.info("Add some data to see the chart")