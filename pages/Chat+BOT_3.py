import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os as os


load_dotenv(".streamlit/secrets.toml")

url=os.environ.get("AZURE_OPENAI_ENDPOINT_CHAT")

# api_key = st.secrets["AZURE_OPENAI_API_KEY"]
api_key=os.environ.get("AZURE_OPENAI_ENDPOINT_CHAT")
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"

    }
 
data = {

    "messages": [{"role":"system","content":"which country is bigger Asia or Ameria."}],

   "max_tokens": 800,
  "temperature": 0.7,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "top_p": 0.95,
  "stop": ""

}
 

with st.form(key = 'userdata'):
        st.write('data')
        prompt = st.text_input("How can I help you :", key='prompt')
        st.text("### which country is bigger Asia or Ameria.")
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
  "temperature": 0.5,
  "top_p": 0.95,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 800,
  "stop": "None"
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
                 
