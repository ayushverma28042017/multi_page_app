import streamlit as st
import sqlite3


# con = sqlite3.connect("elixir01_db.db")
con = sqlite3.connect("dyiDB.db")

cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS elixirdb(POLICY_NO INTEGER , NRIC TEXT)")
# cur.execute("INSERT INTO elixirdb VALUES (3037850,'T0518890G')")
# con.commit

with st.form(key = 'execute_sql'):
        st.write('SQL')
        prompt = st.text_input("Enter your sql:", key='prompt')
        submit_form = st.form_submit_button(label="Execute", help="Click to execute query!")
        if submit_form:
            rows = cur.execute(prompt).fetchall()
            st.write(rows)
# rows = cur.execute("SELECT * FROM dyi").fetchall()
# st.write(rows)
con.close()

st.markdown("# Query SQL🎉")
st.sidebar.markdown("# Query SQL 🎉")