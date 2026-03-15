import csv 

with open('file1.csv','r') as file:
    file_reader=csv.reader(file)

    #Skips the 1st file mostly heading,that is the heading 
    next(file_reader)

    with open('new_file2.csv','w') as file2:
        #file_writer=csv.writer(file2,delimiter="-")
        file_writer=csv.writer(file2,delimiter='\t')
        for line in file_reader:
            #prints fully as it is in the form of list
            print(line)
            file_writer.writerow(line)
        #prints 1st index value alone 
        #print(line[1])
