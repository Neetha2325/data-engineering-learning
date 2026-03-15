file=open('info.txt','r')
print(file.read())
#Go to a particular position
file.seek(0)

#Tell the current position
print(file.tell())

#Reads only 1 line
print(file.readline())
