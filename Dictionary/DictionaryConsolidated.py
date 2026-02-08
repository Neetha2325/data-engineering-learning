#1.Accessing
#Access by key
dict1={"a":8,"b":16,"c":24,"d":32,"e":45}
print(dict1["c"])

#Access using get (returns None if not found)
print(dict1.get("f"))
print(dict1.get("d"))

#All Keys
print(dict1.keys())

#All values
print(dict1.values())

#All key-value pairs
print(dict1.items())


#2.Updating/Adding:-
#Add or update
dict1["c"]=30
print(dict1.items())

dict1["f"]=56
print(dict1)

#update multiple
dict1.update({"g":64,"h":72})
print(dict1)

dict1.update({"c":24,"d":32,"e":40,"f":48,"g":56,"h":64,"i":72,"j":80})
print(dict1)

#3.Removing
#Remove by Key
dict1.pop("j")
print(dict1)

#Remove last inserted pair
dict1.popitem()
print(dict1)

#Delete by key
del dict1["a"]
print(dict1)

#Remove all
dict1.clear()
print(dict1)

#4.Utility functions
dict2={1:5,2:10,3:15,4:20,5:25}
print(dict2)
#count the no.of elements in dict
print(len(dict2))

#copy dictionary
dict3=dict2.copy()
print(dict3)

#Advanced Techniques
#5.Iterating
#Loop by Key
for k in dict2:
    print(k)

#Loop by key-value pairs
for key,value in dict2.items():
    print(key,value)

#6.Membership
#Check if key present in dict
print(5 in dict2)
#Check if key not present in dict
print(5 not in dict2)

#Check if value present in dict
if 20 in dict2.values():
    print("value present")

#Check if key-value pair present in dict
if (2,10) in dict2.items():
    print("value present")

#Check for multiple key-value pairs
pair_to_find={1:10,3:15,4:20}
found=True
for k in pair_to_find:
    if k not in dict2:
        found=False
        break
    if pair_to_find[k]!=dict2[k]:
        found=False
        break

if found:
    print("value present")
else:
    print("value not present")

#Show matched and failed pairs
pair_to_find={1:10,3:15,4:20}
matched=[]
failed=[]
for k in pair_to_find:
    if k in dict2 and pair_to_find[k]==dict2[k]:
        matched.append(k)
    else:
        failed.append(k)
print("Matched Keys:",matched)
print("Failed Keys:",failed)
print("Count of Matched Keys:",len(matched))
print("Count of Failed Keys:",len(failed))


#7.Dictionary Comprehension
dict4={k:v*3 for k,v in dict2.items() if k%2==0}
print(dict4)