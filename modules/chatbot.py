import streamlit as st
import google.generativeai as genai
import os

def render_chatbot():
    st.header("💬 AI Assistant powered by Google Gemini")
    
    # Securely load API key from Streamlit secrets or environment
    api_key = None
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        pass
        
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        st.warning("⚠️ Google Gemini API Key is missing. Please set GEMINI_API_KEY in .env or .streamlit/secrets.toml.")
        return

    genai.configure(api_key=api_key)
    
    # Initialize the model
    # We use gemini-1.5-flash for fast, standard chat responses
    try:
        model = genai.GenerativeModel('gemini-1.5-flash',
                                      system_instruction="You are an expert, helpful, and non-partisan Election AI Assistant. Answer questions about voting, registration, ID requirements, and the election process clearly and concisely.")
    except Exception as e:
        st.error(f"Failed to initialize Gemini model: {e}")
        return
        
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your Election AI Assistant, powered by Google Gemini. How can I help you today?"}
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

        # Generate response using Google Gemini
        with st.spinner("Thinking..."):
            try:
                # Convert session state history to Gemini format
                history = []
                for msg in st.session_state.messages[:-1]: # exclude the current prompt we just appended
                    role = "user" if msg["role"] == "user" else "model"
                    history.append({"role": role, "parts": [msg["content"]]})
                
                chat = model.start_chat(history=history)
                response = chat.send_message(prompt)
                bot_reply = response.text
            except Exception as e:
                bot_reply = f"Sorry, I encountered an error while communicating with Google Gemini: {e}"

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
