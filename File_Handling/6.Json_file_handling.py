import json 
with open('states.json','r') as f:
    data=json.load(f)

for state in data['states']:
    print(state['name'],state['area_codes'])
    
for state in data['states']:
    del state['area_codes']


with open('new_json.json','w') as f:
    json.dump(data,f,indent=2)