from pymongo import MongoClient

client = MongoClient("mongodb+srv://pyalumno:py123@cluster0.e5oc3.mongodb.net/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

query = {
    "email": "ana.ming28@gmail.com"
}

for alumno in alumnosCollection.find(query):
    print(alumno)

client.close()