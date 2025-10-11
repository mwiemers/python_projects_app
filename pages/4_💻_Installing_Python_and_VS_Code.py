import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css


def play_video(file_name):
    try:
        with open(file_name, "rb") as file:
            video_bytes = file.read()
        st.video(video_bytes, format="video/mp4", start_time=0)
    except FileNotFoundError:
        st.error(f"Local video file '{file_name}' not found.")

def load_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image


st.set_page_config(
    page_title='Installing Python',
    page_icon="💻"
)

local_css("css/style.css")

st.markdown("""
## Installing Anaconda, Jupyter Notebook and VS Code on your MacBook
        
With Anaconda you can install Python, Python libraries and easily manage different Python environments on your personal laptop.
            
You will use Anaconda in combination with VS Code to write code in Python using Jupyter Notebooks.
            
The final video will show you how to open the Python exercises as jupyter notebooks in VS Code and how to write and run Python code.
        
""")

st.image("img/conda_logo.webp", caption='Anaconda', width=500)

st.markdown("""
You can change the width of the video to span across the entire webpage. See instructions below.
""")
st.image("img/settings.png", width=400)


st.markdown(
    """
### Downloading Anaconda Installation File

Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of Anaconda. Check the processor 
type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac.

If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.
""")        
st.image("img/mac_processor.png", width=500)

st.markdown(
    """
Please go to [this website](https://www.anaconda.com/download/success) to download the distribution installer (Anaconda).
"""
)

st.image("img/download_anaconda.jpg", width=500)


st.markdown(
    """
### Installing Anaconda
    
Double click the installation file and follow the instructions.
""")        



st.markdown(
    """
### Downloading VS Code Installation File
    
Please go to [this website](https://code.visualstudio.com/download) to download the installation file for your operating system and CPU type.
""")        

st.image("img/vs_code_installation.png", width=600)



st.markdown(
    """
### Installing and setting up VS Code (Mac)
    
Follow the steps from the video to install and set up VS Code for Python and Jupyter Notebooks on your MacBook.
""")        

vs_code_installation_mac_video = "screen_rec/mac/install_setup_vs_code_edited.mp4"  

play_video(vs_code_installation_mac_video)


st.markdown(
    """
### Installing and setting up VS Code (Windows)
    
Follow the steps from the video to install and set up VS Code for Python and Jupyter Notebooks on Windows.
""")        

vs_code_installation_mac_video = "screen_rec/win/install_setup_vs_code_win_edited.mp4"  

play_video(vs_code_installation_mac_video)


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
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python workshops, on your personal laptop.
"""
)
