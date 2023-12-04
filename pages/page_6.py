import sqlite3
import pandas as pd
import streamlit as st
import pandas as pd
from io import StringIO
import openpyxl as openpyxl

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    cxn = sqlite3.connect('dyiDB.db')
    # wb = pd.read_excel(uploaded_file)
    wb = pd.read_excel(uploaded_file, sheet_name='TestSet')

# dataframe
    wb.to_sql(name='dyi',con=cxn,if_exists='replace',index=True)
    cxn.commit()
    cxn.close()
   
st.markdown("# save data from xlx file to SQL DB ")
st.sidebar.markdown("# save data from xlx file to SQL DB 🎉")