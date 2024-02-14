import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu


# global varibales for UI
hide_streamlit_label = """
                            <style>
                                footer {visibility: hidden;}
                                footer: before {
                                content: 'Techweck';
                                visibility: visible;
                                display: block;
                                position: relative;
                                background-color: #00338d; color: white; font-weight: 500; font-size: 16px; padding:
                                5px;
                                top: 2px;
                                footer: after {
                                content: '©'；
                                visibility: visible;
                                display: block;
                                position: relative;
                                # background-color: #0090da;
                                color: grey; font-weight: 300; font-size: 10px; padding: 5px;
                                top: 2px;
                                }
                            </style>
                        """
col_summary_html='''
                    <h3 style="background-color: #00338d;
                                color: white; font-weight: 600; text-align: center;
                                top: 2px; font-size: 20px; display: block;
                                position: relative;
                                padding: 4px;">Summary Metrics number</h3>
                    <h4 style="background-color: #00338d;
                                color: white; font-weight: 600; text-align: center;
                                top: 2px; font-size: 15px; display: block;
                                position: relative;
                                padding: 4px;">This is a metric card</h4>
                    <p style="background-color: #00338d;
                                color: white; font-weight: 600; text-align: center;
                                top: 2px; font-size: 12px; display: block;
                                position: relative;
                                padding: 4px;">This is message</p>
                '''


# App page configurations:
st.set_page_config(
    page_title="Personal Website",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)


# Defining the sidebar UI
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(col_summary_html, unsafe_allow_html=True)

with col2:
    st.markdown(col_summary_html, unsafe_allow_html=True)

with col3:
    st.markdown(col_summary_html, unsafe_allow_html=True)

with col4:
    st.markdown(col_summary_html, unsafe_allow_html=True)

st.markdown(hide_streamlit_label, unsafe_allow_html=True)

