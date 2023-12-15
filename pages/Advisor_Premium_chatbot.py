import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 

load_dotenv(".streamlit/secrets.toml")
url=os.environ["api_base"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
azureSearchKey=os.environ["azureSearchKey"]
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}
with st.form(key = 'userdata'):
    # st.write('data')
    prompt = st.text_area("Enter Q&A  :", key='prompt')
    # input_data = "Create summary in 300 words in very simple english language without any grammar mistake ,simple sentence ,active voice and use more we and you and keep usage of promoun for below conversation between Financial Advisor and Customer :\n\nConversation:"+prompt
    submit_form = st.form_submit_button(label="submit", help="Click to submit")
    if submit_form:
      data = {"messages": [
    {
      "role": "system",
      "content": "you are a Financial advisor and you need to create a summary for the user for all the questions and answers given by the user You need to follow the below instructions: \nuse short sentences- \nActive voice\nuse more we and write in a positive\nAvoid hidden verbs by being more direct and to the point"
    },
    ,
    {
      "role": "user",
      "content": prompt
    
  ],
  "temperature": 0,
  "top_p": 1,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 800,
  "stop": "#",
  "azureSearchEndpoint": "https://cognitive-search-dyi.search.windows.net",
  "azureSearchKey": azureSearchKey,
  "azureSearchIndexName": "premium-index"
}
      response = requests.post(url, headers=headers, data=json.dumps(data))   
      if response.status_code == 200: 
            st.write("Success!!!!")   
            st.write(response.json())
            st.write(response.json()["choices"][0]["message"]["content"])
      else:
            st.write("Failed to fetch data") 
            st.write("Status code:", response.status_code)
            st.write("Response:", response.json())
