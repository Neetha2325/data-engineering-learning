#1.List creation
l1=[1,2,3]
print(l1)

l2=list((1,2,3))
print(l2)

#2.Accessing
#Access by index
print(l1[1])

#Access from end
print(l1[-1])

#Slice
print(l1[0:1])

#Slice with step
print(l1[::2])

#3.Updating
#Update element
l1[2]=4
print(l1)

#Update slice
l1[0:1]=[6,5]
print(l1)

#4.Ordering
#Sort in ascending
l1.sort()
print(l1)
#Sort in reverse
l2.reverse()
print(l2)

#5.Adding
#Adding at end
l1.append(8)
print(l1)

#insert at index
l1.insert(2,6)
print(l1)

#Add multiple values
l1.extend([10,20,30,40,50])
print(l1)

#6.Removing
#remove by value
l1.remove(6)
print(l1)

#remove by index
l1.pop(1)
print(l1)

#remove all
l2.clear()
print(l2)

#7.Utility functions
#Count total elements
print(len(l1))

#Count occurances of a particular element
print(l1.count(10))

#find index of a particular value
print(l1.index(50))

#copy list
l5=l1.copy()
print(l5)
