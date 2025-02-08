import streamlit as st
import scraper
import data_cleaning 
import dashboard
import evaluation 
import pandas as pd
import os

st.set_page_config(page_title="Scraper App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à :", ["Scraper", "Télécharger", "Dashboard", "Évaluation"])

# Charger les données
DATA_FILE = "Beautifusoup_scraped_data/"

if page == "Scraper":
    st.title("Scraping des données")
    url = st.text_input("Entrer l'URL de départ")
    num_pages = st.number_input("Nombre de pages à scraper", min_value=1, value=5)
    if st.button("Lancer le scraping"):
        output_file = os.path.join(DATA_FILE, "new_scraped_data.csv")
        scraper.scrape_data(url, num_pages, output_file)
        st.success("Scraping terminé ! Données enregistrées.")

elif page == "Télécharger":
    st.title("Téléchargement des données")
    for file_name in os.listdir(DATA_FILE):
        file_path = os.path.join(DATA_FILE, file_name)
        with open(file_path, "rb") as file:
            st.download_button(f"Télécharger {file_name}", file, file_name=file_name)

elif page == "Dashboard":
    st.title("Visualisation des données")
    selected_file = st.selectbox("Sélectionnez un dataset :", os.listdir(DATA_FILE))
    
    if selected_file:
        df = pd.read_csv(os.path.join(DATA_FILE, selected_file))
        cleaned_df = data_cleaning.clean_data(df)
        dashboard.show_dashboard(cleaned_df)

elif page == "Évaluation":
    st.title("Formulaire d'évaluation")
    evaluation.show_evaluation_form()
