import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LangChain Chatbot", page_icon=":robot_face:",layout="centered")

st.title("LangChain Chatbot")


#chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  


#llm instance
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro", 
    temperature=0.0,
)

#user input
user_input = st.chat_input("Ask a question :")

#chatbot response
if user_input:
    st.chat_message("user").markdown(user_input)    
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    response = llm.invoke(
        input=[
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.chat_history
        ]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
