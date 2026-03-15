#Tuple comprehension
t1=(*(x for x in range(1,6)),)
print(t1)

#using tuple constructor
t1=tuple(x for x in range(1,6))
print(t1)

t2=(*(x**2 for x in range(1,6)),)
print(t2)

t3=(*(x.lower() for x in 'pYTHON'),)
print(t3)

t4=(*(int(x) for x in '123'),)
print(t4)

t5=(*(x for x in '1bncrdg4657$%' if x.isalpha()),)
print(t5)
