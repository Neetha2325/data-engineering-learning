#1.List Comprehensions
#list creation using list comprehension
i=[x*2 for x in [1,2,3,4,5]]
print(i)

#list comprehension using condition
i=[x*2 for x in [1,2,3,4,5] if x%2==0]
print(i)

#2.Nested List
#nested list comprehension
matrix=[[1,2],[3,4]]
print(matrix)

#nested list accessing elements
print(matrix[1][0])

#3.Combining list
#concatenation of lists
list1=[1,2]+[3,4]
print(list1)

#Repitition of list
list2=list1*2
print(list2)

#4.Iterating over list
#list iteration
for x in [1,2,3,4,5]:
    print(x)
#enumeration
for index,value in enumerate(list2):
    print(index,value)

#5.Membership
#in
print(34 in list2)

#not in
print(34 not in list2)

#6.Built-in functions
#min
print(min(list2))

#max
print(max(list2))

#sum
print(sum(list2))