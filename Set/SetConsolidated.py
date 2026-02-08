#1.Accessing
#using Loop
for x in {1,2,3,4,5}:
    print(x)
#Membership
print(20 in {1,2,3,})

#2.Updating
#Add single element
set1={10,20,30,40,50}
set1.add(20)
print(set1)
#Adding multiple values
set1.update((2,3,4,5))
print(set1)

#3.Removing
#Remove
set1.remove(20)
print(set1)
#Discard
set1.discard(25)
print(set1)
#pop
popped_item=set1.pop()
print(popped_item)
print(set1)
#clear
set1.clear()
print(set1)

#4.utility functions
#Count the no of elements
set2={2,3,4,5,6}
print(len(set2))

#copy set
set3=set2.copy()
print(set3)

#5.Set Operations
set1={1,2,3,4,5}
set2={1,2,3}

#Union (or)
union_set=set1|set2
print(union_set)

#Intersection(and)
intersection_set=set1&set2
print(intersection_set)

#Difference
difference_set=set1-set2
print(difference_set)

#Symmetric Difference(Not common elements)
symmetrix_difference=set1^set2
print(symmetrix_difference)

#6.Advanced Techniques
#Set comprehension
set1={x for x in range(20) if x%5==0}
print(set1)

#Frozen Set
fs=frozenset(set1)
print(fs)
