import requests
from config import TRANSLATION_API_KEY

def translate_titles(titles):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

    translated_titles = []

    for title in titles:
        payload = {
            "from": "es",  # Spanish 
            "to": "en",    # English 
            "q": title     # Text 
        }

        dataCard= []
        # Set the headers with the RapidAPI key
        headers = {
            "x-rapidapi-key": TRANSLATION_API_KEY,  
            "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        # Make POST request to the API
        response = requests.post(url, json=payload, headers=headers)
        dataCard = response.toString()
        translated_text = response.json()  # Directly take the response if it's a string
        translated_titles.append(translated_text)
        

    return translated_titles
