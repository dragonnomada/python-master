# https://dev.mysql.com/downloads/connector/python/

# https://www.datacamp.com/community/tutorials/mysql-python

import mysql.connector as mysql

client = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "python-master" # OJO: Indicamos la base de datos
)

cursor = client.cursor()

cursor.execute("""
SELECT * FROM alumnos
""")

for alumno in cursor.fetchall():
    print(alumno)

client.close()
