# https://dev.mysql.com/downloads/connector/python/

import mysql.connector as mysql

client = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password"
)

print(client)

client.close()