#Basic Text file reading 
#1.read mode 
file=open('info.txt','r')
#--Gives output as str and reads file fully
print(file.read())

#prints only specific set of characters 
print(file.read(10))

#--Gives output as str and reads only one line
print(file.readline())

#--Gives output as list and reads fully
print(file.readlines())


#2.write method 
file=open('info.txt','w')
file.write("hello world")


#3.append mode 
file=open('info.txt','a')
#write into file 
file.write('hai Sri Sathya Sai')
#Write the list into file
lst=["This","is","python","programming"]
file.writelines(lst)
file.close()

#4.r+ -read first and then write

#5.w+ -write first and then read 

#6.Alternate way to read a file:-
#Automatically closes the file when with statement is used.So,no need to give close()
#With -context manager
with open('info.txt','r') as file:
    print(file.read())

#7.flush
# Tells to write the contents from buffer to file
file.flush()

