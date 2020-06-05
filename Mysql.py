import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",password="root",db="employeedb")
cur=con.cursor()
cur.execute("select * from employee")
result=cur.fetchall()
for i in result:
    print(i)
cur.close()
con.close()

