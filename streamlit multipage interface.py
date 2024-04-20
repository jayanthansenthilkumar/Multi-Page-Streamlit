import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import numpy as np


def page1():
    st.header("Sample")
    st.text_input("Your Name", key="name")
    st.session_state.name

    today = datetime.today()
    start_date = today - timedelta(days=365 * 150)
    end_date = today

    select_date = st.date_input("DOB", min_value=start_date, max_value=end_date)

    if select_date:
        age = today.year - select_date.year - ((today.month, today.day) < (select_date.month, select_date.day))
        st.write("Age:", age)

)

    if st.button("Go to page 2"):
        st.session_state.page = 2


def page2():
    st.title("Hello everyone👋 ")

    if st.button("Go to page 1"):
        st.session_state.page = 1


if 'page' not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()




