


st.sidebar.title("App settings")
st.sidebar.text_input("Enter your name")
st.sidebar.selectbox("Developer role",options=["React","Java","Python"])

import streamlit as st;
st.title("MySQL Workbench + Streamlit App")
conn: SQLConnection = st.connection("mysql", type="sql")
df: DataFrame = conn.query("SELECT * FROM employees LIMIT 100;", ttl="10m")
#ttl = time to live
st.dataframe(df);

#