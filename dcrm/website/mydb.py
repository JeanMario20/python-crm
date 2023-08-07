import mysql.connector

DataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

#prepare a cursor object
print('all done')