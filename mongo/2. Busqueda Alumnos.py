# pip install "pymongo[srv]"

from pymongo import MongoClient

protocol = "mongodb+srv" # mongodb+srv
server = "cluster0.xxxxx.mongodb.net" # localhost
user = "<usuario>" # -
password = "<contraseña>" # -
database = "python-master" # -

# 1. Abrir la conexión al cliente

# mongodb://localhost/python-master
# MongoDB Atlas - https://cloud.mongodb.com
# client = MongoClient("{}://{}:{}@{}/{}".format(protocol, user, password, server, database))
client = MongoClient("mongodb://localhost/python-master")

# 2. Recuperar la base de datos de trabajo
db = client["python-master"]

# 3. Recuperar la colección de trabajo
alumnosCollection = db["alumnos"]

# 4. Buscar todos los documentos (búqueda sin criterio) y recorrer los documentos encontrados
for alumno in alumnosCollection.find():
    # 5. Imprimir el documento (el documento es un diccionario dónde cada campo es una clave)
    print(alumno)

#  6. Cerrar la conexión
client.close()