A={1,2,3,5,7}
B={5,7,9,10,11}

#union
print(A.union(B))
print(A|B)

#Intersection
print(A.intersection(B))
print(A&B)


#Difference
print(A.difference(B))
print(A-B)

print(B.difference(A))
print(B-A)

#Symmetric difference
print(A.symmetric_difference(B))
print(A^B)

#Union Update
A=A.union(B)
print(A)


#Intersection Update
A.intersection_update(B)
print(A)
print(B)

#difference update
A.difference_update(B)
print(A)
print(B)

#Symmetric difference Update
A.symmetric_difference_update(B)
print(A)
print(B)
