import streamlit as st
import scraper
import data_cleaning 
import dashboard
import evaluation 
import pandas as pd

st.set_page_config(page_title="Scraper App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Scraper", "Télécharger", "Dashboard", "Évaluation"])

# Charger les données
DATA_FILE = "scraped_data.csv"

if page == "Scraper":
    st.title("Scraping des données")
    url = st.text_input("Entrer l'URL de départ")
    num_pages = st.number_input("Nombre de pages à scraper", min_value=1, value=5)
    if st.button("Lancer le scraping"):
        scraper.scrape_data(url, num_pages, DATA_FILE)
        st.success("Scraping terminé ! Données enregistrées.")

elif page == "Télécharger":
    st.title("Téléchargement des données")
    try:
        with open(DATA_FILE, "rb") as file:
            st.download_button("Télécharger les données brutes", file, file_name="raw_data.csv")
    except FileNotFoundError:
        st.error("Aucune donnée trouvée. Veuillez d'abord scraper.")

elif page == "Dashboard":
    st.title("Visualisation des données")
    try:
        df = pd.read_csv(DATA_FILE)
        cleaned_df = data_cleaning.clean_data(df)
        dashboard.show_dashboard(cleaned_df)
    except FileNotFoundError:
        st.error("Aucune donnée trouvée. Veuillez d'abord scraper.")

elif page == "Évaluation":
    st.title("Formulaire d'évaluation")
    evaluation.show_evaluation_form()