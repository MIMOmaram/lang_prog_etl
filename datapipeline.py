import requests
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2 as y

def extract(url):
    response = requests.get(url)
    text= BeautifulSoup(response.text, 'html.parser')
    return text.get_text()
   
def transform(texte):
    ligne_vide = [ligne.strip() for ligne in texte.split('\n') if ligne.strip()]
    texte = '\n'.join(ligne_vide)
    
    entiers = set()
    mots = set()

    for mot in texte.split():
        if mot.isdigit():
            entiers.add(int(mot))
        else:
            mots.add(mot.upper())  
   
    return list(entiers), list(mots)


def load(entiers, mots):
    conn = y.connect(
        host="127.0.0.1",
        port="5432",
        database="madw",
        user="postgres",
        password="fatma95356658"
    )
    cursor = conn.cursor()
    min_length = min(len(entiers), len(mots))

    for i in range(min_length):
        cursor.execute("""
            INSERT INTO tab_mdaw (entiers, mots) VALUES (%s, %s)
        """, (entiers[i], mots[i]))

    conn.commit()
    print("Données chargées avec succès dans la base de données.")
    conn.close()


url = "https://www.data.gov.tn"
texte_extrait = extract(url)
entiers, mots = transform(texte_extrait)
load(entiers, mots)
