# pip install "pymongo[srv]"

from pymongo import MongoClient

# mongodb://localhost/python-master
client = MongoClient("mongodb+srv://pyalumno:py123@cluster0.e5oc3.mongodb.net/python-master")

print(client)

client.close()