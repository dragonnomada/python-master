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

result = cursor.execute("""
INSERT INTO alumnos 
    (`nombre`, `email`, `alias`) 
    VALUES 
    ('Ana Ming', 'ana.ming28@gmail.com', 'aming')
""")

# Es importante al insertar o actualizar enviar el commit para que se ejecute en la base de datos
client.commit()

print(result)

client.close()

