from pymongo import MongoClient

client = MongoClient("mongodb+srv://pyalumno:py123@cluster0.e5oc3.mongodb.net/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

# query
filter = {
    "alias": "ppdi"
}

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.delete_many
# https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.DeleteResult
result = alumnosCollection.delete_many(filter)

print("Eliminados:", result.deleted_count)

client.close()