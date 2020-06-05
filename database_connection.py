import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",password="root",db="employeedb")
cur=con.cursor()
cur.execute("select * from employee")
result=cur.fetchall()
"""for i in result:
    print(i)"""
    
cur.close()
con.close()
a=result

file=open("empdt.txt","w")
print(file.write(str(a)))
file.close()
file=open("empdt.txt","r")
print(file.read())
