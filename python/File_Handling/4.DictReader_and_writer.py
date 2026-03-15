import csv 

with open('file1.csv','r') as file1:
    csv_reader=csv.DictReader(file1)

    with open('new_file3.csv','w') as file2:
        field_name=['first_name','last_name','email']
        csv_writer=csv.DictWriter(file2,fieldnames=field_name,delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
        
        for line in csv_reader:
        #prints entire content
            print(line)
        #prints whatever key is given
            print(line['email'])



#Load only firstname and lastname in a new file

import csv         

with open('file1.csv','r') as file1:
    csv_reader=csv.DictReader(file1)

    with open('new_file4.csv','w',newline='',encoding='utf-8') as file2:
        field_names=['first_name','last_name']
        csv_writer=csv.DictWriter(file2,delimiter='\t',fieldnames=field_names)

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
