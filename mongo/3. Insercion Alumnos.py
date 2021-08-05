from pymongo import MongoClient

client = MongoClient("mongodb://localhost/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_one
result = alumnosCollection.insert_one({
    "_id": "alumno-001", # Se puede omitir y mongo generará uno aleatorio
    "nombre": "Ana Ming",
    "email": "ana.ming28@gmail.com",
    "alias": "aming"
})

print(result.inserted_id)

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.insert_many
result = alumnosCollection.insert_many([
    {
        "_id": "alumno-002", # Se puede omitir y mongo generará uno aleatorio
        "nombre": "Pepe Díaz",
        "email": "pepe.dia78@hotmail.com",
        "alias": "ppdi"
    },
    {
        "_id": "alumno-003", # Se puede omitir y mongo generará uno aleatorio
        "nombre": "Jorge Rojo",
        "email": "jorge_rojo.98@yahoo.com.mx",
        "alias": "jr98"
    }
])

print(result.inserted_ids)

client.close()