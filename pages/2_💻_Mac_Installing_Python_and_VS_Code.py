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
## Installing Miniconda, Python, Jupyter Notebook and VS Code on your MacBook
        
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

Depending on whether your Mac has an M1/M2 or Intel processor, you will have to download a different version of miniconda and VS Code. Check the processor 
type by clicking on the Apple icon in the top left corner of your screen and selecting About this Mac. 

If you have an M1/M2 processor, you will see Apple M1 in the Overview tab. If you have an Intel processor, you will see Intel in the Overview tab.

""")        

st.image("img/mac_processor.png", width=400)

st.markdown(
    """

For Intel Macs, download and install [this file](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg).

For M1-M3 Mac, download and install [this file](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg).
""")        


st.markdown(
    """
### Installing VS Code
    
Go to [this website](https://code.visualstudio.com/download#).

1. Download the installer.
    - If you have an Intel Mac, select intel-chip as you can see in the highlighted section below.
    - If you have an M1-M3 Mac, select Apple silicon in the highlighted section.
2. Double click on the installer file. Drag the VS Code icon into your application folder.
""")        

st.image("img/vs_code_mac.png", width=300)



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
