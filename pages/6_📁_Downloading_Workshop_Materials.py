import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Accessing Materials',
    page_icon='📁'
)

local_css("css/style.css")

st.title("Accessing and opening Jupyter Notebooks")

st.markdown("""

### Download the Python Pre-sessional workshop materials

The DSL teaches Python using Jupyter Notebooks.

You can download the notebooks from below.

### Python Fundamentals

The Python Fundamentals workshops are for beginners that have no prior experience in programming with Python and cover the following topics:
- Numerical variables
- String variables
- Type casting
- Lists
- For loops
- Conditionals
- Writing functions
- Basics of data cleaning
- Basics of inspecting data (exploratory data analysis)
- Data visualisation
        
The notebooks will be combined into a single zip file. Mac-users can simple double click on the zip file to unpack the jupyter notebooks.
Window-users have to right-click on the zip file, select Extract All... and then click on Extract.
            
This should create a new folder named PF_notebooks which contains the different jupyter notebook files.
""")


with open("materials/PythonSeries.zip", "rb") as f:
    btn = st.download_button(
        label = "Download Python materials",
        data = f,
        file_name = "PythonSeries.zip",
        mime = "application/zip"
        )


st.markdown(
    """
<br>

 <div class="highlight blue">
    Come to the pre-sessional workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="Pre-sessional_Workshops", target="_self">Python Pre-sessional workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
### Next step

Go to the Opening Jupyter Notebooks section and follow
the instructions to open the Jupyter Notebooks and Python code in a Jupyter Notebook.
"""
)
