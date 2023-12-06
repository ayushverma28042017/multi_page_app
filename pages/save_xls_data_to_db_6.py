import sqlite3
import pandas as pd
import streamlit as st
import pandas as pd
import openpyxl as openpyxl
from dotenv import load_dotenv
import os 


load_dotenv(".streamlit/secrets.toml")
st.text("# save data from xlx file to SQL DB ")
st.text("# save data from xls file to SQL DB ")
st.text("# To know the table schema enter PRAGMA table_info({dbname});")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    prompt = st.text_input("Enter the DB name", key='prompt')
    database_name=prompt
    cxn = sqlite3.connect(prompt+'.db')
    wb = pd.read_excel(uploaded_file, sheet_name='TestSet')

# dataframe
    wb.to_sql(name=prompt,con=cxn,if_exists='replace',index=True)
    cxn.commit()
    cxn.close()

    with st.form(key = 'execute_sql'):
        st.write('SQL')
        promptDb = st.text_input("Enter DB name :", key='promptDb')
        promptsql = st.text_input("Enter your sql:", key='promptsql')
        submit_form = st.form_submit_button(label="Execute", help="Click to execute query!")
        if submit_form:
            con = sqlite3.connect(promptDb+".db")
            cur = con.cursor()
            rows = cur.execute(promptsql).fetchall()
            st.write(rows)
            con.close()

   
