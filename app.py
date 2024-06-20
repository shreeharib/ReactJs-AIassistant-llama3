from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Act as a very experienced professional react developer and answer the user queries and give the react js code accordingly. if the users questions is not relevant to the react js just tell them it is not relevant to react js and tell user to ask query related to reactjs. the code you give should be very simple and correct."),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('React JS AI Assistant')
st.header('[Provide your React JS code and get your doubts clarified here.]')
st.subheader("Powered with llama3",divider='rainbow')

input_text=st.text_input("Ask your questions here!")

# ollama LLAma2 LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))