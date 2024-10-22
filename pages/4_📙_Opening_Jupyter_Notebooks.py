import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css


st.set_page_config(
    page_title='Opening Jupyter Notebooks',
    page_icon='📙'
)

local_css("css/style.css")

st.title("Opening Jupyter Notebooks")


st.markdown(
    """
### Open and work with Jupyter Notebooks

If you haven't unzipped and placed the jupyter notebooks in a specific folder, do this first. You can find instructions in the last step of the previous page.

Below are the steps you need to take to open the Python jupyter notebooks in VS Code. Apart from step 1, **this is also shown in the video**.
""")

st.markdown(
    """
1. Open the VS Code app.
2. Open the PF_notebooks folder, which contains the different jupyter notebook files. Go to Files > Open Folder and the select the folder.
3. Click on the first jupyter notebook to open it.
4. Select the kernel, which is the Python version by clicking on the **Select Kernel** button.
""")

st.image("img/select_kernel_01.png")

st.markdown(
    """
5. Select **Python Environments...**
""")

st.image("img/select_kernel_02.png")

st.markdown(
    """
5. Select the **base** environment.
""")

st.image("img/select_kernel_03.png")

st.markdown(
    """
6. Scroll down to the first task and hit the Run button next to the code cell. This button is used to execute the code inside a code cell.
""")

st.image("img/install_jupyter_01.png")

st.markdown(
    """
7. VS Code will prompt you to install the jupyter libraries. Select Install
""")

st.image("img/install_jupyter_02.png", width=200)

st.markdown(
    """
    A pop up window will appear in the lower-right corner of the VS Code app. Wait until the installation has been completed.
""")

st.image("img/install_jupyter_03.png", width=400)


st.markdown(
    """

    &nbsp;
    &nbsp;

    You are all set to use jupyter notebooks in VS Code now. Please remember, that you will have to select the kernel and chose the base environment every time you open a jupyter notebook.

    &nbsp;
""")



st.markdown(
    """
### Next step

Go to the DSL Python workshops section to 
learn about the format of the Python workshops and how to sign up for a session.
"""
)
