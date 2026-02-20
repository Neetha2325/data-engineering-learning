import json

people_string='''
{
    "people":[
    {
        "name":"Stephen Hawking",
        "phone":"615-245-9087",
        "emails":["stephen.official@gmail.com","stepehen-personal@gmail.com"]
    },
    {
        "name":"Denn Stuart",
        "phone":"619-245-8452",
        "emails":["denn-official@gmail.com","den-personal@gmail.com"]
    }
    ]
}
'''
#1.Convert json string into Python object
data=json.loads(people_string)
print(data)
print(type(data))
print(type(data['people']))

#2.Convert python object into json string
new_str=json.dumps(data,indent=2,sort_keys=True)
print(new_str)

#3.Loop through the python object and access particular key's values
for name in data['people']:
    print(name['name'])