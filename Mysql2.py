import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",password="root",db="employeedb")
cur=con.cursor()
empid=input("Enter empid ")
empname=input("Enter empid ")
cur.execute("select * from employee where Empid=%s and Empname=%s",[empid,empname])
result=cur.fetchone()
print(result)
cur.close()
con.close()
