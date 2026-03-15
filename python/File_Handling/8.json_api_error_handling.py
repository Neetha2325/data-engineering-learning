import requests
import json 

def get_url(base):
    url=f"https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        print(data['base'])
    else:
        print("Error fetching data in this url",url)
    
base=get_url("USD")
print("Base : ",base)
