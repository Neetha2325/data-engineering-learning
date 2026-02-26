import oracledb
try:
    con=oracledb.connect(user="neetha",password="password123",dsn="localhost/orclpdb")
    #print(con.version)

    cursor=con.cursor()
    
    #DDL - Create 
    #cursor.execute("create table testing(no integer)")
    #print("Table created successfully")

    #cursor.execute("insert into testing values (:1)",(1,))
    #cursor.execute("insert into testing values (:1)",(2,))
    #cursor.execute("insert into testing values (:1)",(3,))
    #cursor.execute("insert into testing values (:1)",(4,))
    #cursor.execute("insert into testing values (:1)",(5,))
    #con.commit()

    #print("Records inserted successfully")

    
    #DDL - Alter
    #cursor.execute("alter table testing add customer_name varchar(20)")
    #con.commit()

    #DML-Update
    #cursor.execute("update testing set customer_name=:1 where no=:2",('John',3))
    #con.commit()

    #DML-delete
    #cursor.execute("delete from testing where no=4")
    #con.commit()

    #DML- Select 
    cursor.execute("Select * from testing")
    for row in cursor:
        print(row)

except oracledb.DatabaseError as e:
    print("Oracle Error:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


