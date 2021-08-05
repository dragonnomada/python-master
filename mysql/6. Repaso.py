import mysql.connector as mysql

client = mysql.connect(
    host="localhost",
    user="root",
    passwd="password"
)

cursor = client.cursor()

cursor.execute("CREATE DATABASE demo")

client.commit()

client.close()

# --- Trabajar sobre `demo` ---

client = mysql.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="demo"
)

cursor = client.cursor()

cursor.execute("""
CREATE TABLE historial (
    id_historial INT PRIMARY KEY,
    nombre VARCHAR(60) NOT NULL
)
""")

client.commit()

client.close()