import streamlit as st
import json
import os

def load_css():
    """Injects premium white custom CSS into the Streamlit app"""
    st.markdown("""
        <style>
        /* Premium White Aesthetic */
        .stApp {
            background-color: #f8fafc;
            color: #0f172a;
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Cards styling for containers */
        div[data-testid="stExpander"] {
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #3b82f6;
            color: white;
            border-radius: 8px;
            border: none;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #2563eb;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
            color: white;
            border: none;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #0f172a !important;
        }
        </style>
    """, unsafe_allow_html=True)

def load_json(filepath):
    """Utility to safely load json files"""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}
