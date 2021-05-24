import streamlit as st
import utils
import os

def genHeader(active):
    """ 
    This is a function that returns the "Footer" session 
    
    """
    if os.getenv("IS_HEROKU") == "TRUE":
        urlpath = os.getenv("urlpath")
    else:
        urlpath = '/share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py'

    if active == "0":
        st.write(
            f"""
               <div class="conteudo" id="navbar">
               <a>&nbsp;</a>
               <a class="active" href="{urlpath}?page=initial">Koti</a>
               <a href="{urlpath}?page=spm">Strategiaprojektit</a>
               <a href="{urlpath}?page=psm">Mittarit ja tunnusluvut</a>
               </div>
               """,
            unsafe_allow_html=True,
        )
    if active == "1":
        st.write(
            f"""
                <div class="conteudo" id="navbar">
                <a>&nbsp;</a>
                <a href="{urlpath}?page=initial">Koti</a>
                <a class="active" href="{urlpath}?page=spm">Strategiaprojektit</a>
                <a href="{urlpath}?page=psm">Mittarit ja tunnusluvut</a>
                </div>
                """,
            unsafe_allow_html=True,
        )
    elif active == "2":
        st.write(
            f"""
                <div class="conteudo" id="navbar">
                <a>&nbsp;</a>
                <a href="{urlpath}?page=initial">Koti</a>
                <a href="{urlpath}?page=spm">Strategiaprojektit</a>            
                <a class="active" href="{urlpath}?page=psm">Mittarit ja tunnusluvut</a>
                </div>
                """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
