import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv(".streamlit/secrets.toml")

url=os.environ["AZURE_OPENAI_ENDPOINT_NLP_TO_PYTHON"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
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
 

with st.form(key = 'userdata'):
        st.write('data')
        prompt = st.text_input("Enter your python function:", key='prompt')
        st.text("### EG :Write a python function to reverse a string. The function should be an optimal solution in terms of time and space complexity.\n# Example input to the function: abcd123\n# Example output to the function: 321dcba")
        submit_form = st.form_submit_button(label="submit", help="Click to submit")
        if submit_form:
            data = {

            "prompt": prompt,

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
                 
