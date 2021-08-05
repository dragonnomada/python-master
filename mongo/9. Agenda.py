from pymongo import MongoClient

client = MongoClient("mongodb://localhost/")

db = client["agenda"] # Base de Datos: `agenda`

contactosCollection = db["contactos"] # Colección: `agenda.contactos`

# --- MENU ---

while True:
    # TODO: Pintar las opciones del menú (Agregar Contacto, Ver Contactos, ...)

    opc = input("Opción:> ")

    if opc == "1":
        # TODO: Capturar los datos del contacto
        nombre = input("Nombre: ")
        email = input("Email: ")
        # ...
        
        # TODO: Insertar el contacto en la base de datos
        contactosCollection.insert_one({
            "nombre": nombre,
            "email": email,
            # ...
        })

    if opc == "2":
        # TODO: Ver todos los contactos
        for contacto in contactosCollection.find():
            print("+----------------------------+")
            print("| {} ({}) |".format(contacto["nombre"], contacto["email"]))
            # ...
            print("+----------------------------+")
            print()

    # Buscar contactos por nombre (usar Regex)
    # Buscar contactos por teléfono (usar Regex)
    # Buscar contactos por email (usar Regex)

    if opc == "X":
        # TODO: Salir
        client.close()
        print("Bye")
        break
