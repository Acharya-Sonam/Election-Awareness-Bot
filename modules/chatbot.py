import streamlit as st
from google import genai
from google.genai import types
import os
from utils.helpers import load_json

def get_local_response(prompt, faq_data):
    """Fallback logic to get response from local FAQ data"""
    prompt_lower = prompt.lower()
    for key, answer in faq_data.items():
        if key in prompt_lower:
            return answer
    return "That's a great question! However, I couldn't find a specific answer in my local database and the AI service is currently unavailable. Please check your local election authority's official website."

def render_chatbot():
    st.header("💬 AI Assistant powered by Google Gemini")
    
    faq_data = load_json('data/faq.json')
    
    # Securely load API key
    api_key = None
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        pass
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your Election AI Assistant. How can I help you today?"}
        ]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask me about voting, ID requirements, registration, etc."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        bot_reply = ""
        
        if api_key:
            with st.spinner("AI is thinking..."):
                # Try multiple model names for maximum compatibility
                models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-flash-latest"]
                success = False
                
                for model_name in models_to_try:
                    try:
                        client = genai.Client(api_key=api_key)
                        
                        history = []
                        for msg in st.session_state.messages[:-1]:
                            role = "user" if msg["role"] == "user" else "model"
                            history.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))
                        
                        config = types.GenerateContentConfig(
                            system_instruction="You are an expert, helpful, and non-partisan Election AI Assistant. Answer questions about voting, registration, ID requirements, and the election process clearly and concisely.",
                            temperature=0.7
                        )
                        
                        chat = client.chats.create(model=model_name, config=config, history=history)
                        response = chat.send_message(prompt)
                        bot_reply = response.text
                        success = True
                        break
                    except Exception as e:
                        # Continue to next model if 404
                        if "404" in str(e) or "not found" in str(e).lower():
                            continue
                        else:
                            bot_reply = f"AI Service Error: {e}"
                            break
                
                if not success and not bot_reply:
                    st.info("Falling back to local knowledge base...")
                    bot_reply = get_local_response(prompt, faq_data)
                elif not success:
                    st.info("Falling back to local knowledge base...")
                    bot_reply = f"{bot_reply}\n\n{get_local_response(prompt, faq_data)}"
        else:
            st.info("Using local knowledge base (Gemini API key not found)...")
            bot_reply = get_local_response(prompt, faq_data)

        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
