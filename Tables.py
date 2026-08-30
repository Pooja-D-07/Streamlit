import pandas as pd
import streamlit as st

table = pd.DataFrame(
    {
        "student_name": ["Pooja", "Reshmi", "Saran", "preethi", "Ram","Varun"],
        "Gender": ["F", "F", "M", "F", "M","M"]
    }
)

# FIXED: Changed Tables_data to table
st.title("Tables")
st.table(table)

st.title("DataFrame")
st.dataframe(table,hide_index=True,
             use_container_width=True)

st.title("Data Editor")
st.data_editor(table,num_rows="dynamic")

table = pd.DataFrame(
    {
        "student_name": ["Pooja", "Reshmi", "Saran", "preethi", "Ram"],

        "Maths": [ 10,20,30,40,50],
        "Physics":[30,40,44,66,87],
        "Chemistry":[36,87,98,90,100]
    }
)
import streamlit as st
import pandas as pd

table_data = pd.DataFrame({
    "Student_name": ["pooja", "riya", "Sooriya"],
    "gender": ["M", "M", "F"],
    "Fees": [100, 200, 300],
    "Marks": [90, 89, 78]
})

st.title("Column Config")

st.dataframe(
    table_data,
    hide_index=True,
    column_config={
        "Fees": st.column_config.NumberColumn(
            "Exam Fees",
            format="$ %d"
        ),
        "Marks": st.column_config.ProgressColumn(
            "Student Marks",
            help="Score out of 100",
            min_value=0,
            max_value=100,
            format="%d Marks"
        )
    }
)
st.data_editor{
    table_data,
    
}
