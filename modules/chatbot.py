import streamlit as st
from utils.helpers import load_json

def render_chatbot():
    st.header("💬 Election Assistant Chat")
    
    faq_data = load_json('data/faq.json')
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your Election AI Assistant. How can I help you today?"}
        ]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask me about voting, ID requirements, registration, etc."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Simple keyword matching logic
        response = "That's a great question! However, I couldn't find a specific answer in my database. Please check your local election authority's official website for the most accurate information."
        prompt_lower = prompt.lower()
        
        for key, answer in faq_data.items():
            if key in prompt_lower:
                response = answer
                break

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
