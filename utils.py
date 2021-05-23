#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:30:14 2021
@author: raju1g
"""

import streamlit as st
from streamlit.server.server import Server
from datetime import datetime
from datetime import timedelta
from typing import List, Dict
import session
from models import (
    BackgroundColor,
    Logo,
    Link,
    Indicator,
    AlertBackground,
    IndicatorBackground,
    Illustration,
    Dimension,
)
from typing import List
import re
import numpy as np
import math
import pandas as pd
import os

import collections
import functools
import inspect
import textwrap
#import yaml
import random
#from ua_parser import user_agent_parser
import time
#import loader
import base64
from pathlib import Path
import base64
from io import BytesIO
from pathlib import Path

#config = yaml.load(open("configs/config.yaml", "r"), Loader=yaml.FullLoader)

# DATASOURCE TOOLS


def get_server_session():
    return session._get_session_raw()


def hash_code(size=16):
    return "".join(
        random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuv")
        for i in range(size)
    )


def give_cookies(cookie_name, cookie_info, cookie_days=99999, rerun=False):
    """ Gives the user a browser cookie """
    # Cookie days is how long in days will the cookie last
    st.write(
        f"""<iframe src="resources/cookiegen.html?cookie_name={cookie_name}&cookie_value={cookie_info}&cookies_days={cookie_days}" height="0" width="0" style="border: 1px solid black; float: right;"></iframe>""",
        unsafe_allow_html=True,
    )
    if rerun:
        time.sleep(1)
        reload_window()
        # session.rerun()


def update_user_public_info():
    """ updates the user's public data for us like his ip address and geographical location """
    st.write(
        f"""
        <iframe src="resources/cookiegen.html?load_user_data=true" height="0" width="0" style="border: none; float: right;"></iframe>""",
        unsafe_allow_html=True,
    )


def local_css(file_name):
    """
        This function will add css file to streamlit app.
        Write html-code to streamlit app.

        Parameters
        ----------
        file_name : string
            Path to file.

        Returns
        -------
        None.
    """
    with open(file_name) as file:
        st.markdown(
            f'<style type="text/css">{file.read()}</style>',
            unsafe_allow_html=True
        )


def image_to_bytes(img_path, html=1):
    """
        This function makes PNG image to bytes, which we can show on HTML page

        Parameters
        ----------
        img_path : String
            Path to the image file which you want to show.

        Returns
        -------
        image_html : String
            HTML code which includes the image in base64 format.
        """

    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    if html == 1:
        image_html = "<img src='data:image/png;base64,{}' style='display: block; text-align: center; width: 2em; margin: 5em auto;' />".format(
            encoded)
    else:
        image_html = f"data:image/png;base64,{encoded}"

    return image_html


def reload_window():
    """ Reloads the user's entire browser window """
    st.write(
        f"""
        <iframe src="resources/window_reload.html?load_user_data=true" height="0" width="0" style="border: none; float: right;"></iframe>""",
        unsafe_allow_html=True,
    )
    time.sleep(1)


# JAVASCRIPT / CSS HACK METHODS

def load_image(path):
    return base64.b64encode(Path(str(os.getcwd()) + "/" + path).read_bytes()).decode()


def stylizeButton(name, style_string, session_state, others=dict()):
    """ adds a css option to a button you made """
    session_state.button_styles[name] = [style_string, others]


def applyButtonStyles(session_state):
    """ Use it at the end of the program to apply styles to buttons as defined by the function above """
    time.sleep(0.1)
    html = ""
    for name, style in session_state.button_styles.items():
        parts = (
            style[0]
            .replace("\n", "")
            .replace("    ", "")
            .replace("; ", "&")
            .replace(";", "&")
            .replace(":", "=")
        )
        other_args = "&".join(
            [str(key) + "=" + str(value) for key, value in style[1].items()]
        )
        html += f"""
        <iframe src="resources/redo-button.html?name={name}&{parts}&{other_args}" style="height:0px;width:0px;">
        </iframe>"""
    st.write(html, unsafe_allow_html=True)


def get_radio_horizontalization_html(radio_label):
    """ Takes a normal radio and restilizes it to make it horizontal and bigger"""
    html = f"""<iframe src="resources/horizontalize-radio.html?radioText={radio_label}" style="height:0px;width:0px;"></iframe>"""
    return html


def hide_iframes():
    st.write(
        f"""<iframe src="resources/hide-iframes.html" height = 0 width = 0></iframe>""",
        unsafe_allow_html=True,
    )


