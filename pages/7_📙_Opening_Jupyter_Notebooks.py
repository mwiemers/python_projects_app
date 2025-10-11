import streamlit as st
from load_css import local_css


def play_video(file_name):
    try:
        with open(file_name, "rb") as file:
            video_bytes = file.read()
        st.video(video_bytes, format="video/mp4", start_time=0)
    except FileNotFoundError:
        st.error(f"Local video file '{file_name}' not found.")

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
4. Select the kernel. The kernel is the specific Python environment to use. We set up the py312 environment with Python 3.12 in a previous step and will use this to 
work with the jupyter notebooks.
5. Read through the description about the workshops/scroll down to the first exercise.
6. Type in your solution code in the code cell and run the code with the Cmd+Enter (Mac) or Ctrl+Enter (Win) keyboard shortcut.
""")

vs_code_jupyter_notebooks_video = "screen_rec/both/vs_code_jupyter_notebooks2.mov"

play_video(vs_code_jupyter_notebooks_video)




st.markdown(
    """
<br>

 <div class="highlight blue">
    Come to the pre-sessional workshops if you struggle with any of the steps from this tutorial. You can find more information about the workshops in the 
    <a href="https://dsl-python-presessional.streamlit.app/Pre-sessional_Workshops", target="_self">Python Pre-sessional workshops section</a>.
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
### Next step

Go to the Pre-sessional workshops section to 
learn about the format of the Python workshops and how to sign up for a session.
"""
)
