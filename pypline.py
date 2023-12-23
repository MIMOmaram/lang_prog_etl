import requests
import pandas as pd

def extract():
    # Fonction d'extraction de données du site www.data.gov.tn
    url = "https://www.data.gov.tn/fr/"  # Remplacez par l'URL réel du site www.data.gov.tn
    response = requests.get(url)

    

    return response.text

print(extract())