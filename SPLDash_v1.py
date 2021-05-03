# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 09:21:15 2021

@author: GeetRaju
"""
import streamlit as st
import plotly
import streamlit.components.v1 as components
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
from load_css import local_css
import SessionState
import openpyxl


session_state = SessionState.get(page_number=0)

menu1 = ["---", "Projekti 1 - Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
         "Projekti 2", "Projekti 3", "Projekti 4", "Projekti 5"]
menu2 = ["---", "Tulospalvelu", "Pelipaikka", "Nettisivut"]
menu3 = ["---", "Pelaajakehitys", "Erotuomari-toiminnan järjestäminen", "Kilpailu-toiminnan järjestäminen",
         "Seura-toimijoiden rekrytointi ja osaamisen kehittäminen", "Pelaajien rekrytointi ja mukana pitäminen",
         "Valmentajien koulutus ja osaamisen kehittäminen", "Sidosryhmäyhteistyö ja –vaikuttaminen",
         "Myynti ja markkinointi", "Olosuhteiden rakennuttaminen ja ylläpito", "Tukitoiminta"]

# Page layout
st.set_page_config(
    page_title="SPL Dashboard",
    page_icon="images/favicon.ico",
    layout='wide',
    initial_sidebar_state='auto'
    )
local_css("style.css")

# Home Page
# Title banner
row00_space1, row00_1, row00_space2 = st.beta_columns([0.01, 1, 0.01])
with row00_1:
    HTML_BANNER1 = """
        <div style="background-color:#4f6994;padding:3px;border-radius:30px">
        <h1 style="color:white;text-align:center;font-family:sans-serif;">Suomen Palloliitto Dashboard</h1><p>&nbsp;</p>
        </div>
        """
    components.html(HTML_BANNER1)

# SPL Logo and selection buttons
row01_space1, row01_space2, row01_1, row01_space3, row01_space4 = st.beta_columns([1.25, 1, 1, 1, 1])
with row01_1:
    st.image("images/spl_logo.png", width=200)
row02_space1, row02_space2, row02_1, row02_space3, row02_space4 = st.beta_columns([1.7, 1, 2, 1, 1])
with row02_1:
    st.markdown("<h1>Valitse moduuli</h1><p>&nbsp;</p>", unsafe_allow_html=True)
row03_space1, row03_1, row03_2, row03_space2 = st.beta_columns([1.1, 1, 1, 0.5])
with row03_1:
    if st.button('Strategiaprojektit'):
        session_state.page_number = 1 
with row03_2:
    if st.button('Mittarit ja tunnusluvut'):
        session_state.page_number = 2
st.markdown("""
---------------------------------------------------------------- 
""")

# Strategic Project Monitoring Section
if session_state.page_number == 1:
    st.sidebar.markdown(
        "<h2 style='text-align: center;font-family:sans-serif;'>Valitse <br> strategiaprojekti</h2>",
        unsafe_allow_html=True)
    choice = st.sidebar.selectbox("", menu1)

    row04_space1, row04_1, row04_2 = st.beta_columns([1, 2, 0.5])
    with row04_1:
        st.markdown(
            "<h1 style='text-align: center;font-family:sans-serif;'>Strategiaprojektin yhteenveto</h1>",
            unsafe_allow_html=True)
    with row04_2:
        st.image("images/spl_logo.png", width=25)

    row05_space1, row05_1, row05_2, row05_3, row05_4, row05_5, row05_space2 = st.beta_columns([0.4, 1, 1, 1, 1, 1, 0.1])
    with row05_1:
        st.markdown(
            "<h3 style='text-align: center;font-family:sans-serif;'>Parannamme Palloliiton perusjärjestelmien "
            "<br>ja verkkopalvelujen käytettävyyttä</h3>", unsafe_allow_html=True)
    with row05_2:
        st.markdown(
            "<h3 style='text-align: center;font-family:sans-serif;'>Parannamme Palloliiton perusjärjestelmien "
            "<br>ja verkkopalvelujen käytettävyyttä</h3>", unsafe_allow_html=True)
    with row05_3:
        st.markdown(
            "<h3 style='text-align: center;font-family:sans-serif;'>Parannamme Palloliiton perusjärjestelmien "
            "<br>ja verkkopalvelujen käytettävyyttä</h3>", unsafe_allow_html=True)
    with row05_4:
        st.markdown(
            "<h3 style='text-align: center;font-family:sans-serif;'>Parannamme Palloliiton perusjärjestelmien "
            "<br>ja verkkopalvelujen käytettävyyttä</h3>", unsafe_allow_html=True)
    with row05_5:
        st.markdown(
            "<h3 style='text-align: center;font-family:sans-serif;'>Parannamme Palloliiton perusjärjestelmien x"
            "<br>ja verkkopalvelujen käytettävyyttä</h3>", unsafe_allow_html=True)

    row06_space1, row06_1, row06_2, row06_3, row06_4, row06_5, row06_space2 = st.beta_columns([0.1, 1, 1, 1, 1, 1, 0.1])
    with row06_1:
        df_01 = pd.read_excel('data/state_of_tasks.xlsx')
        x_01 = ['']
        sizes_01 = [6, 11]
        fig_01 = go.Figure(
            go.Bar(x=x_01, y=[1], name='Voitto', texttemplate="%{y}<br>Voitto",
                   hovertemplate="<br>".join(["Tehtävät: %{---}"]), textposition="inside", textangle=0,
                   textfont_color="white", marker_color='#2ca02c'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[1], name='Hävi', texttemplate="%{y}<br>Häviö",
                   hovertemplate="<br>".join(["Tehtävät: %{---}"]), textposition="inside", textangle=0,
                   textfont_color="white", marker_color='#d62728'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[1], name='Jatkuva', texttemplate="%{y}<br>Tasapeli",
                   hovertemplate="<br>".join(["Tehtävät: %{---}"]), textposition="inside", textangle=0,
                   textfont_color="#4f6994", marker_color='yellow'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[5], name='Aloita', texttemplate="%{y}<br>Kesken",
                   hovertemplate="<br>".join(["Tehtävät: %{---}"]), textposition="inside", textangle=0,
                   textfont_color="#4f6994",marker_color='lightgrey'))
        fig_01.update_xaxes(
            showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
        fig_01.update_yaxes(
            showline=False, linewidth=0.25, linecolor='#4f6994', mirror=False, title='y', visible=False,
            showticklabels=False)
        fig_01.update_layout(
            barmode='stack', xaxis={'categoryorder': 'total descending'}, showlegend=False,
            uniformtext=dict(mode="hide", minsize=8), title_font_size=42, font_size=18, title_font_family='Arial',
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_showgrid=False, yaxis_showgrid=False)
        st.plotly_chart(fig_01, use_container_width=True)

        fig_02 = px.sunburst(
            df_01,
            path=["Overall", "Tasks", "Objectives"],
            color="State",
            color_discrete_map={'(?)': 'grey', 'Voitto': '#2ca02c', 'Hävi': '#d62728',
                                'Tasapeli': 'yellow', 'Ei aloitettu': 'lightgrey'}
        )
        fig_02.update_layout(margin=dict(t=10, l=10, r=10, b=10))
        fig_02.update_layout(width=300, height=300, showlegend=False, font_size=8)
        st.plotly_chart(fig_02, use_container_width=True)
    with row06_2:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
    with row06_3:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
    with row06_4:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
    with row06_5:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
    st.markdown("""
    ----------------------------------------------
    """)
    
    if choice == '---':
        st.write("")
    elif choice == 'Projekti 1 - Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä':
        st.sidebar.markdown(
            "<h2 style='text-align: center;font-family:sans-serif;'>Valitse <br> tavoitteet</h2>",
            unsafe_allow_html=True)
        choice9 = st.sidebar.selectbox("", menu2)
        if choice9 == '---':
            row07_1, row07_space1, row07_2 = st.beta_columns([5, 0.1, 0.25])
            with row07_1:
                st.markdown(
                    "<h1 style='text-align: center;font-family:sans-serif;'>"
                    "Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä </h1>",
                    unsafe_allow_html=True)
                st.markdown(
                    "<h2 style='text-align: center;font-family:sans-serif;'>TAVOITEET: Tulospalvelu, "
                    "Pelipaikka, Nettisivut </h2>",
                    unsafe_allow_html=True)
            with row07_2:
                st.image("images/spl_logo.png", width=25)
            row08_1, row08_space1 = st.beta_columns([4, 0.1])
            with row08_1:
                df_02 = pd.read_excel('data/tulospalvelu_gantt.xlsx')
                tasks = df_02['Tehtävä']
                start = df_02['Alkaa']
                finish = df_02['Loppunut']
                complete = df_02['Valmistuminen']
                status = df_02['State']
                colors = {'Voitto': '#2ca02c', 'Häviö': '#d62728', 'Tasapeli': 'yellow', 'Ei aloitettu': 'lightgrey'}
                fig_03 = px.timeline(
                    df_02, x_start=start, x_end=finish, y=tasks, color=status, color_discrete_map=colors)
                fig_03.add_shape(
                    type='line', x0='2021-05-01', y0=-0.5, x1='2021-05-01', y1='Kilpailutusvalinta',
                    line=dict(color='#4f6994', width=1.25, dash="dot"))
                fig_03.update_yaxes(autorange='reversed')
                fig_03.update_layout(
                    font_size=18, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                    xaxis_showgrid=False, yaxis_showgrid=False, showlegend=False)
                st.plotly_chart(fig_03, use_container_width=True)

            row09_space1, row09_1, row09_space2 = st.beta_columns([1.5, 1, 1])
            with row09_1:
                st.markdown(
                    "<h1 style='text-align: center;font-family:sans-serif;'>Mittarit</h1>", unsafe_allow_html=True)

            row10_space1, row10_1, row10_2, row10_3, row10_space2 = st.beta_columns([0.1, 1, 1, 1, 0.1])
            with row10_1:
                df_03 = pd.read_excel('data/mittarit1.xlsx')
                count = df_03['Count']
                year = df_03['Year']
                fig_04 = go.Figure()
                fig_04.add_trace(
                    go.Scatter(x=year, y=count, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[4, 4], fill='tozeroy', mode='none', fillcolor='rgba(255, 0, 0, 0.2)'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[4.9, 4.9], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[5, 5], fill='tonexty', mode='none', fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_04.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_04.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_04.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_04.add_annotation(
                    x=year[5], y=5.1, text="Max. (5.0)", showarrow=False, arrowhead=0)
                fig_04.add_annotation(
                    x=year[5], y=4.75, text="Tavoite (4.9)", showarrow=False, arrowhead=0)
                fig_04.update_layout(
                    title="Tulospalvelu: <br>Käyttäjäkokemukset", title_font_color="#4f6994", title_font_size=22,
                    showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_04, use_container_width=True)

            with row10_2:
                df_04 = pd.read_excel('data/mittarit2.xlsx')
                month = df_04['Month']
                percent = df_04['Percentage']
                fig_05 = go.Figure()
                fig_05.add_trace(
                    go.Scatter(x=month, y=percent, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[99, 99], mode='lines', line_color='rgba(255, 0, 0, 0.2)'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[99.5, 99.5], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[100, 100], fill='tonexty', mode='none',
                               fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_05.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_05.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_05.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_05.add_annotation(
                    x=month[0], y=100.035, text="Max. (100%)", showarrow=False, arrowhead=0)
                fig_05.add_annotation(
                    x=month[0], y=98.95, text="Tavoite (99%)", showarrow=False, arrowhead=0)
                fig_05.update_layout(
                    title="Tulospalvelu: <br>Käytettävissä", title_font_color="#4f6994", title_font_size=22,
                    showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_05, use_container_width=True)

            with row10_3:
                df_05 = pd.read_excel('data/mittarit3.xlsx')
                count2 = df_05['Count']
                year2 = df_05['Year']
                fig_06 = go.Figure()
                fig_06.add_trace(
                    go.Scatter(x=year2, y=count2, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_06.add_trace(
                    go.Scatter(x=[2020, 2024], y=[4, 4], mode='lines', line_color='rgba(255, 0, 0, 0.2)'))
                fig_06.add_trace(
                    go.Scatter(x=[2020, 2024], y=[4.5, 4.5], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_06.add_trace(
                    go.Scatter(x=[2020, 2024], y=[5, 5], fill='tonexty', mode='none', fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_06.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_06.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_06.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_06.add_annotation(
                    x=year2[0], y=5.05, text="Max. (5.0)", showarrow=False, arrowhead=0)
                fig_06.add_annotation(
                    x=year2[3], y=4.05, text="Tavoite (4.0)", showarrow=False, arrowhead=0)
                fig_06.update_layout(
                    title="Pelipaikka: <br>Seurojen tyytyväisyys Pelipaikan käyttöön", title_font_color="#4f6994",
                    title_font_size=22, showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_06, use_container_width=True)

            row11_space1, row11_1, row11_2, row11_3, row11_space2 = st.beta_columns([0.1, 1, 1, 1, 0.1])
            with row11_1:
                df_06 = pd.read_excel('data/mittarit4.xlsx')
                count3 = df_06['Count']
                month2 = df_06['Month']
                fig_07 = go.Figure()
                fig_07.add_trace(
                    go.Scatter(x=month2, y=count3, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_07.add_trace(
                    go.Scatter(x=[month2[0], month2[11]], y=[400, 400], fill='tozeroy', mode='none',
                               fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_07.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_07.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_07.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_07.add_annotation(
                    x=month2[5], y=420, text="Tavoite: Alle 400 vuodessa", showarrow=False, arrowhead=0)
                fig_07.update_layout(
                    title="Pelipaikka: Tukipyyntöjen lukumäärä <br>suhteessa rekisteröinteihin",
                    title_font_color="#4f6994", title_font_size=22, showlegend=False, font_size=12,
                    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_07, use_container_width=True)

            with row11_2:
                df_07 = pd.read_excel('data/mittarit5.xlsx')
                count4 = df_07['Count']
                year3 = df_07['Year']
                fig_08 = go.Figure()
                fig_08.add_trace(
                    go.Scatter(x=year3, y=count4, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_08.add_trace(
                    go.Scatter(x=[2020, 2024], y=[4, 4], mode='lines', line_color='rgba(255, 0, 0, 0.2)'))
                fig_08.add_trace(
                    go.Scatter(x=[2020, 2024], y=[4.5, 4.5], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_08.add_trace(
                    go.Scatter(x=[2020, 2024], y=[5, 5], fill='tonexty', mode='none', fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_08.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_08.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_08.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_08.add_annotation(
                    x=year3[0], y=5.05, text="Max. (5.0)", showarrow=False, arrowhead=0)
                fig_08.add_annotation(
                    x=year3[3], y=4.05, text="Tavoite (4.0)", showarrow=False, arrowhead=0)
                fig_08.update_layout(title="Nettisivut: <br>Tyytyväisyys nettisivuihin", title_font_color="#4f6994",
                                     title_font_size=22, showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_08, use_container_width=True)

            with row11_3:
                df_08 = pd.read_excel('data/mittarit6.xlsx')
                count5 = df_08['Number']
                month3 = df_08['Month']
                fig_09 = go.Figure()
                fig_09.add_trace(
                    go.Scatter(x=month3, y=count5, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_09.add_trace(
                    go.Scatter(x=[month3[0], month3[11]], y=[500000, 500000], fill='tozeroy', mode='none',
                               fillcolor='rgba(255, 0, 0, 0.2)'))
                fig_09.add_trace(
                    go.Scatter(x=[month3[0], month3[11]], y=[1000000, 1000000], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_09.add_trace(
                    go.Scatter(x=[month3[0], month3[11]], y=[2720266, 2720266], fill='tonexty', mode='none',
                               fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_09.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_09.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_09.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_09.add_annotation(
                    x=month3[5], y=2900000, text="Tavoite: 2 720 266", showarrow=False, arrowhead=0)
                fig_09.update_layout(
                    title="Nettisivut: <br>Kävijämäärät", title_font_color="#4f6994", title_font_size=22,
                    showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_09, use_container_width=True)

            st.markdown("""
            
            ---------------------------------------------------------------            
            
            """)

        elif choice9 == 'Tulospalvelu':
            row12_space1, row12_1, row12_2 = st.beta_columns([1.5, 2, 0.5])
            with row12_1:
                st.markdown(
                    "<h1 style='text-align: center;font-family:sans-serif;'>"
                    "Tulospalvelu </h1>", unsafe_allow_html=True)
            with row12_2:
                st.image(
                    "images/spl_logo.png", width=25)

            row13_space1, row13_1, row13_space2 = st.beta_columns([1.25, 2, 0.5])
            with row13_1:
                st.markdown(
                    "<h1 style='text-align: center;font-family:sans-serif;'>"
                    "Tehtävät ja Mittarit </h1>", unsafe_allow_html=True)

            row14_1, row14_space1 = st.beta_columns([4, 0.1])
            with row14_1:
                df_09 = pd.read_excel('data/tulospalvelu_gantt.xlsx')
                tasksa = df_09['Tehtävä']
                starta = df_09['Alkaa']
                finisha = df_09['Loppunut']
                completea = df_09['Valmistuminen']
                statusa = df_09['State']
                colorsa = {'Voitto': '#2ca02c', 'Häviö': '#d62728', 'Tasapeli': 'yellow', 'Ei aloitettu': 'lightgrey'}
                fig_10 = px.timeline(
                    df_09, x_start=starta[0:5], x_end=finisha[0:5], y=tasksa[0:5], color=statusa[0:5],
                    color_discrete_map=colorsa)
                fig_10.add_shape(
                    type='line', x0='2021-05-01', y0=-0.5, x1='2021-05-01', y1='Aktiivinen kehitysvaihe',
                    line=dict(color='#4f6994', width=1.25, dash="dot"))
                fig_10.update_yaxes(autorange='reversed')
                fig_10.update_layout(
                    font_size=18, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                    xaxis_showgrid=False, yaxis_showgrid=False, showlegend=False)
                st.plotly_chart(fig_10, use_container_width=True)

            row15_space1, row15_1, row15_space2 = st.beta_columns([0.75, 3, 0.5])
            with row15_1:
                st.title(
                    "Johdonmukaisesti käytettävä tulospalvelu")
                st.header(
                    "Tulospalvelun käyttö on helppoa ja se täyttää ne tarpeet, joita eri käyttäjäryhmillä on")

            row16_space1, row16_1, row16_2, row16_space2 = st.beta_columns([0.1, 1, 1, 0.1])
            with row16_1:
                df_03 = pd.read_excel('data/mittarit1.xlsx')
                count = df_03['Count']
                year = df_03['Year']
                fig_04 = go.Figure()
                fig_04.add_trace(
                    go.Scatter(x=year, y=count, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[4, 4], fill='tozeroy', mode='none', fillcolor='rgba(255, 0, 0, 0.2)'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[4.9, 4.9], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_04.add_trace(
                    go.Scatter(x=[2021, 2024], y=[5, 5], fill='tonexty', mode='none', fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_04.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_04.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_04.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_04.add_annotation(
                    x=year[5], y=5.1, text="Max. (5.0)", showarrow=False, arrowhead=0)
                fig_04.add_annotation(
                    x=year[5], y=4.75, text="Tavoite (4.9)", showarrow=False, arrowhead=0)
                fig_04.update_layout(
                    title="Tulospalvelu: <br>Käyttäjäkokemukset", title_font_color="#4f6994", title_font_size=22,
                    showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_04, use_container_width=True)

            with row16_2:
                df_04 = pd.read_excel('data/mittarit2.xlsx')
                month = df_04['Month']
                percent = df_04['Percentage']
                fig_05 = go.Figure()
                fig_05.add_trace(
                    go.Scatter(x=month, y=percent, line=dict(color='#4f6994', width=1.25), mode='markers+lines'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[99, 99], mode='lines', line_color='rgba(255, 0, 0, 0.2)'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[99.5, 99.5], fill='tonexty', mode='none',
                               fillcolor='rgba(255, 255, 0, 0.2)'))
                fig_05.add_trace(
                    go.Scatter(x=[month[0], month[22]], y=[100, 100], fill='tonexty', mode='none',
                               fillcolor='rgba(0, 128, 0, 0.2)'))
                fig_05.update_traces(
                    marker=dict(size=20, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
                fig_05.update_xaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_05.update_yaxes(
                    showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
                fig_05.add_annotation(
                    x=month[0], y=100.035, text="Max. (100%)", showarrow=False, arrowhead=0)
                fig_05.add_annotation(
                    x=month[0], y=98.95, text="Tavoite (99%)", showarrow=False, arrowhead=0)
                fig_05.update_layout(
                    title="Tulospalvelu: <br>Käytettävissä", title_font_color="#4f6994", title_font_size=22,
                    showlegend=False, font_size=12, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_05, use_container_width=True)

# Process State Monitoring Section
elif session_state.page_number == 2:
    row17_1, row17_space2, row17_2 = st.beta_columns([3, 3, 0.5])
    with row17_1:
        st.markdown(
            "<h1 style='text-align: center;font-family:sans-serif;'>Mittarit</h1>",
            unsafe_allow_html=True)
    with row17_2:
        st.image(
            "images/spl_logo.png", width=25)

    row18_space1, row18_1, row18_space2 = st.beta_columns([0.1, 1, 0.2])
    with row18_1:
        st.image(
            "images/psm.png", width=1200)

    row19_space1, row19_1, row19_space2 = st.beta_columns([2.1, 1, 2])
    with row19_1:
        st.markdown(
            "<h1 style='text-align: center;font-family:sans-serif;'>Valitse Pääprosessi</h1>",
            unsafe_allow_html=True)

    row20_space1, row20_1, row20_space2 = st.beta_columns([2, 1, 2])
    with row20_1:
        choice4 = st.selectbox("", menu3)

    if choice4 == '---':
        st.write("")

    elif choice4 == 'Pelaajakehitys':
        row21_1, row21_space1, row21_space2 = st.beta_columns([4, 0.1, 0.5])
        with row21_1:
            st.markdown(
                "<h1 style='text-align: left;font-family:sans-serif;'>Pelaajakehitys</h1><p>&nbsp;</p>",
                unsafe_allow_html=True)

        row22_space1, row22_1, row22_2, row22_space2 = st.beta_columns([0.1, 2, 2, 0.1])
        with row22_1:
            df_10 = pd.read_excel('data/rankings_men.xlsx')
            rank = df_10['Ranking']
            year4 = df_10['Year']
            fig_11 = go.Figure()
            fig_11.add_trace(
                go.Scatter(x=year4, y=rank, line=dict(color='#4f6994', width=1.5), mode='markers+lines'))
            fig_11.add_trace(
                go.Scatter(x=[1992, 2020], y=[57, 57], fill='tozeroy', mode='none',
                           fillcolor='rgba(255, 255, 0, 0.15)'))
            fig_11.add_trace(
                go.Scatter(x=[1992, 2020], y=[54, 54], fill='tozeroy', mode='none', fillcolor='rgba(0, 128, 0, 0.3)'))
            fig_11.update_traces(marker=dict(size=50, line=dict(width=2, color='#4f6994')),
                                 selector=dict(mode='markers'))
            fig_11.update_traces(
                hovertemplate='FIFA rank: %{y} <br>Year: %{x}<extra></extra>')
            fig_11.add_annotation(
                x=1992.5, y=30, text="Voitto", showarrow=False, arrowhead=0)
            fig_11.add_annotation(
                x=1992.70, y=55, text="Tasapeli", showarrow=False, arrowhead=0)
            fig_11.add_annotation(
                x=1994, y=-1.1, text="Belgium FIFA rank (#1)", showarrow=False, arrowhead=0)
            fig_11.update_layout(
                title="A-maajoukkueen rankingsijoitus - Miehet (1992-2020)", title_font_size=20,
                title_font_color="#4f6994", font_size=12, title_font_family='Arial', paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', xaxis_showgrid=False, yaxis_showgrid=False, showlegend=False,
                xaxis=dict(title="Year", tickmode='linear', tick0=1990, dtick=2, color='#4f6994'),
                yaxis=dict(title="FIFA rank", tickmode='linear', tick0=100, dtick=5, color='#4f6994'))
            fig_11.update_yaxes(autorange='reversed')
            fig_11.update_xaxes(
                showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False,
                title_font=dict(size=18, family='Arial', color='#4f6994'))
            fig_11.update_yaxes(
                showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False,
                title_font=dict(size=18, family='Arial', color='#4f6994'))
            st.plotly_chart(fig_11, use_container_width=True)

        with row22_2:
            df_11 = pd.read_excel('data/rankings_women.xlsx')
            rank2 = df_11['Ranking']
            year5 = df_11['Year']
            fig_12 = go.Figure()
            fig_12.add_trace(
                go.Scatter(x=year5, y=rank2, line=dict(color='#4f6994', width=1.5), mode='markers+lines'))
            fig_12.add_trace(
                go.Scatter(x=[2003, 2020], y=[27, 27], fill='tozeroy', mode='none',
                           fillcolor='rgba(255, 255, 0, 0.15)'))
            fig_12.add_trace(
                go.Scatter(x=[2003, 2020], y=[20, 20], fill='tozeroy', mode='none', fillcolor='rgba(0, 128, 0, 0.3)'))
            fig_12.update_traces(
                marker=dict(size=50, line=dict(width=2, color='#4f6994')), selector=dict(mode='markers'))
            fig_12.update_traces(
                hovertemplate='FIFA rank: %{y} <br>Year: %{x}<extra></extra>')
            fig_12.add_annotation(
                x=2003.25, y=18, text="Voitto", showarrow=False, arrowhead=0)
            fig_12.add_annotation(
                x=2003.35, y=26.5, text="Tasapeli", showarrow=False, arrowhead=0)
            fig_12.add_annotation(
                x=2003.7, y=0.15, text="USA FIFA rank (#1)", showarrow=False, arrowhead=0)
            fig_12.update_layout(
                title="A-maajoukkueen rankingsijoitus - Naiset (2003-2020)", title_font_size=20,
                title_font_color="#4f6994", font_size=12, title_font_family='Arial', paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)', xaxis_showgrid=False, yaxis_showgrid=False, showlegend=False,
                xaxis=dict(title="Year", tickmode='linear', tick0=2000, dtick=2, color='#4f6994'),
                yaxis=dict(title="FIFA rank", tickmode='linear', tick0=100, dtick=2, color='#4f6994'))
            fig_12.update_yaxes(autorange='reversed')
            fig_12.update_xaxes(
                showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False,
                title_font=dict(size=18, family='Arial', color='#4f6994'))
            fig_12.update_yaxes(
                showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False,
                title_font=dict(size=18, family='Arial', color='#4f6994'))
            st.plotly_chart(fig_12, use_container_width=True)

        st.markdown("""
        -------------------------------------------------------------------------------------------
        """)
