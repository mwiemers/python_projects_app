import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='DSL Python workshops',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python workshops")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Development Lead - Academic Partnerships
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    Python is pre-installed on all teaching PCs in our library training room LRB.R08.

    If you wish to install Python on your personal laptop, please follow the instructions on this website to install Python + VS Code to use Jupyter Notebooks.

    For students joining the Python Bootcamp, please follow the installation instructions, as the teaching room will NOT have PCs.
    
    We recommend to set apart 30 minutes to work through this tutorial (excluding the optional sections on installing libraries and managing environments).

    Please work through the pages from the sidebar menu for information about:
    * Why Python is one of the most popular programming languages and why you should learn it.
    * How you can install Python + VS Code on your personal laptop.
    * The Python workshops format and timetable.
    * How to access the Python workshop materials from this website.
    * How to access and work with jupyter noteboos in VS Code.
    * How to install libraries and create and manage environments with conda (optional).

    &nbsp;

    <div class="highlight blue">
    Come to the workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="Python_Workshops", target="_self">Python workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)
