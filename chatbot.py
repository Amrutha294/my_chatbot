import streamlit as st
import google.generativeai as genai

# Load API Key from Streamlit Secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash-lastest")

# Create chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# App Title
st.title("Chatbot - Your AI Assistant")
st.write("Welcome to my Chatbot! How can I help you?")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Say something...")

if prompt:

    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Gemini response
        response = st.session_state.chat.send_message(prompt)

        reply = response.text

        # Store assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Error: {e}")
