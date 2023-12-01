import streamlit as st
import sqlite3


con = sqlite3.connect("elixir01_db.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS elixirdb(POLICY_NO INTEGER , NRIC TEXT)")
cur.execute("INSERT INTO elixirdb VALUES (3037850,'T0518890G')")
con.commit



rows = cur.execute("SELECT POLICY_NO,NRIC FROM elixirdb").fetchall()
st.write(rows)
con.close()

st.markdown("# Page 3 🎉 {data}")
st.sidebar.markdown("# Page 3 🎉")