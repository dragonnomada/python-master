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
CREATE TABLE alumnos (
  id_alumno INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  email VARCHAR(45) NOT NULL,
  alias VARCHAR(45) NULL,
  PRIMARY KEY (id_alumno))
""")

print(result)

client.close()