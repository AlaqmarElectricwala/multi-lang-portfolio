from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

llm = GoogleGenerativeAI(model="gemini-2.5-flash-lite")

st.title("AI Q&A Bot")
st.markdown("My Q&A bot with langchain and Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask me anything!")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res)
    st.session_state.messages.append({"role": "ai", "content": res})