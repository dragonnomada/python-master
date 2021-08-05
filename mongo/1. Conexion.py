# pip install "pymongo[srv]"

from pymongo import MongoClient

# mongodb://localhost/python-master
client = MongoClient("mongodb://localhost/python-master")

print(client)

client.close()