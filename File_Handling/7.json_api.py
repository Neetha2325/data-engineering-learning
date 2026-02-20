import requests
import json 

url="https://api.exchangerate-api.com/v4/latest/USD"
response=requests.get(url)
data=response.json()

print(json.dumps(data,indent=5))
print("INR rate:",data['rates']['INR'])

with open('rates.json','w') as f:
    json.dump(data,f,indent=4)