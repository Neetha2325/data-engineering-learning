S=set(range(1,11))
A={1,2,3,4,5,7}
B={5,6,7,8,9,10}
C=set(range(1,11))
D={1,2,3,4,5}
E={6,7,8,9,10}

print(A.issubset(S))
print(B.issubset(S))
print(C==S)

print(A<S)
print(C<S)

print(S.issuperset(A))

print(D.isdisjoint(E))
print(B.isdisjoint(A))
