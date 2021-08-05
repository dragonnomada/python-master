from pymongo import MongoClient

client = MongoClient("mongodb://localhost/")

db = client["repaso"] # Base de Datos: `repaso`

frutasCollection = db["frutas"] # Colección: `repaso.frutas`

# --- Insertamos las frutas ---

frutasCollection.insert_one({
    "name": "Manzana",
    "color": "Rojo",
    "peso": 60
})

frutasCollection.insert_many([
    {
        "name": "Plátano",
        "color": "Amarillo",
        "peso": 80
    },
    {
        "name": "Mango",
        "color": "Amarillo",
        "peso": 60
    }
])

# --- Buscar las frutas amarillas ---

query = {
    "color": "Amarillo"
}

for fruta in frutasCollection.find(query):
    print(fruta)

client.close()