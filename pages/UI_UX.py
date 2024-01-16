import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 
import streamlit as st
from streamlit_chat import message
import sqlite3


load_dotenv(".streamlit/secrets.toml")

url=os.environ["AZURE_OPENAI_ENDPOINT_CHAT"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]


st.image("Geine.jpg", width=100)
st.header("Let's UI/UX suggestion .... ")


headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}

def initdb():
       cxn = sqlite3.connect("UIUX"+'.db')
       sql_createtable = """ CREATE TABLE IF NOT EXISTS UIUX(
                                        name_id integer auto_increment primary key,
                                        timestamp DATE DEFAULT (datetime('now','localtime')),
                                        name text NOT NULL
                                    );
                                      """
       c = cxn.cursor()
       c.execute(sql_createtable)

def insert_data_in_db(data):
 
     cxn = sqlite3.connect("UIUX"+'.db')
     c = cxn.cursor()
     c.execute("insert into UIUX(name) values(?)",(data,))
     cxn.commit()
     cxn.close() 




def generate_response(prompt):
    data = {

    "model": "GPT-4",
     "temperature": 0.2,
     "max_tokens" :800,
     "frequency_penalty":0,
     "presence_penalty":0,
     "top_p":0.95,


    "messages": [
       {"role":"system","content":"""I am a UX writer who writes in a conversational tone while adopting a helpful and friendly persona in the UX copy I write.
         My organization sells insurance in Singapore, and we use British English in our copy. We want to create a positive user experience while avoiding the use of technical jargon without explaining or giving context to it. 
        kinldy write you suggestion in a header and body message format .
         Keep the message clear, succinct and readable, with a maximum of 150 characters """},
    {
            "role": "user",
            "content": prompt
        }
    ]

}
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = requests.post(url, headers=headers, data=json.dumps(data))
    # response = requests.post(url, headers=headers, data=json.dumps(data))   
    if completion.status_code == 200: 
            response = completion.json()["choices"][0]["message"]["content"]
            st.session_state['messages'].append({"role": "assistant", "content": response})
            # total_tokens = str(completion.json()["usage"]["total_tokens"])
            # prompt_tokens = str(completion.json()["usage"]["prompt_tokens"])
            # completion_tokens = str(completion.json()["usage"]["completion_tokens"])
       
            return str(response)
    else:
            st.write("Failed to fetch data") 
            st.write("Status code:", completion.status_code)
            st.write("Response:", completion.json())


# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
# st.sidebar.title("Sidebar")
# model_name = st.sidebar.radio("Choose a model:", ("Azure-Gen-AI(GPT3.5)", "Oracle-Gen-AI(Cohere)"))
# counter_placeholder = st.sidebar.empty()
# counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
# if model_name == "GPT-3.5":
#     model = "gpt-3.5-turbo"
# else:
#     model = "gpt-4"

# reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a Singlife Advisor assistant."}
    ]
    # st.session_state['number_tokens'] = []
    # st.session_state['model_name'] = []
    # st.session_state['cost'] = []
    # st.session_state['total_cost'] = 0.0
    # st.session_state['total_tokens'] = []
    # counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
# container for chat history
response_container = st.container()
# container for text box
container = st.container()
with container:
    with st.form(key='my_form', clear_on_submit=True):
    # st.write('data')
     user_input = st.text_area("Enter Q&A  :", key='prompt')
     submit_button = st.form_submit_button(label='Send')
    # input_data = "Create summary in 300 words in very simple english language without any grammar mistake ,simple sentence ,active voice and use more we and you and keep usage of promoun for below conversation between Financial Advisor and Customer :\n\nConversation:"+prompt
    # submit_form = st.form_submit_button(label="submit", help="Click to submit")
     if user_input and submit_button:
        output= generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        # st.session_state['model_name'].append(model_name)
        # st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
        # st.write("total_tokens....",total_tokens)
        # if model_name == "GPT-3.5":
        #     total_tokens=float(total_tokens)
        #     cost = ((total_tokens/1000) * 0.002)
        
        # else:
        #     prompt_tokens=float(prompt_tokens)
        #     completion_tokens= float(completion_tokens)
        #     cost = (((prompt_tokens/1000) * 0.03) + ((completion_tokens/1000 * 0.01))) 

        # st.session_state['cost'].append(cost)
        # st.session_state['total_cost'] += cost

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            # st.write(
            #     f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
            # counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
      

with st.form(key = 'history'): 
     view_history = st.form_submit_button(label="view", help="Click to view")
     if view_history:
        cxn = sqlite3.connect("UIUX"+'.db')
   
        c = cxn.cursor()
        c.execute("select name  from UIUX" ) 
        found_records = c.fetchall();
        for record in found_records:
            st.write(record)
            st.write("\n")

        cxn.commit()
        cxn.close()



