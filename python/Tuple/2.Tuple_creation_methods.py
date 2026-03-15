#Tuple creation methods
#1.Using paranthesis -empty tuple is created
t1=()
print(t1)
print(type(t1))

#2.using tuple() constructor with iterable - list,string and range
t2=tuple([1,2,3])
print(t2)
print(type(t2))

t3=tuple('python')
print(t3)
print(type(t3))

t4=tuple(range(1,5))
print(t4)
print(type(t4))

#3.Creating single-element tuple
t5=(2,)
print(t5)
print(type(t5))

#4.Tuple packing multiple values without ()
t6=1,2,3,4,5
print(t6)
print(type(t6))
