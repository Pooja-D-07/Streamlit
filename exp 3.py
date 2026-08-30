import streamlit as st;
import pandas as pd;

table_data = pd.DataFrame({
    "Student_name : ["pooja","riya","Sooriya"],
    "gender":["M","M","F"],
    "Fees":[100,200,300],
    "Marks":[90,89,78]


st.title("Column Config"):
st.dataframe(table_data,hide_index=True,
             column_config={
                 "Fees":st.column_config.NumberColumn{
                     "Exam Fees",
                     format=" $ %d"
                 }
             }
);

             st.dataframe(table_data,column_config={
                 "Marks:st.column_config.progressColumn{
                 "student Marks",
                 help="Score out of 100",
                 min_value=0,
                 max_value=100,
                 format="%d Marks"
             }
})