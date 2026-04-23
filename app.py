import streamlit as st
from utils.helpers import load_css
from modules.process import display_timeline
from modules.eligibility import check_eligibility
from modules.chatbot import render_chatbot

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Democracy Guide | Election AI Assistant",
    page_icon="🗳️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def main():
    # Inject premium CSS
    load_css()
    
    # Title Section
    st.markdown("<h1 style='text-align: center;'>Democracy Guide</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.2rem; margin-bottom: 2rem;'>Your Interactive Election AI Assistant</p>", unsafe_allow_html=True)
    
    # Main Layout
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        # Left side: Timeline and Eligibility
        st.markdown("### Process & Requirements")
        display_timeline()
        st.markdown("---")
        check_eligibility()
        
    with col2:
        # Right side: Chatbot
        st.markdown("### Ask the AI")
        render_chatbot()

if __name__ == "__main__":
    main()
