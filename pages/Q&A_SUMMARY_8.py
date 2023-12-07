import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv(".streamlit/secrets.toml")

url=os.environ["AZURE_OPENAI_ENDPOINT_CHAT"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"

    }
 
with st.form(key = 'userdata'):
        st.write('data')
        prompt = st.text_input("Pass your Q&A :", key='prompt')
        st.text("Paste your Q&A here ")
        submit_form = st.form_submit_button(label="submit", help="Click to submit")
        if submit_form:
            data = {
  "messages": [
    {
      "role": "system",
      "content": "You are an AI assistant that helps people find information."
    },
    {
      "role": "user",
      "content": prompt
    }
  ],
 "max_tokens": 350,
  "temperature": 0.3,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "top_p": 1,
  "stop": ["Outcome "],
}
            response = requests.post(url, headers=headers, data=json.dumps(data))   
            if response.status_code == 200: 
                st.write("Success!!!!")   
                # st.write(response.json())
                st.write(response.json()["choices"][0]["message"]["content"])
            else:
                 st.write("Failed to fetch data") 
                 st.write("Status code:", response.status_code)
                #  st.write("Response:", response.choices)
                 
