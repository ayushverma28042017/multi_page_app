import sqlite3
import pandas as pd
import streamlit as st
import pandas as pd
from io import StringIO
import openpyxl as openpyxl

st.markdown("# save data from xlx file to SQL DB ")
st.sidebar.markdown("# save data from xls file to SQL DB ")
st.sidebar.markdown("# to know the table schema enter PRAGMA table_info(mmyyddbb);")


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

# st.markdown("# Query SQL🎉")
# st.sidebar.markdown("# Query SQL 🎉")
   
