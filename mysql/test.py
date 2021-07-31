import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "test"
)

print(db)

cursor = db.cursor()

cursor.execute("SELECT * FROM pruebas")

for record in cursor.fetchall():
    print(record)

db.close()