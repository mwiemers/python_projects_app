import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from load_css import local_css



st.set_page_config(
    page_title='Effective Use of Claude/GenAI Tools',
    page_icon="🤖"
)

# Method 1: Display the HTML directly
with open('pages/claude_learning_guide.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
    st.components.v1.html(html_content, height=1750, scrolling=True)


st.markdown(
    """
### Next step
Go to the Installing Python and VS Code page to find out how to setup Python on your personal laptop.
"""
)
