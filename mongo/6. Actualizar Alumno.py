from pymongo import MongoClient

client = MongoClient("mongodb+srv://pyalumno:py123@cluster0.e5oc3.mongodb.net/python-master")

db = client["python-master"]

alumnosCollection = db["alumnos"]

# query
filter = {
    "email": "dragonnomada123@gmail.com"
}

update = {
    "$set": {
        "alias": "Dragón Nómada 123"
    }
}

# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.update_one
# https://pymongo.readthedocs.io/en/stable/api/pymongo/results.html#pymongo.results.UpdateResult
result = alumnosCollection.update_one(filter, update)

print("Encontrados:", result.matched_count)
print("Modificados:", result.modified_count)
print("Ids modificicados:", result.upserted_id)

client.close()