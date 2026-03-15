#1.Updating
#update
d1={1:'one',2:'two',3:'three'}
d2={4:'four',5:'five'}
d1.update(d2)
print(d1)

#fromkeys
l1=[1,2,3,4,5]
d_new=dict.fromkeys(l1)
print(d_new)

d_new_with_default=dict.fromkeys(l1,'Default Value')
print(d_new_with_default)


d1=dict.fromkeys([1,2,3],'Default value')
print(d1)

#copy()
d2=d1.copy()
print(d2)

#2.Deleting
#pop()
popped_value=d1.pop(5,"Missing")
print(popped_value)

#popped_value2=d1.pop(6)#This throws keyError because default value is not given here.
#print(popped_value2)

#popitem()
d5={1:'one',2:'two',3:'three'}
item=d5.popitem()
print(item)
print(d5)

#clear()
d1.clear()
print(d1)

