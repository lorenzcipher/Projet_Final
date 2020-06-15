# -*- coding: utf-8 -*-

import streamlit as st
from streamlit.logger import get_logger

import Algorithe_genetique_11062020 as ga

logger = get_logger(__name__)


st.sidebar.header("Paramètres")
st.title("Algorithme Génétique")
st.header("Description")
st.write("Rédiger une description générale des algorithmes génétique.")

st.header("Tutorial")
st.write("Rédiger une documentation step by step pour l'utilisation de cette appli et initialiser les paramètres à coté.")
# parameters
nombre_individus = st.sidebar.slider("Nombre d'individus", 1, 30, 1, 1)
nombre_generation = st.sidebar.slider("Nombre génération", 2, 20, 2, 1)
probabilite_mutation = st.sidebar.slider("Probabilité mutation", 0., 1., .1, .05)
probabilite_croisement = st.sidebar.slider("Probabilité croisement", 0., 1., .1, .05)
capacity = st.sidebar.slider("Capacité", 1, 10, 3, 1)
data = [1, 2, 3, 3]

parameters = {
    "nombre_individus": nombre_individus,
    "nombre_generation": nombre_generation,
    "probabilite_mutation": probabilite_mutation,
    "probabilite_croisement": probabilite_croisement,
    "data": data,
    "capacity": capacity
}

if st.sidebar.button("Initialiser population"):
    ag = ga.AG(**parameters)
    p = ag.fct_initialisation_population()
    st.write(p)

if st.button("Celebrate !"):
    st.balloons()