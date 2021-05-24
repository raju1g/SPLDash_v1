import streamlit as st
import utils
import os

def genHeader(active):
    """ 
    This is a function that returns the "Footer" session 
    
    """
    urlpath = 'https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py'

    if active == "0":
        st.write(
            f"""
               <div class="conteudo" id="navbar">
               <a>&nbsp;</a>
               <a class="active" href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=initial">Koti</a>
               <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=spm">Strategiaprojektit</a>
               <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=psm">Mittarit ja tunnusluvut</a>
               </div>
               """,
            unsafe_allow_html=True,
        )
    if active == "1":
        st.write(
            f"""
                <div class="conteudo" id="navbar">
                <a>&nbsp;</a>
                <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=initial">Koti</a>
                <a class="active" href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=spm">Strategiaprojektit</a>
                <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=psm">Mittarit ja tunnusluvut</a>
                </div>
                """,
            unsafe_allow_html=True,
        )
    elif active == "2":
        st.write(
            f"""
                <div class="conteudo" id="navbar">
                <a>&nbsp;</a>
                <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=initial">Koti</a>
                <a href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=spm">Strategiaprojektit</a>            
                <a class="active" href="https://share.streamlit.io/raju1g/spldash_v1/main/SPLDash_v1.py?page=psm">Mittarit ja tunnusluvut</a>
                </div>
                """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
