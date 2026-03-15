#1.Tuple concatenation
t1=(1,2,3)
t2=(4,5)
t3=t1+t2
print(t3)

#2.Tuple repitition
t4=t1*2
print(t4)

#3.Packing
t5=10,20,30,40,50
print(t5)
print(type(t5))

#4.Unpacking
a,b,c,d,e=t5
print(a,b,c,d,e)

#starred * unpacking
a,*b,c=t5
print(a,b,c)

*a,b,c=t5
print(a,b,c)

a,b,*c=t5
print(a,b,c)


#5.Membership operator
print(20 in t5)
print(100 in t5)

print(20 not in t5)
print(100 not in t5)

