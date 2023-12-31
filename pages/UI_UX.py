import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 
import sqlite3

load_dotenv(".streamlit/secrets.toml")
url=os.environ["AZURE_OPENAI_ENDPOINT_CHAT"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}

def insert_data_in_db(data):
    cxn = sqlite3.connect("UI_UX"+'.db')
    sql_createtable = """ CREATE TABLE IF NOT EXISTS UI_UX(
                                        name text NOT NULL
                                    );
                                      """
    
    c = cxn.cursor()
    c.execute(sql_createtable)
    #INSERT INTO artists (name) VALUES('Bud Powell');
    # c.execute("insert into contacts (name) values"), (data)")
    c.execute("insert into UI_UX(name) values(?)",(data,))
    cxn.commit()
    cxn.close() 


with st.form(key = 'userdata'):
    # st.write('data')
    prompt = st.text_area("Enter your input  :", key='prompt')
    # input_data = "Create summary in 300 words in very simple english language without any grammar mistake ,simple sentence ,active voice and use more we and you and keep usage of promoun for below conversation between Financial Advisor and Customer :\n\nConversation:"+prompt
    submit_form = st.form_submit_button(label="submit", help="Click to submit")
    if submit_form:
      data = {
                    "messages": [
                    {
                    "role": "system",
                    "content": "I am a UX writer who writes in a conversational tone while adopting a helpful and friendly persona in the UX copy I write. My organization sells insurance in Singapore, and we use British English in our copy. We want to create a positive user experience while avoiding the use of technical jargon without explaining or giving context to it. \n\nSuggest a header and body message. Keep the message clear, succinct and readable, with a maximum of 150 characters"
                    },
                    {
                    "role": "user",
                    "content": prompt
                    }
                             ],
	                "temperature": 0.7,
                    "top_p": 0.95,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "max_tokens": 250,
                    "stop": "None"
}
      response = requests.post(url, headers=headers, data=json.dumps(data))   
      if response.status_code == 200: 
            st.write("Success!!!!")   
                # st.write(response.json())
            st.write(response.json()["choices"][0]["message"]["content"])
            with open("history.txt", "a") as myfile:
            #  myfile.write(datetime.now())
             myfile.write(prompt)
             myfile.write("\n\n")
            #  myfile.write()
             insert_data_in_db(response.json()["choices"][0]["message"]["content"])
             myfile.write("\n\n\n\n\n")
      else:
        
            st.write("Failed to fetch data") 
            st.write("Status code:", response.status_code)
            st.write("Response:", response.choices)
with st.form(key = 'history'): 
     view_history = st.form_submit_button(label="view", help="Click to view")
     if view_history:
        cxn = sqlite3.connect("UI_UX"+'.db')
   
        c = cxn.cursor()
        c.execute("select * from UI_UX" ) 
        found_records = c.fetchall();
        for record in found_records:
            st.write(record)

        cxn.commit()
        cxn.close()



