# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 09:41:50 2021

@author: GeetRaju
"""
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)