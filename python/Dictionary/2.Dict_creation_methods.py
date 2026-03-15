#iterable pairs
iterable_pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
d1=dict(iterable_pairs)
print(d1)

#zip function
l1=[1,2,3,4,5]
l2=['one','two','three','four','five']
d2=dict(zip(l1,l2))
print(d2)

#enumerate
l3=['one','two','three','four','five']
d3=dict(enumerate(l3,start=1))
print(d3)
