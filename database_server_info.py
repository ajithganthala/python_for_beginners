import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",password="root",db="employeedb")
print(con.get_server_info())
