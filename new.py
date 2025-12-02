import streamlit as st
from groq import Groq

client = Groq(api_key="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")

MODEL_NAME = "llama-3.1-8b-instant"  

st.title("⚡ Groq Chatbot with Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask anything...")

if user_input:
 
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": user_input}]
    )

    bot_reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.write(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
