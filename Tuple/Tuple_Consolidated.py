#1.Accessing
#Access by Index
t1=(10,20,30)
print(t1[1])
t2=(20,)
print(t2)
#Access from end
print(t1[-1])

#Slice
print(t1[0:1])

#slice with step
print(t1[0:2:2])


#2.Updating
#Immutable.So, convert to list and then update
t1=(1,2,3,4,5)
l1=list(t1)
l1.append(8)
t2=tuple(l1)
print(t2)


#3.Adding
#Concatenation
t2=(1,2)+(3,4)
print(t2)


#Repitition
t2=(1,2)*3
print(t2)

#4.Removing
#Immutable.So, need to remove using list
t1=(1,2,3,4,5)
l1=list(t1)
l1.pop(3)
t2=tuple(l1)
print(t2)

#5.Utility functions
#count elements
print(len(t1))

#Find position of an element
print(t1.index(3))

#count occurances of an element
print(t1.count(2))


#Advanced Techniques
#6.Nested Tuple

#matrix
matrix_tuple=((1,2),(3,4))

#accessing
print(matrix_tuple[1][1])

#7.Iterating
#Iterating over loop
for i in t1:
    print(i)

#Enumeration
for i,v in enumerate(t1):
    print(i,v)

#8.Membership
print(10 in t1)
print(10 not in t1)

#9.Built-in functions
#min
print(min(t1))

#max
print(max(t1))

#sum
print(sum(t1))