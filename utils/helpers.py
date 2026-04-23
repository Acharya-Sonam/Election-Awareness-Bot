import streamlit as st
import json
import os

def load_css():
    """Injects premium gradient custom CSS into the Streamlit app"""
    st.markdown("""
        <style>
        /* Premium Gradient Aesthetic */
        .stApp {
            background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
            color: #0f172a;
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Cards styling for containers */
        div[data-testid="stExpander"] {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
            border: 1px solid #cbd5e1;
            margin-bottom: 1rem;
        }
        
        /* Better contrast for expander text */
        div[data-testid="stExpander"] * {
            color: #0f172a !important;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #2563eb;
            color: white !important;
            border-radius: 8px;
            border: none;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.3);
            transition: all 0.3s ease;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #1d4ed8;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4);
            border: none;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #1e293b !important;
        }
        </style>
    """, unsafe_allow_html=True)

def load_json(filepath):
    """Utility to safely load json files"""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}
