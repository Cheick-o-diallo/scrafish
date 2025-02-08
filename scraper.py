import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(start_url, num_pages, output_file):
    data = []
    
    for page in range(1, num_pages + 1):
        url = f"{start_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Exemple de scraping : extraire les titres des articles
        items = soup.find_all("h2", class_="title")
        for item in items:
            data.append({"title": item.text.strip()})
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
