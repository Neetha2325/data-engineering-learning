import oracledb

pool=oracledb.create_pool(user="neetha",
                          password="password123",
                          dsn="localhost/orclpdb")
with pool.acquire() as con_pool:
    cursor=con_pool.cursor()
    cursor.execute("Select count(*) from testing")
    print(cursor.fetchone())
