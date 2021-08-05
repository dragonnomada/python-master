from pymongo import MongoClient

client = MongoClient("mongodb://localhost/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

query = {
    "email": "ana.ming28@gmail.com"
}

for alumno in alumnosCollection.find(query):
    print(alumno)

client.close()