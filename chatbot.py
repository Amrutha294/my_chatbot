import streamlit as st
import google.generativeai as genai

API_KEY="AIzaSyC7bSTrapRouGwqE10DzVVs2ys4oyTgNn8"

genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')

if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])

st.title("Chatbot-Your AI Assistant")
st.write("Welcome to the my Chatbot! How Can i help you?")

if "message" not in st.session_state:
  st.session_state.message=[]

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)
