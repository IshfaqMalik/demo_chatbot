#import streamlit 
import streamlit as st
import chatbot_backend as demo 

#Set ttitle using strealit https://docs.streamlit.io/develop/api-reference/text/st.title
st.title(" Hi, This is Chatbot Ishfaq's little assistant :sunglasses:")

#langchain memory to session cache : https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
if 'memory' not in st.session_state:
    st.session_state.memory= demo.demo_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history= []
#Rerender Chat history 
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message["text"])

#Enter the details for chatbot input box 

input_text = st.chat_input("Chat with my AI Assistant")

if input_text:

    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({"role":"user", "text":input_text})

    chat_response = demo.demo_conv(input_text = input_text, memory= st.session_state.memory)

    with st.chat_message("assistant"):
        st.markdown(chat_response)
