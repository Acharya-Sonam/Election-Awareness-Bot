import streamlit as st
from utils.helpers import load_json

def display_timeline():
    st.header("🗳️ Election Process Timeline")
    st.write("Click on each step below to learn more about the process.")
    
    data = load_json('data/election_info.json')
    if not data:
        st.error("Timeline data not found.")
        return
        
    for item in data:
        with st.expander(f"Step {item['step']}: {item['title']}"):
            st.write(item['description'])
