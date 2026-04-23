import streamlit as st
import json
import os

def load_css():
    """Injects premium dark navy custom CSS into the Streamlit app"""
    st.markdown("""
        <style>
        /* Premium Dark Navy Aesthetic */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Cards styling for containers (Expanders, etc.) */
        div[data-testid="stExpander"] {
            background-color: rgba(30, 41, 59, 0.8);
            border-radius: 12px;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3), 0 4px 6px -2px rgba(0,0,0,0.15);
            border: 1px solid #334155;
            margin-bottom: 1rem;
        }
        
        /* Text inside expanders */
        div[data-testid="stExpander"] * {
            color: #f8fafc !important;
        }
        
        /* Chat messages */
        div[data-testid="stChatMessage"] {
            background-color: rgba(30, 41, 59, 0.6);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid #334155;
        }
        
        div[data-testid="stChatMessage"] * {
            color: #f8fafc !important;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #3b82f6;
            color: white !important;
            border-radius: 8px;
            border: none;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3);
            transition: all 0.3s ease;
            font-weight: 600;
        }
        .stButton > button:hover {
            background-color: #60a5fa;
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
            border: none;
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #ffffff !important;
        }
        
        /* Form text */
        label {
            color: #cbd5e1 !important;
        }
        </style>
    """, unsafe_allow_html=True)

def load_json(filepath):
    """Utility to safely load json files"""
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {}
