import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Digital Skills Lab Python for Mathematics workshops',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python for Mathematics workshops")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Development Lead (Academic Partnerships)  
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    The DSL Python for Mathematics workshops support is divided into two main parts:

    1. The instructions from this website to install Python + VS Code on your laptop to use Jupyter Notebooks (30 min)
    2. The on-campus Python workshops to learn the fundamentals of programming in Python (10-12 hours of learning).

    Please follow the instructions on this website to install Python + VS Code to use Jupyter Notebooks before 
    you join the DSL Python for Mathematics workshops.
    
    We recommend to set apart 30 minutes to work through this tutorial (excluding the optional sections on installing libraries and managing environments).

    Please work through the pages from the sidebar menu for information about:
    * Why Python is such a popular programming language and why you should learn it.
    * How you can install Python + VS Code on your personal laptop.
    * The Python workshops format and timetable.
    * How to access the Python workshop materials from this website.
    * How to access and work with jupyter noteboos in VS Code.
    * How to install libraries and create and manage environments with conda (optional).

    &nbsp;
    """, unsafe_allow_html=True
)
