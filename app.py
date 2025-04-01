from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

###<<< i have to take this files from .env>>>###
##os.environ["OPENAI_API_KEY"]="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"
##Langmith tracking
###os.environ["LANGCHAIN_TRACING_V2"]="true"
##os.environ["LANGCHAIN_API_KEY"]="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"


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
st.title('AI Chatbot')
input_text=st.text_input("Search the topic u want")

# openAI LLm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
