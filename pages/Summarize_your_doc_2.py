from dotenv import load_dotenv
import requests
from PyPDF2 import PdfReader
import json
import streamlit as st

from dotenv import load_dotenv
import os

load_dotenv(".streamlit/secrets.toml")

url=os.environ["AZURE_OPENAI_ENDPOINT_SUMMARY"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]

headers = {

    "api-key": api_key,

    "Content-Type": "application/json"

}
 
def main():
    load_dotenv(".streamlit/secrets.toml")
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
       
                 
if __name__ == '__main__':
    main()