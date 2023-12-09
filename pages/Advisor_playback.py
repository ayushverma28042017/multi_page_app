import requests
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
 
with st.form(key = 'userdata'):
        st.write('data')
        prompt = st.text_area("Enter q&A  :", key='prompt')
       
        submit_form = st.form_submit_button(label="submit", help="Click to submit")
        if submit_form:
            data = {
 "prompt": "You are a Financial Advisor and you need to Generate a summary of the below conversation in the following format:\n\nThe summary should be less than 300 words, there should be no English and grammar errors in the summary.  and may use the below sentence to generate a summary.\n\nI will base my advice on the information that you give in this form about your investment goals, financial situation, and needs.\nYou may incur transaction costs without gaining any real benefit from the switch.\nWe are required to have a reasonable basis for any investment product recommendation we make to you\nThe regular investment amount is greater than or equal to your monthly surplus.\nI accept the product recommendation and agree to purchase the following plan. \n\n Conversation:"+prompt,
 "temperature": 0.35,
  "top_p": 0.95,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 300,
  "stop": "None"
}
            response = requests.post(url, headers=headers, data=json.dumps(data))   
            if response.status_code == 200: 
                 st.write("Success!!!!")   
                # st.write(response.json())
                 st.write(response.json()["choices"][0]["text"])
            else:
                 st.write("Failed to fetch data") 
                 st.write("Status code:", response.status_code)
                #  st.write("Response:", response.choices)





