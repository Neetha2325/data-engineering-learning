#Qn:-Return the first character that appears only once.
s = "aabbcddeff"

dict1={}
for i in s:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1

for key,value in dict1.items():
    if dict1[key]==1:
        print(key)
        break
