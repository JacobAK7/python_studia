import requests

def pobierz_cene_euro():
    url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR?format=json"
    response = requests.get(url)
    data = response.json()
    return data['rates'][0]['mid']
