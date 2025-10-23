import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px


DROPDOWN_VALUES = ['TSLA', 'MSFT', 'GOOG', 'META', 'NFLX', 'AMZN', 'BTC-USD']

st.set_page_config(
    page_title='Accessing Claude',
    page_icon="🤖"
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("img/claude.gif", width=400)

st.markdown(
    """
### Using Claude for your digital skills development

AI tools like Claude can be powerful learning companions when you're starting to code. Rather than just generating solutions, 
think of them as a patient tutor available 24/7. When you're stuck on a concept, ask for explanations in your own words
 or request analogies that make sense to you. Encountering an error? Paste your code and ask the AI to help you understand
  why it's breaking—not just fix it. Another effective way to engage with Claude is "learning mode": Change the response style
  to learning mode and they will guide you through problems step-by-step with questions rather than answers, 
  helping you discover solutions yourself. This approach builds genuine understanding and problem-solving skills. 
  Remember, the goal isn't to have AI write your code, but to use it as a coach that helps you think like a programmer 
  and develop the skills to solve problems independently.
"""
)

st.markdown(
    """
### Accessing Claude

LSE is now offering Anthropic’s [‘Claude for Education’](https://www.anthropic.com/education) AI technology, to all students and academic staff free of charge. 
Claude is an educationally focused AI tool that can help with tasks such as summarising complex information, creating 
personalised study plans, and assisting with data analysis and visualisation. 

Claude should be used in accordance with [School-wide guidance on generative AI](https://info.lse.ac.uk/current-students/digital-skills-lab/Gen-AI)
 and any specific guidance set out by 
your programme, course or department.

LSE students and academic staff can request access to Claude by completing [this form](https://link.lse.ac.uk/requestClaude). 

"""
)

st.markdown(
    """
### Not sure how to use Claude for your digital skills development?

Go to the next page for an overview of effective ways to use Claude and similar GenAI tools to learn new digital skills.
"""
)