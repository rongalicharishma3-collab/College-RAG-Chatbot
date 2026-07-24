import streamlit as st
from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

st.title("Groq Test")

if st.button("Test"):

    try:

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY")
        )

        response = llm.invoke("Say Hello")

        st.success(response.content)

    except Exception as e:
        st.error(e)