def gen_pdf_report():
    st.write(
        """
    <iframe src="resources/ctrlp.html" height="100" width="350" style="border:none; float: right;"></iframe>
    """,
        unsafe_allow_html=True,
    )


def make_clickable(text, link):
    # target _blank to open new window
    # extract clickable text to display for your link
    return f'<a target="_blank" href="{link}">{text}</a>'


def localCSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def gen_whatsapp_button(info) -> None:
    """Generate WPP button

    Args:
        info: config["contact"]
    """
    url = "https://api.whatsapp.com/send?text={}&phone=${}".format(info["msg"], info["phone"])
    st.write(
        """ 
         <a href="%s" class="float" target="_blank" id="messenger">
                <i class="material-icons">?</i>
                <p class="float-header">Doubts?</p></a>
        """
        % url,
        unsafe_allow_html=True,
    )

def gen_reference_table(config):

    situation_classification = config["br"]["farolcovid"]["rules"][
        "situation_classification"
    ]["cuts"]
    control_classification = config["br"]["farolcovid"]["rules"][
        "control_classification"
    ]["cuts"]
    capacity_classification = config["br"]["farolcovid"]["rules"][
        "capacity_classification"
    ]["cuts"]
    trust_classification = config["br"]["farolcovid"]["rules"]["trust_classification"][
        "cuts"
    ]

    date_update = config["br"]["farolcovid"]["date_update"]

    # TODO -> VOLTAR PARA PROJECAO DE LEITOS
    # <td><span>Capacidade de respostas do sistema de saúde</span></td>
    # <td><span>Projeção de tempo para ocupação total de leitos UTI</span></td>
    # <td class="light-blue-bg bold">{capacity_classification[3]} - 90 dias</td>
    # <td class="light-yellow-bg bold"><span>{capacity_classification[2]} - {capacity_classification[3]} dias</span></td>
    # <td class="light-orange-bg bold"><span>{capacity_classification[1]} - {capacity_classification[2]} dias</span></td>
    # <td class="light-red-bg bold"><span>{capacity_classification[0]} - {capacity_classification[1]} dias</span></td>
    return f"""<div style="font-size: 12px">
        <b>Atualizado em</b>: {date_update}<br>
    </div>
    <div class="info-div-table">
        <table class="info-table">
        <tbody>
            <tr>
                <td class="grey-bg"><strong>Dimensão</strong></td>
                <td class="grey-bg"><strong>Indicador</strong></td>
                <td class="grey-bg"><strong>Novo Normal</strong></td>
                <td class="grey-bg"><strong>Risco Moderado</strong></td>
                <td class="grey-bg"><strong>Risco Alto</strong></td>
                <td class="grey-bg"><strong>Risco Altíssimo</strong></td>
            </tr>
            <tr>
                <td rowspan="2">
                <p><span>Situação da doença</span></p><br/>
                </td>
                <td><span>Novos casos diários por 100mil hab.(Média móvel 7 dias)</span></td>
                <td class="light-blue-bg bold"><span>x&lt;={situation_classification[1]}</span></td>
                <td class="light-yellow-bg bold"><span>{situation_classification[1]}&lt;x&lt;={situation_classification[2]}</span></td>
                <td class="light-orange-bg bold"><span>{situation_classification[2]}&lt;=x&lt;={situation_classification[3]}</span></td>
                <td class="light-red-bg bold"><span>x &gt;= {situation_classification[3]} </span></td>
            </tr>
            <tr>
                <td><span>Tendência de novos casos diários</span></td>
                <td class="lightgrey-bg" colspan="4"><span>Se crescendo*, mover para o nível mais alto</span></td>
            </tr>
            <tr>
                <td><span>Controle da doença</span></td>
                <td><span>Número de reprodução efetiva</span></td>
                <td class="light-blue-bg bold"><span>&lt;{control_classification[1]}</span></td>
                <td class="light-yellow-bg bold"><span>&lt;{control_classification[1]} - {control_classification[2]}&gt;</span></td>
                <td class="light-orange-bg bold"><span>&lt;{control_classification[2]} - {control_classification[3]}&gt;</span>&nbsp;</td>
                <td class="light-red-bg bold"><span>&gt;{control_classification[3]}</span></td>
            </tr>
            <tr>
                <td><span>Capacidade de respostas do sistema de saúde <i>(alterado em 18/12/2020)</i></span></td>
                <td><span>Total de leitos UTI por 100 mil hab.</span></td>
                <td class="light-blue-bg bold"> > {capacity_classification[3]}</td>
                <td class="light-yellow-bg bold"><span>{capacity_classification[2]} - {capacity_classification[3]}</span></td>
                <td class="light-orange-bg bold"><span>{capacity_classification[1]} - {capacity_classification[2]}</span></td>
                <td class="light-red-bg bold"><span>{capacity_classification[0]} - {capacity_classification[1]}</span></td>
            </tr>
            <tr>
                <td><span>Confiança dos dados</span></td>
                <td><span>Subnotificação (casos <b>não</b> diagnosticados a cada 10 infectados)</span></td>
                <td class="light-blue-bg bold"><span>{int(trust_classification[0]*10)}&lt;=x&lt;{int(trust_classification[1]*10)}</span></td>
                <td class="light-yellow-bg bold"><span>{int(trust_classification[1]*10)}&lt;=x&lt;{int(trust_classification[2]*10)}</span></td>
                <td class="light-orange-bg bold"><span>{int(trust_classification[2]*10)}&lt;=x&lt;{int(trust_classification[3]*10)}</span></td>
                <td class="light-red-bg bold"><span>{int(trust_classification[3]*10)}&lt;=x&lt;=10</span></td>
            </tr>
        </tbody>
        </table>
    </div>
    <div style="font-size: 12px">
        * Como determinamos a tendência:
        <ul class="sub"> 
            <li> Crescendo: caso o aumento de novos casos esteja acontecendo por pelo menos 5 dias. </li>
            <li> Descrescendo: caso a diminuição de novos casos esteja acontecendo por pelo menos 14 dias. </li>
            <li> Estabilizando: qualquer outra mudança. </li>
        </ul>
    </div>
    """

