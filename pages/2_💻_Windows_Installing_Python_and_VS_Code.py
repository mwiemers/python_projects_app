import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css



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
## Installing Miniconda, Python, Jupyter Notebook and VS Code on your Windows laptop
        
With Miniconda you can install Python, Python libraries and easily manage different Python environments on your personal laptop.
            
You will use Miniconda in combination with VS Code to write code in Python using Jupyter Notebooks.
            
The final video will show you how to open the Python exercises as jupyter notebooks in VS Code and how to write and run Python code.
        
""")

st.image("img/conda_logo.webp", caption='Anaconda', width=500)

st.markdown("""
You can change the width of the video to span across the entire webpage. See instructions below.
""")
st.image("img/settings.png", width=400)


st.markdown(
    """
### Installing Miniconda

Download and run [this file](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe).

During the installation, when being asked, tick the option to **add Miniconda3 to the my PATH environemt variable**.
""")        

st.image("img/miniconda_add_to_path.png", width=400)




st.markdown(
    """
### Installing VS Code
    
Go to [this website](https://code.visualstudio.com/download#).

1. Download the installer as highlighted in the image below.
2. Run the installer.
""")        

st.image("img/vs_code_win_install.png", width=300)



st.markdown(
    """
### Setting up VS Code
    
1. Open VS Code
2. On the left-hand menu open the Extensions section.
""")        

st.image("img/vs_code_extensions.png", width=300)

st.markdown(
    """
3. Search and install the Python and Jupyter extension.
    - Search in the search bar for python and then click install.
    - Search for jupyter and click install.
""")       

st.image("img/vs_code_extensions2.png", width=300)



st.markdown(
    """
### Next step
Go to the Downloading Workshop Materials section and follow the instructions to download the Jupyter Notebooks, which contain the exercises 
 for the Python workshops, on your personal laptop.
"""
)
