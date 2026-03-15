my_dict={'name':'ABC','age':25,'city':'chennai'}
print(my_dict['name'])
print(my_dict['age'])

#get()
print(my_dict.get('country','unknown'))

#Adding new key-vaule to exisitng dictionary
my_dict['email']='abc@gmail.com'
print(my_dict)

#comprehension
sq={x**x for x in range(5)}
print(sq)

#keys
print(my_dict.keys())

#values
print(my_dict.values())

#items
print(my_dict.items())

#pop
popped=my_dict.pop('email')
print(popped)
print(my_dict)


#clear
my_dict.clear()
print(my_dict)

#Updating existing value
my_dict['age']=29
print(my_dict)

#Traverse
for key in my_dict:
    print(key,my_dict[key])


#Dict with mixed data types
d1={
    1:3.5,
    2.8:True,
    (8+6j):'complex'
}
print(d1)

#adding tuple as key in the dict
d1[(4,5)]='Tuple value'
print(d1)



