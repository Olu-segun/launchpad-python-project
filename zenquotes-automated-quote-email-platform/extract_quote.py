import requests
from datetime import datetime

def extract_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        data = response.json()
        quote_author = f'"{data[0]["q"]}" - {data[0]["a"]}'
        return quote_author
    
    except Exception as e:
        print(f'Error fetching quote: {e}')




