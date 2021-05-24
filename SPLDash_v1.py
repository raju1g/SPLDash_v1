# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:30:14 2021

@author: raju1g
"""
import streamlit as st
import utils
import koti as kt
import spm as spm
import psm as psm
import time
import session
#from State import _get_state
#from excel_cleaner_old import excel_cleaner
#import numpy as np
#from datetime import datetime

st.set_page_config(
    page_title='SPL Dashboard',
    page_icon='images/favicon.ico',
    layout='wide',
    initial_sidebar_state='collapsed'
)

utils.local_css('style.css')


def main():
    # SESSION STATE
    time.sleep(
        0.05
    )  # minimal wait time so we give time for the user session to appear in steamlit
    session_state = session.SessionState.get()
    # Set tabs variables and check which tab is activated
#    st.sidebar.markdown(
#        f"<div style='background-color:#022B7E; "
#        f"width: 3840px; height: 2160px; z-index: 0; background-image: url({image_to_bytes('Untitled-1-02.png', 0)}); "
#        f"background-repeat: no-repeat; background-position: center; background-size: 2000px;'>&nbsp;</div>",
#        unsafe_allow_html=True
#    )

#    st.markdown(
#        "<div style='text-align: center;'</div><p1>Suomen Palloliitto Dashboard</p1>", unsafe_allow_html=True
#    )
#    st.markdown(
#        "<div style='text-align: center;'</div><p3>Valitse moduuli</p3>", unsafe_allow_html=True
#    )

    #page = st.radio("Valitse moduuli", tuple(pages.keys()))
    st.write(
        """
    <iframe "resources/sidebar-closer.html" height=0 width=0>
    </iframe>""",
        unsafe_allow_html=True,
    )

    page_list = ["Koti", "Strategiaprojektit", "Mittarit ja tunnusluvut"]
    pages_dict = {
        "Koti": "initial",
        "Strategiaprojektit": "spm",
        "Mittarit ja tunnusluvut": "psm",
    }
    pages_index = {
        "initial": 0,
        "spm": 1,
        "psm": 2,
    }
    PAGES = {
        "initial": kt,
        "spm": spm,
        "psm": psm,
    }
    query_params = st.experimental_get_query_params()
    if query_params:
        # Gambiarra para redirecionar páginas
        if query_params["page"][0] == '0' or query_params["page"][0] == 'Koti':
            query_params["page"][0] = "initial"
        elif query_params["page"][0] == '1' or query_params["page"][0] == 'Strategiaprojektit':
            query_params["page"][0] = "spm"
        elif query_params["page"][0] == '2' or query_params["page"][0] == 'Mittarit ja tunnusluvut':
            query_params["page"][0] = "psm"
    default = query_params["page"][0] if "page" in query_params else "initial"
    st.sidebar.markdown(
        f"<div style='margin: -5rem -0.25rem; width: 310px; height: 1200px; opacity: 0.5; position: fixed; background-color: #022B7E;'>&nbsp;</div>",
        unsafe_allow_html=True)
    st.sidebar.markdown(
        "<h2 style='text-align: center; color: #022B7E; font-family:sans-serif;'>Valitse moduuli</h2>",
        unsafe_allow_html=True,
    )
    page = st.sidebar.selectbox("", page_list, index=pages_index[default])
#    st.sidebar.header("Valitse moduuli")
#   page = st.sidebar.radio("", page_list, index=pages_index[default])
#   page = st.sidebar.radio("", page_list, index=pages_index[default])
    st.experimental_set_query_params(page=pages_dict[page])
    PAGES[pages_dict[page]].main(session_state)


if __name__ == "__main__":
    main()





















