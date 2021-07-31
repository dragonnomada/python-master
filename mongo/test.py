# python -m pip install "pymongo[srv]"

from pymongo import MongoClient

client = MongoClient("mongodb://localhost/test")

db = client["test"]

messagesCollection = db["messages"]

cursor = messagesCollection.find({})

for doc in cursor:
    print(doc)