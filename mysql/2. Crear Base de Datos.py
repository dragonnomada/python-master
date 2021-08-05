# https://dev.mysql.com/downloads/connector/python/

# https://www.datacamp.com/community/tutorials/mysql-python

import mysql.connector as mysql

client = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

cursor = client.cursor()

result = cursor.execute("CREATE DATABASE python-master")

client.commit()

print(result)


client.close()