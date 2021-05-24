# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:30:14 2021

@author: raju1g
"""
import streamlit as st
import header as he
import utils
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import openpyxl


spm_menu = ["---", "Projekti 1 - Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä",
         "Projekti 2", "Projekti 3", "Projekti 4", "Projekti 5"]
tavoitteet_menu = ["---", "Tulospalvelu", "Pelipaikka", "Nettisivut"]


#res = excel_cleaner(table_1='strategic_project_monitoring.tehtavat', table_2='strategic_project_monitoring.tehtavat_paivitykset', table_3='strategic_project_monitoring.valitavoitteet', table_4='strategic_project_monitoring.valitavoitteet_paivitykset', table_5='strategic_project_monitoring.poistetut')
#tehtavat_df = res.tehtavatcsv
#tehtavat_paivitykset_df = res.tehtavat_paivitykset

#summary_table_df = res.summary_table


def main(session_state):
    utils.localCSS("style_new2.css")
    he.genHeader("1")
    st.sidebar.markdown(
        "<h2 style='text-align: center; color: #022B7E; font-family:sans-serif;'>Valitse <br> strategiaprojekti</h2>",
        unsafe_allow_html=True,
    )
    choice = st.sidebar.selectbox("", spm_menu)
    st.write(
        f"""
        <div class="base-wrapper" style="background-color:#224B90;">
            <div class="hero-wrapper">
                <div class="hero-container" style="width:100%;">
                    <div class="hero-container-content">
                        <span class="subpages-container-product white-span">Strategiaprojektit</span>
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

    row1_1, row1_2, row1_3, row1_4, row1_5 = st.beta_columns([1, 1, 1, 1, 1])

    with row1_1:
        x_01 = ['']
        fig_01 = go.Figure(
            go.Bar(x=x_01, y=[1], name='Voitto', texttemplate="<b>%{y}</b>",
                   hovertemplate="<b>1. Tulospalvelu: Käytettävissä</b><br>",
                   textposition="inside", textangle=0,
                   textfont_color="white", marker_color='#2ca02c'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[1], name='Häviö', texttemplate="<b>%{y}</b>",
                   hovertemplate="<b>1. Nettisivut: Kävijämäärät</b><br>",
                   textposition="inside", textangle=0,
                   textfont_color="white", marker_color='#d62728'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[1], name='Tasapeli', texttemplate="<b>%{y}</b>",
                   hovertemplate="<b>1. Tulospalvelu: Käyttäjäkokemukset</b><br>",
                   textposition="inside", textangle=0,
                   textfont_color="#4f6994", marker_color='yellow'))
        fig_01.add_trace(
            go.Bar(x=x_01, y=[5], name='Kesken',
                   texttemplate="<b>%{y}</b>",
                   hovertemplate="<b>1. Pelipaikka: Seurojen <br>tyytyväisyys Pelipaikan <br>käyttöön<br><br> "
                                 "2. Pelipaikka: Tukipyyntöjen <br>lukumäärä suhteessa <br>rekisteröinteihin<br><br>"
                                 "3. Nettisivut: Tyytyväisyys <br>nettisivuihin<br><br>"
                                 "4. Tulospalvelu: Käytettävissä<br><br>"
                                 "5. Nettisivut: Kävijämäärät</b>",
                   textposition="inside", textangle=0,
                   textfont_color="#4f6994", marker_color='lightgrey'))
        fig_01.update_xaxes(
            showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False)
        fig_01.update_yaxes(
            showline=False, linewidth=0.25, linecolor='#4f6994', mirror=False, title='y', visible=False,
            showticklabels=False)
        fig_01.update_layout(
            barmode='stack', xaxis={'categoryorder': 'total descending'}, showlegend=False,
            uniformtext=dict(mode="hide", minsize=8), title_font_size=42, font_size=18, title_font_family='Arial',
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis_showgrid=False, yaxis_showgrid=False,
            hoverlabel_align='left', width=50, autosize=True,
        )
        st.plotly_chart(fig_01, use_container_width=True)

        df_01 = pd.read_excel('data/state_of_tasks.xlsx')
        fig_02 = px.sunburst(
            df_01,
            path=["Overall", "Tasks", "Objectives"],
            color="State",
            color_discrete_map={'(?)': 'grey', 'Voitto': '#2ca02c', 'Hävi': '#d62728',
                                'Tasapeli': 'yellow', 'Ei aloitettu': 'lightgrey'},
            hover_name=df_01['Kommentti']
        )
        fig_02.update_traces(
            go.Sunburst(hovertemplate="<b>%{hovertext}</b><br>" + "%{id}"),
            insidetextorientation='radial',
        )
        fig_02.update_layout(margin=dict(t=10, l=10, r=10, b=10))
        fig_02.update_layout(width=300, height=300, showlegend=False, font_size=8)
        st.plotly_chart(fig_02, use_container_width=True)
        st.write("""      
                <div class = "info">
                               <a href="#entenda-mais" class="info-btn;">Parannamme Palloliiton <br>perusjärjestelmien ja <br>verkkopalvelujen käytettävyyttä</a>
                               <div id="entenda-mais" class="info-modal-window">
                                   <div><a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                                       <div style="margin: 10px 15px 15px 15px;">
                                           <h1 class="primary-span">Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä</h1>
                                           <h2 class="primary-span">Toimenpiteet</h2>
                                           <div style="font-size: 14px">
                                               <p><b>Tulospalvelu<b>
                                               <li>Tulospalvelun määrittely<br>
                                               <li>Toteutusvaihe<br>
                                               <li>Testaus / korjaus<br>
                                               <li>Julkaisu<br>
                                               <li>Korjaus</p><br>
                                               <p><b>Pelipaikka<b>
                                               <li>Selvitetään pelipassin ostamiseen liittyvät haasteet<br>
                                               <li>Suunnitellaan toimenpiteitä haasteiden helpottamiseksi<br>
                                               <li>Toteutetaan toimenpiteet haasteiden helpottamiseksi<br>
                                               <li>FIFA:an vaikuttaminen<br>
                                               <li>Rajapinnan avaaminen jäsenrekisteritoimittajien kanssa<br>
                                               <li>Seuratiedotus</p><br>
                                               <p><b>Nettisivut<b>
                                               <li>Sivujen esimäärittely<br>
                                               <li>Toimittajan kilpailutus ja valinta<br>
                                               <li>Sivujen määrittely yhdessä toimintojen ja eri käyttäjäryhmien kanssa<br>
                                               <li>Sivujen tekninen toteutus<br>
                                               <li>Uusien sivujen asteittainen ylösajo</p><br>
                                                <br><br>
                                               <i>For more details select a project from the sidebar</i>.
                                           </div><br>                           
               <div class='base-wrapper product-section'>
               </div>
               """,
         unsafe_allow_html=True,
         )

    with row1_2:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
        st.write("""
               <div class = "info">
                   <a href="#entenda-mais" class="info-btn;">Lasten valmentamisen <br>ydintaitojen kehittäminen <br>seuraympäristössä</a>
                   <div id="entenda-mais" class="info-modal-window">
                       <div><a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                           <div style="margin: 10px 15px 15px 15px;">
                               <h1 class="primary-span">Lasten valmentamisen ydintaitojen kehittäminen seuraympäristössä</h1>
                               <h2 class="primary-span">Toimenpiteet</h2>
                               <div style="font-size: 14px">
                                   <i>For more details select a project from the sidebar</i>.
                               </div><br>                           
               <div class='base-wrapper product-section'>
               </div>
               """, unsafe_allow_html=True,)
    with row1_3:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
        st.write("""
               <div class = "info">
                   <a href="#entenda-mais" class="info-btn;">Kasvatamme ja ylläpidämme <br>joukkuetoiminnan pelaajamääriä</a>
                   <div id="entenda-mais" class="info-modal-window">
                       <div><a href="#" title="Close" class="info-btn-close" style="color: white;"></a>
                           <div style="margin: 10px 15px 15px 15px;">
                               <h1 class="primary-span">Kasvatamme ja ylläpidämme joukkuetoiminnan pelaajamääriä</h1>
                               <div style="font-size: 14px">
                                   <p><b>Tulospalvelu<b>
                                   <i>For more details select a project from the sidebar</i>.
                               </div><br>                           
               <div class='base-wrapper product-section'>
               </div>
               """, unsafe_allow_html=True)
    with row1_4:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
        st.write("""
                   <div class = "info">
                       <a href="#entenda-mais" class="info-btn;">Kasvatamme seuravetoista <br>harrastetoimintaa uusissa <br>kohderyhmissä</a>
                       <div id="entenda-mais" class="info-modal-window">
                           <div><a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                               <div style="margin: 10px 15px 15px 15px;">
                                   <h1 class="primary-span">Kasvatamme seuravetoista harrastetoimintaa uusissa kohderyhmissä</h1>
                                   <h2 class="primary-span">Toimenpiteet</h2>
                                   <div style="font-size: 14px">
                                       <i>For more details select a project from the sidebar</i>.
                                   </div><br>                           
       """, unsafe_allow_html=True)
    with row1_5:
        st.plotly_chart(fig_01, use_container_width=True)
        st.plotly_chart(fig_02, use_container_width=True)
        st.write("""
                       <div class = "info">
                           <a href="#entenda-mais">Kehitämme Palloliiton <br>kykyä tuottaa tietoa<br> jalkapalloyhteisön käyttöön</a>
                           <div id="entenda-mais" class="info-modal-window">
                               <div><a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                                   <div style="margin: 10px 15px 15px 15px;">
                                       <h1 class="primary-span">Kehitämme Palloliiton kykyä tuottaa tietoa jalkapalloyhteisön käyttöön</h1>
                                       <h2 class="primary-span">Toimenpiteet</h2>
                                       <div style="font-size: 14px">
                                           <i>For more details select a project from the sidebar</i>.
                                       </div><br>                           
           """, unsafe_allow_html=True)

    st.markdown("""
    -----------------------------------
    """)

    df_02 = pd.read_excel('data/tulospalvelu_gantt.xlsx')
    tasks = df_02['Tehtävä']
    start = df_02['Alkaa']
    finish = df_02['Loppunut']
    complete = df_02['Valmistuminen']
    status = df_02['State']
    comments = df_02['Kommentti']
    objs = df_02['Toivoteet']
    colors = {'Voitto': '#2ca02c', 'Häviö': '#d62728', 'Tasapeli': 'yellow', 'Ei aloitettu': 'lightgrey'}
    fig_03 = px.timeline(df_02, x_start=start, x_end=finish, y=tasks, color=status,
                         color_discrete_map=colors, text=objs)
    fig_03.add_shape(type='line', x0='2021-05-01', y0=-0.5, x1='2021-05-01',
                     y1='Aktiivinen kehitysvaihe II', line=dict(color='#4f6994', width=1.25, dash="dot"))
    fig_03.update_xaxes(showline=True, linewidth=0.25, linecolor='#4f6994', mirror=False, visible=True)
    fig_03.update_yaxes(autorange='reversed', visible=False)
    fig_03.update_yaxes(showline=True, linewidth=0.25, linecolor='#4f6994', mirror=True)
    fig_03.update_layout(font_size=16, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                         xaxis_showgrid=True, yaxis_showgrid=False, showlegend=False)
    st.plotly_chart(fig_03, use_container_width=True)

    st.write(
        """
        <div class='base-wrapper' 
            <i>* <b>Muutama periaate</b> </i>
            <li>Seurataan vain 5 tärkeintä projektia tällä tasolla<br>
            <li>Muiden projektien osalta voi olla hyödyllistä käydä läpi toimenpiteiden ja tuloksen lisäksi myös välitavoitteet, jotta tiimillä ja jorylla oin sama käsitys siitä, mitkä asiat johtavat tulokseen.<br>
            <li>Strategiaprojektien mittarit automatisoidaan, jotta mittaaminen ei kuormita projektia suorittavaa projektitiimiä.<br>
            <li>Tuloksen saavuttamisen seuraaminen vaati välitavoitteiden seuraamista, sillä monessa tapauksessa tuloksen saavuttaminen voidaan todeta vasta lopuksi.<br>
            <i>Tarkista yksittäiset projektin tavoitteet tarkemmin.</i>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if choice == '---':
        st.write("")
    elif choice == 'Projekti 1 - Parannamme Palloliiton perusjärjestelmien ja verkkopalvelujen käytettävyyttä':
        st.sidebar.markdown(
            "<h2 style='text-align: center; color: #022B7E; font-family:sans-serif;'>Valitse <br> tavoiteet</h2>",
            unsafe_allow_html=True,
        )
        choice2 = st.sidebar.selectbox("", tavoitteet_menu)

    # Write cards section

    st.write(f"""<div>
                <div class="base-wrapper flex flex-column" style="background-color:#224B90">
                    <div class="white-span header p1" style="font-size:30px;">HALUATKO TIETÄÄ LISÄÄ STRATEGIAKAUDESTA?</div>
                    <span class="white-span">Seuraa linkkiä saadaksesi lisätietoja<br><br>
                    <a class="btn-ambassador" href="https://www.palloliitto.fi/sites/default/files/Palloliitto/strategia_2020-24_2.pdf" target="_self">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Suomalaisen jalkapallo ja futsalin strategia&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
                    <br><br><span class="white-span">ja jaa WhatsAppin avulla!<br><br>
                    <a class="btn-ambassador" href="https://api.whatsapp.com/send?text=%s" target="blank">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jaa WhatsAppin kautta &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a>
            </div>""",
             unsafe_allow_html=True,
             )



