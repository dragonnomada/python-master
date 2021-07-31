# pip install "pymongo[srv]"

from pymongo import MongoClient

protocol = "mongodb+srv" # mongodb
server = "cluster0.e5oc3.mongodb.net"
user = "pyalumno"
password = "py123"
database = "python-master"

# 1. Abrir la conexión al cliente

# mongodb://localhost/python-master
# MongoDB Atlas - https://cloud.mongodb.com
# client = MongoClient("mongodb+srv://pyalumno:py123@cluster0.e5oc3.mongodb.net/python-master")
client = MongoClient("{}://{}:{}@{}/{}".format(protocol, user, password, server, database))

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