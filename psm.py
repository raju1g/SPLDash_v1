# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:30:14 2021

@author: raju1g
"""
import streamlit as st
import header as he
import utils

def main(session_state):
    utils.localCSS("style_new2.css")
    he.genHeader("2")
    st.write(
        f"""
            <div class="base-wrapper" style="background-color:#224B90;">
                <div class="hero-wrapper">
                    <div class="hero-container" style="width:100%;">
                        <div class="hero-container-content">
                            <span class="subpages-container-product white-span">Mittarit ja tunnusluvut</span>
                            <span class="subpages-subcontainer-product white-span">Yhteenveto</span>
                        </div>
                    </div>
                </div><br>
            </div>
            <div class="base-wrapper">
                <span> </span>
                <br><br>
                <embed>
            </div>
            """,
        unsafe_allow_html=True,
    )

    st.write(
        """
        <div class='base-wrapper' 
            <i>* <b>Oh no! We are not ready for you yet :( </b> </i>
            <br>
            <i>See you on August 15</i>
        </div>
        """,
        unsafe_allow_html=True,
    )
