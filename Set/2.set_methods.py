#Creation of set
set1={1,2,3}
print(set1)
print(type(set1))

set2=set()
print(set2)
print(type(set2))

set3=set([1,2,3])
print(set3)
print(type(set3))

set4=set('python')
print(set4)
print(type(set4))

#Adding elements to set
set4.add('kite')
set4.add((1,2,3))
set4.add(12)
print(set4)

#remove element
set4.remove('kite')
print(set4)

#pop()
set4.pop()
print(set4)

#update
set3.update((80,90))
print(set3)

set3.update('ruby')
print(set3)
set3.update([11,15,17])
print(set3)

#copy()
s2=set3.copy()
print(id(s2),id(set3))

#discard
set3.discard(20)
#set3.remove(20) #throws keyError

set3.discard('r')
print(set3)

#clear()
set3.clear()
print(set3)