# VIEW COMPONENTS FAROLCOVID

def genHeroSection(title1: str, title2: str, subtitle: str, logo: str, header: bool, explain: bool = False):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-bold">corona</span><span class="logo-lighter">cidades</span></a>"""
    else:
        header = """<br>"""

    # TODO -> VOLTAR PARA PROJECAO DE LEITOS
    # - <b>Capacidade do sistema</b>: tempo para ocupação de leitos UTI</br>
    if explain:
        explain = f"""<div class="hero-container-content">
            <div>
                <a href="#novidades" class="info-btn">Como navegar</a>
            </div>
            <div id="novidades" class="nov-modal-window">
                <div>
                    <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                    <div style="margin: 10px 15px 15px 15px;">
                        <h1 class="primary-span">Saiba como cada ferramenta apoia a resposta ao coronavírus</h1>
                        <p class="darkblue-span uppercase"> <b>Farol Covid</b> </p>
                        <div>
                            <p> <b>Importante: mudamos a metodologia dos indicadores - veja mais em Modelos, limitações e fontes no menu lateral.</b> Descubra o nível de alerta do estado, regional de saúde ou município de acordo com os indicadores:</p>
                            - <b>Situação da doença</b>: média de novos casos 100 mil por habitantes;</br>
                            - <b>Controle da doença</b>: taxa de contágio</br>
                            - <b>Capacidade do sistema</b>: total de leitos UTI por 100 mil hab. (CNES)</br>
                            - <b>Confiança de dados</b>: taxa de subnotificação de casos</br><br>
                        </div>
                        <div>
                        <p class="darkblue-span uppercase"> <b>SimulaCovid</b> </p>
                        <p style="height:100px;">Simule o que pode acontecer com o sistema de saúde local se o ritmo de contágio aumentar 
                            ou diminuir e planeje suas ações para evitar a sobrecarga hospitalar.</p>
                        </div>
                        <div>
                        <p class="darkblue-span uppercase"> <b>Distanciamento Social</b> </p>
                            <p style="height:100px;">Acompanhe a atualização diária do índice e descubra como está a circulação de pessoas 
                                e o distanciamento social no seu estado ou município.    
                            </p>
                        </div>
                        <div>
                        <p class="darkblue-span uppercase"> <b>Saúde em Ordem</b> </p>
                        <p> Entenda quais atividades deveriam reabrir primeiro no seu estado ou regional, considerando:
                            - <b>Segurança Sanitária</b>: quais setores têm menor exposição à Covid-19?</br>
                            - <b>Contribuição Econômica</b>: quais setores movimentam mais a economia local?</br></p>
                        <p> </p>
                        </div>
                        <div>
                        <p class="darkblue-span uppercase"> <b>Onda Covid</b> </p>
                        <p>Com base no número de óbitos de Covid-19 registrados, acompanhe se seu município já saiu do pico da doença. </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
    else:
        explain = ""

    st.write(
        f"""
        <div class="base-wrapper hero-bg">
            <div class="hero-wrapper">
                <div class="hero-container">
                    {header}
                    <div class="hero-container-content">
                        <span class="hero-container-product primary-span">{title1}<br/>{title2}</span>
                        <span class="hero-container-subtitle primary-span">{subtitle}</span>
                    </div>
                </div>
                <div class="hero-container-image">   
                    <img style="width: 100%;" src={logo}/>
                </div>
            </div><br>
            {explain}
        </div>
        """,
        unsafe_allow_html=True,
    )


def genInputFields(user_input, config, session):

    # # Inicia sem update
    # session.update = False

    authors_beds = user_input["author_number_beds"]
    beds_update = user_input["last_updated_number_beds"]

    authors_icu_beds = user_input["author_number_icu_beds"]
    icu_beds_update = user_input["last_updated_number_icu_beds"]

    print("\nSESSION_STATE:", session.number_beds, session.number_icu_beds)

    if session.reset or session.number_beds == None:
        number_beds = int(
            user_input["number_beds"]
            * config["br"]["simulacovid"]["resources_available_proportion"]
        )
        number_icu_beds = int(
            user_input["number_icu_beds"]
            * config["br"]["simulacovid"]["resources_available_proportion"]
        )
        number_cases = int(user_input["population_params"]["I_confirmed"])
        number_deaths = int(user_input["population_params"]["D"])
        session.reset = False
    else:
        number_beds = int(session.number_beds)
        number_icu_beds = int(session.number_icu_beds)
        number_cases = int(session.number_cases)
        number_deaths = int(session.number_deaths)

    cases_update = pd.to_datetime(user_input["last_updated_cases"]).strftime("%d/%m")

    locality = user_input["locality"]

    if locality == "Brasil":
        authors_beds = "SUS e Embaixadores"
        authors_icu_beds = "SUS e Embaixadores"

    user_input["number_beds"] = st.number_input(
        f"Número de leitos destinados aos pacientes com Covid-19 (50% do reportado em {authors_beds}; atualizado: {beds_update})",
        0,
        None,
        number_beds,
    )

    user_input["number_icu_beds"] = st.number_input(
        f"Número de leitos UTI destinados aos pacientes com Covid-19 (100% do reportado em {authors_icu_beds}; atualizado: {icu_beds_update}):",
        0,
        None,
        number_icu_beds,
    )

    user_input["population_params"]["I_confirmed"] = st.number_input(
        f"Casos confirmados (fonte: Brasil.IO; atualizado: {cases_update}):",
        0,
        None,
        number_cases,
    )

    user_input["population_params"]["D"] = st.number_input(
        f"Mortes confirmadas (fonte: Brasil.IO; atualizado: {cases_update}):",
        0,
        None,
        number_deaths,
    )

    # Faz o update quando clica o botão
    if st.button("Finalizar alteração"):

        print("FINALIZADO:", user_input)

        session.number_beds = int(user_input["number_beds"])
        session.number_icu_beds = int(user_input["number_icu_beds"])
        session.number_cases = int(user_input["population_params"]["I_confirmed"])
        session.number_deaths = int(user_input["population_params"]["D"])

        session.update = True
    else:
        session.update = False

    if st.button("Resetar aos valores oficais"):
        session.reset = True

    # Estiliza botão
    alteration_button_style = """border: 1px solid var(--main-white);box-sizing: border-box;border-radius: 15px; width: auto;padding: 0.5em;text-transform: uppercase;font-family: var(--main-header-font-family);color: var(--main-white);background-color: var(--main-primary);font-weight: bold;text-align: center;text-decoration: none;font-size: 14px;animation-name: fadein;animation-duration: 3s;margin-top: 1em;"""
    reset_button_style = """position:absolute;right:3em;top:-68px;border: 1px solid var(--main-white);box-sizing: border-box;border-radius: 15px; width: auto;padding: 0.5em;text-transform: uppercase;font-family: var(--main-header-font-family);color: var(--main-white);background-color: rgb(160,170,178);font-weight: bold;text-align: center;text-decoration: none;font-size: 14px;animation-name: fadein;animation-duration: 3s;margin-top: 1em;"""
    stylizeButton(
        "Finalizar alteração", alteration_button_style, session,
    )
    stylizeButton(
        "Resetar aos valores oficais", reset_button_style, session,
    )
    return user_input, session


def genAnalysisDimmensionsCard(dimension: Dimension):
    return f"""<div style="margin-top: 0px; display: inline-block; top:0x;">
            <div class="dimension-card primary-span style="top:0x; padding-left: 24px; padding-top: 24px; padding-right: 24px;">
                {dimension.text}
            </div>
        </div>"""


def genAnalysisDimmensionsSection(dimensions: List[Dimension]):
    cards = list(map(genAnalysisDimmensionsCard, dimensions))
    cards = "".join(cards)

    st.write(
        f"""<div class="container">
        <div class="base-wrapper primary-span">
            <div>
                <span class="section-header">DIMENSÕES DA ANÁLISE</span>
            </div>
            <span class="p3">O que olhamos ao avaliar o cenário da pandemia em um lugar?</span>
            <div class="flex flex-row mt flex-m-column" style="margin-bottom: 0px;height:auto; display:inline-block top:0x;">
            {cards}
            </div>
        </div>
        </div>""",
        unsafe_allow_html=True,
    )


def genIndicatorCard(indicator: Indicator, place_type: str, rt_type: str = "nan"):
    if indicator.display == "None":
        indicator.display = ""
        indicator.unit = ""
    # Get name of alert by number
    if indicator.risk == "nan":
        alert = ""
    if indicator.header == "VACINAÇÃO":
        if place_type == "state_num_id":
            indicator.perc_vacinados = indicator.perc_vacinados*2
            indicator.perc_imunizados = indicator.perc_imunizados*2
            indicator.nao_vacinados = int(indicator.nao_vacinados/2)
            caption = "A porcentagem da população vacinada em seu <b>estado</b>, é"
        if place_type == "health_region_id":
            indicator.perc_vacinados = indicator.perc_vacinados*2
            indicator.perc_imunizados = indicator.perc_imunizados*2
            indicator.nao_vacinados = int(indicator.nao_vacinados/2)
            caption = "A porcentagem da população vacinada em sua <b>regional de saúde</b>, é"
        if place_type == "city_id":
            caption = "A porcentagem da população vacinada em seu <b>município</b>, é"
        return f"""
        <div id="vacina" class="main-indicator-card flex flex-column mr" style="z-index:1;display:inline-block;position:relative;background:#fafafa;border:4px solid #0097A7;">
            <span class="main-card-header-v2" >{indicator.header}</span>
            <span class="main-card-list-v2">{caption}</span>
            <div class="flex flex-row flex-justify-space-between mt" style="width:250px;">
            </div>
            <span class="bold p2 main-card-display-value">{indicator.perc_vacinados}<span class="p5">{indicator.unit}</span></span>
            <div class="main-card-display-text-v2 sdcardtext-left">
                    <span class="lighter">{indicator.left_label}<br></span>
                    <span class="bold">{indicator.perc_imunizados} %</span>
            </div>
            <div class="main-card-display-text-v2 sdcardtext-right">
                    <span class="lighter">{indicator.right_label}<br></span>
                    <span class="bold">{indicator.nao_vacinados}</span>
            </div>
            <div class="last-updated-text">Atualizado em: {indicator.last_updated}</div>
        </div>"""
    else:
        None
#        alert = loader.config["br"]["farolcovid"]["categories"][int(indicator.risk)]

    if indicator.right_display == "estabilizando":
        indicator_right_display = "estabilizando em " + alert
    else:
        indicator_right_display = indicator.right_display

    # TODO -> VOLTAR PARA PROJECAO DE LEITOS
    # "CAPACIDADE DO SISTEMA": "Se nada mudar, a capacidade hospitalar de seu <b>...</b> será atingida em",
    captions_by_place = {
        "state_num_id": {
            "VACINAÇÃO": "A porcentagem da populacão vacinada em seu <b>estado</b>, é",
            "SITUAÇÃO DA DOENÇA": "Hoje em seu <b>estado</b> são <b>reportados</b> em média",
            "CONTROLE DA DOENÇA": "Não há dados abertos sistematizados de testes ou rastreamento de contatos no Brasil. Logo, <b>classificamos pela estimativas de Rt de seu estado.</b>",
            "CAPACIDADE DO SISTEMA": "Com base nos dados do DataSUS, hoje em seu <b>estado</b> existem *",
            "CONFIANÇA DOS DADOS": "A cada 10 pessoas infectadas em seu <b>estado</b>,",
        },
        "health_region_id": {
            "VACINAÇÃO": "A porcentagem da populacão vacinada em sua <b>regional de saúde</b>, é",
            "SITUAÇÃO DA DOENÇA": "Hoje em sua <b>regional de saúde</b> são <b>reportados</b> em média",
            "CONTROLE DA DOENÇA": "Não há dados abertos sistematizados de testes ou rastreamento de contatos no Brasil. Logo, <b>classificamos pela estimativas de Rt de sua regional.</b>",
            "CAPACIDADE DO SISTEMA": "Com base nos dados do DataSUS, hoje em sua <b>regional de saúde</b> existem *",
            "CONFIANÇA DOS DADOS": "A cada 10 pessoas infectadas em sua <b>regional de saúde</b>,",
        },
        "city_id": {
            "VACINAÇÃO": "A porcentagem da populacão vacinada em seu <b>município</b>, é",
            "SITUAÇÃO DA DOENÇA": "Hoje em seu <b>município</b> são <b>reportados</b> em média",
            "CONTROLE DA DOENÇA": {
                "health_region_id": "Não há dados abertos sistematizados de testes ou rastreamento de contatos no Brasil. Logo, <b>classificamos pela estimativas de Rt de sua regional.</b>",
                "city_id": "Não há dados abertos sistematizados de testes ou rastreamento de contatos no Brasil. Logo, <b>usamos estimativas de Rt de seu município para classificação.</b>",
            },
            "CAPACIDADE DO SISTEMA": "Com base nos dados do DataSUS, hoje em sua <b>regional de saúde</b> existem *",
            "CONFIANÇA DOS DADOS": "A cada 10 pessoas infectadas em sua <b>regional de saúde</b>,",
        },
    }

    if place_type == "city_id" and indicator.header == "CONTROLE DA DOENÇA":
        indicator.caption = captions_by_place[place_type][indicator.header][rt_type]
    else:
        indicator.caption = captions_by_place[place_type][indicator.header]

    return f"""
    <div class="main-indicator-card flex flex-column mr" style="background-color: white;z-index:1;display:inline-block;position:relative;">
        <span class="main-card-header-v2">{indicator.header}</span>
        <span class="main-card-list-v2">{indicator.caption}</span>
        <div class="flex flex-row flex-justify-space-between mt" style="width:250px;">
        </div>
        <span class="bold p2 main-card-display-value">{indicator.display}<span class="p5">  {indicator.unit}</span></span>
        <div class="{IndicatorBackground(try_int(indicator.risk)).name}-alert-bg risk-pill " style="position:absolute;bottom:120px;">
            <span class="white-span p5">alerta <b>{alert}</b></span>
        </div>
        <div class="main-card-display-text-v2 sdcardtext-left">
                <span class="lighter">{indicator.left_label}<br></span>
                <span class="bold">{indicator.left_display}</span>
        </div>
        <div class="main-card-display-text-v2 sdcardtext-right">
                <span class="lighter">{indicator.right_label}<br></span>
                <span class="bold">{indicator.right_display}</span>
        </div>
        <div class="last-updated-text">Atualizado em: {indicator.last_updated}</div>
    </div>"""


def noOverallalert(user_input, data, states):
    if user_input["state_name"] in states:
        st.write(
            """
            <div>
                <div class="base-wrapper flex flex-column" style="background-color:#0090A7">
                    <div class="white-span header p1" style="font-size:30px;">⚠️ ATENÇÃO: Os municípios e regionais de saúde de {} estão desatualizados</div>
                        <span class="white-span">Utilizamos dados abertos das secretarias estaduais para os cálculos dos indicadores. 
                        Esses dados são capturados diariamente por voluntários do Brasil.io, que vêm enfrenteando problemas na atualização dos dados desses estados.
                        Estamos resolvendo a situação e iremos retornar com os indicadores o mais breve possível.</b></span>
                </div>
            <div>""".format(user_input["state_name"]),
            unsafe_allow_html=True
        )
    elif not isinstance(data["overall_alert"].values[0], str) and user_input["city_name"] != "Todos":
        st.write(
            """
            <div>
                <div class="base-wrapper flex flex-column" style="background-color:#0090A7">
                    <div class="white-span header p1" style="font-size:30px;">⚠️ ATENÇÃO: Os dados do município {} estão desatualizados.</div>
                        <span class="white-span">Utilizamos dados abertos das secretarias estaduais para os cálculos dos indicadores. 
                        Esses dados são capturados diariamente por voluntários do Brasil.io, que vêm enfrenteando problemas na atualização dos dados.
                        Estamos resolvendo a situação e iremos retornar com os indicadores o mais breve possível.</b></span>
                </div>
            <div>""".format(user_input["city_name"]),
            unsafe_allow_html=True
        )
        
def genKPISection(
    place_type: str,
    locality: str,
    alert: str,
    indicators: Dict[str, Indicator],
    n_colapse_regions: int = 0,
    rt_type: str = "nan",
):
    # Genetate cards HTML
    cards = "".join(
        [genIndicatorCard(group, place_type, rt_type) for group in indicators.values()]
    )
    # print(cards)

    # Generate subheader
    if not isinstance(alert, str):
        bg = "gray"
        alert = "Sem classificação"
        caption = "Sugerimos que confira o nível de risco de seu estado ou regional de saúde. <br/>Seu município não possui dados consistentes suficientes para calcularmos o nível de risco."
        stoplight = "%0a%0a"
    else:
        bg = AlertBackground(alert).name
        if alert == "altíssimo":
            caption = f"Nível de alerta <b>{alert.upper()}</b>: há um crescente número de casos de Covid-19 e grande parte deles não são detectados."
        elif alert == "alto":
            caption = f"Nível de alerta <b>{alert.upper()}</b>: há muitos casos de Covid-19 com transmissão comunitária. A presença de casos não detectados é provável."
        elif alert == "moderado":
            caption = f"Nível de alerta <b>{alert.upper()}</b>: há um número moderado de casos e a maioria tem uma fonte de transmissão conhecida."
        elif alert == "novo normal":
            caption = f"Nível de alerta <b>{alert.upper()}</b>: casos são raros e técnicas de rastreamento de contato e monitoramento de casos suspeitos evitam disseminação."

        if "state" in place_type:
            if n_colapse_regions > 0:
                caption = f"{caption}<br><b>Note que {n_colapse_regions} regionais de saúde avaliadas estão em Alerta Alto ou Altíssimo</b>. Sugerimos que políticas de resposta à Covid-19 sejam avaliadas a nível subestatal."
            else:
                caption = f"{caption}<br>Nenhuma regional de saúde avaliada está em Alerta Alto ou Altíssimo de colapso. Sugerimos que políticas de resposta à Covid-19 sejam avaliadas a nível subestatal."

    # TODO -> VOLTAR PARA PROJECAO DE LEITOS
    # %0a%0a🏥 *CAPACIDADE DO SISTEMA*: A capacidade hospitalar será atingida em *{str(indicators['capacity'].display).replace("+", "mais de")} dias* 
    msg = f"""🚨 *BOLETIM CoronaCidades |  {locality}, {datetime.now().strftime('%d/%m')}*  
    %0a%0a💉 *VACINAÇÃO*: Até hoje já foram vacinadas *{indicators['vacina'].perc_vacinados}* de cada 100 pessoas.
    🚨%0a%0aNÍVEL DE ALERTA: {alert.upper()}
    %0a%0a😷 *SITUAÇÃO DA DOENÇA*: Hoje são reportados❗em média *{indicators['situation'].display} casos por 100mil habitantes.
    %0a%0a *CONTROLE DA DOENÇA*: A taxa de contágio mais recente é de *{indicators['control'].left_display}* - ou seja, uma pessoa infecta em média *{indicators['control'].left_display}* outras.
    %0a%0a🏥 *CAPACIDADE DO SISTEMA*: Hoje são registrados no CNES *{str(indicators['capacity'].display)} leitos UTI por 100mil habitantes.* 
    %0a%0a🔍 *CONFIANÇA DOS DADOS*: A cada 10 pessoas infectadas, *{indicators['trust'].display} são diagnosticadas* 
    %0a%0a👉 Saiba se seu município está no nível de alerta baixo, médio ou alto acessando o *FarolCovid* aqui: https://coronacidades.org/farol-covid/"""
    # msg = "temporarily disabled"

    # Write cards section
    st.write("""
    <div class="container">
        <div class="alert-banner %s-alert-bg mb" style="margin-bottom: 0px;height:auto;">
            <div class="base-wrapper flex flex-column" style="margin-top: 0px;">
                <div class="flex flex-row flex-space-between flex-align-items-center">
                    <span class="white-span header p1">%s</span>
                    <a class="btn-wpp" href="https://api.whatsapp.com/send?text=%s" target="blank">Compartilhar no Whatsapp</a>
                </div>
                <span class="white-span p3">%s</span>
                <div class="flex-row flex-m-column">%s
                </div>
                <div class = "info">
                    <a href="#entenda-mais" class="info-btn">Entenda a classificação dos níveis</a>
                    <div id="entenda-mais" class="info-modal-window">
                        <div><a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                            <div style="margin: 10px 15px 15px 15px;">
                                <h1 class="primary-span">Valores de referência</h1>
                                <div style="font-size: 14px">
                                    <i>Para mais detalhes confira nossa página de Metodologia no menu lateral</i>.
                                </div><br>
                                %s
    <div class='base-wrapper product-section'>
    </div>
    """
    % (bg, locality, msg, caption, cards),
    unsafe_allow_html=True,
    )


