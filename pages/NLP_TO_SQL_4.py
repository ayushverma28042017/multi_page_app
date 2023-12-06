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
 
with st.form(key = 'userdata'):
        st.write('data')
        prompt = st.text_input("Enter your NLP For SQL:", key='prompt')
        st.text("### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\n\nSELECT")
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
                 
