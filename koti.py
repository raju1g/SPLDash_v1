# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:30:14 2021

@author: raju1g
"""
import streamlit as st
import header as he
import utils
from utils import image_to_bytes


def main(session_state):
    utils.localCSS("style.css")
    he.genHeader("0")
    st.write(
        f"""
        <div class="base-wrapper" style="background-color:#022B7E; margin: 0rem 42rem; transform: rotate(90deg); background-image: url({image_to_bytes('images/main_logo-03.png', 0)}); background-size: 850px; opacity:1; background-repeat: no-repeat;
        background-position: right; width: 1600px; height: 200px;">
        </div>
        <div class="base-wrapper" style="background-color:#022B7E; background-position: right; background-image: url({image_to_bytes('images/main_logo-04.png', 0)}); background-repeat: no-repeat; opacity:1; background-size: 850px;">
            <div class="hero-wrapper">
                <div class="hero-container" style="width:50%;">
                    <div class="hero-container-content">
                        <span class="subpages-container-product white-span"></span>
                        <span class="subpages-subcontainer-product white-span">Suomen Palloliitto Dashboard</span>
                    </div>
                </div>
            </div><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