def genInputCustomizationSectionHeader(locality: str) -> None:
    st.write(
        """
        <div class="base-wrapper">
                <span class="section-header primary-span">Verifique os dados disponíveis <span class="yellow-span">(%s)</span></span>
                <br><br>
                <span>
                Usamos os dados do Brasil.io e DataSUS, mas é possível que esses dados estejam um pouco desatualizados. Se estiverem, é só ajustar os valores abaixo para continuar a simulação.
                <br><b>Para municípios usamos os dados de leitos da respectiva regional de saúde.</b>
                </span>
                <br>
        </div>"""
        % locality,
        unsafe_allow_html=True,
    )

def gen_footer() -> None:

    st.write(
        """
        <div class="magenta-bg">
                <div class="base-wrapper">
                        <div class="logo-wrapper">
                                <span><b>A equipe do Coronacidades está à disposição para apoiar o gestor público a aprofundar a análise para seu estado ou município, de forma inteiramente gratuita.</b>
                                Também queremos queremos ouvir sua opinião sobre a ferramenta, entre em contato via chat (canto inferior direito). Outras ferramentas e mais recursos para responder à crise da Covid-19 estão disponíveis em nosso site 
                                <a target="_blank" style="color:#3E758A;" href="https://coronacidades.org/">coronacidades.org</a>.</span><br/>
                                <span><b>As análises apresentadas no Farol Covid são indicativas, feitas a partir de dados oficiais públicos e estudos referenciados já publicados, estando sujeitas a variáveis que aqui não podem ser consideradas.</b>
                                Trata-se de contribuição à elaboração de cenários por parte dos governos e não configura qualquer obrigação ou responsabilidade perante as decisões efetivadas.
                                Saiba mais sobre os cálculos por trás de análises e indicadores em nossas páginas de Níveis de Risco e Modelo Epidemiológico (menu lateral esquerdo), 
                                que mantemos atualizadas conforme evoluímos em nossas metodologias.<br><br></span>
                                <span><i>Todo código da ferramenta pode ser acessado no <a target="_blank" class="github-link" href="https://github.com/ImpulsoGov/farolcovid">Github do projeto</a>
                                e os dados estão disponíveis em nossa <a target="_blank" class="github-link" href="https://github.com/ImpulsoGov/coronacidades-datasource/blob/master/README.md">API</a>.</i></span>
                                </br></br></span>
                                <img class="logo-img" src="%s"/>
                                <div class="logo-section">
                                        <img class="logo-img" src="%s"/>
                                        <img class="logo-img" src="%s"/>
                                        <img class="logo-img" src="%s"/>
                                </div>
                        </div>
                </div>
        </div>"""
        % (Logo.IMPULSO.value, Logo.CORONACIDADES.value, Logo.ARAPYAU.value, Logo.SESI.value),
        unsafe_allow_html=True,
    )

# VIEW COMPONENTS SIMULACOVID

def gen_ambassador_section() -> None:

    st.write(
        """
        <br>
        <div class="base-wrapper flex flex-column" style="background-color:#0090A7">
            <div class="white-span header p1" style="font-size:30px;">IMPORTANTE: Usamos dados abertos e históricos para calcular os indicadores.</div><br>
            <span class="white-span"> <b>Quer aprofundar a análise para seu Estado ou Município?</b> A equipe do Coronacidades está disponível de forma inteiramente gratuita!</span>
            <a class="btn-ambassador" href="https://coronacidades.org/fale-conosco/" target="blank">FALE CONOSCO</a>
        </div>""",
        unsafe_allow_html=True,
    )

def try_int(possible_int):
    try:
        return int(float(possible_int))
    except Exception as e:
        return possible_int
