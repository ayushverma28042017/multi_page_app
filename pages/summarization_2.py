
import requests
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import json
import streamlit as st
import openai as openapi
import pandas as pd
 
url = "https://azureopenaistudio-dyi2023uc1.openai.azure.com/openai/deployments/DYIPOC/completions?api-version=2023-09-15-preview"

api_key = "ca48cf88888441899bfd469aed24ec5c" 
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"

}
 
data = {

    "prompt": "# Write a python function to reverse a string. The function should be an optimal solution in terms of time and space complexity.\n# Example input to the function: abcd123\n# Example output to the function: 321dcba",

    "max_tokens": 150,

    "temperature": 0.2,

    "frequency_penalty": 0,

    "presence_penalty": 0,

    "top_p": 1,

    "stop": ["#"]

}
 
def main():
    # load_dotenv()
    st.set_page_config(page_title="Summarize your PDF")
    st.header("Summarize your PDF 💬")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        data = {

            "prompt": text,

            "max_tokens": 150,

            "temperature": 0.2,

            "frequency_penalty": 0,

            "presence_penalty": 0,

            "top_p": 1,

            "stop": ["#"]

}
      response = requests.post(url, headers=headers, data=json.dumps(data))   
      if response.status_code == 200: 
        st.write("Success!!!!")   
        # st.write(response.json())
        st.write(response.json()["choices"][0]["text"])
      else:
        st.write("Failed to fetch data") 
        st.write("Status code:", response.status_code)
        st.write("Response:", response.choices)
                 
if __name__ == '__main__':
    main()