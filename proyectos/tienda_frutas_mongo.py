from pymongo import MongoClient

# TODO: Crea un cliente de conexión a la base de datos de Mongo DB
client = MongoClient("mongodb+srv://tienda:tienda123@cluster0.e5oc3.mongodb.net/tienda")

# TODO: Recupera la base de datos `tienda`
db = client["tienda"]

# TODO: Recupera la colección `tienda.frutas`
frutasCollection = db["frutas"]

# TODO: Recupera la colección `tienda.ventas`
ventasCollection = db["ventas"]

def obtenerFrutas():
    # pass
    # TODO: Recorrer cada fruta de la colección `tienda.frutas`
    
    # TODO: hacer un yield sobre fruta["nombre"], fruta["precio"]

    for fruta in frutasCollection.find():
      yield fruta["nombre"], fruta["precio"]

def agregarFruta(nombre, precio):
    # pass
    # TODO: Hacer un insert_one en la colección `tienda.frutas` con { "nombre": nombre, "precio": precio }
    frutasCollection.insert_one({ "nombre": nombre, "precio": precio })

def buscarFruta(nombre):
    # TODO: Recupera el documento con la fruta de nombre `nombre` en la colección `tienda.frutas`

    # TODO: Si el documento es None regresa None

    fruta = {} # SUSTITUIR POR EL OBTENIDO

    # Regresa el documento nombre y precio de la fruta
    return {
        "nombre": fruta["nombre"],
        "precio": fruta["precio"]
    }

def editarFruta(nombre, precio):
    pass
    # TODO: Actualiza la fruta con el nombre `nombre` y el `precio` de la colección `tienda.frutas`
    # Hint: usa update_one({ "nombre": nombre })

def eliminarFruta(nombre):
    pass
    # TODO: Elimina la fruta con el nombre `nombre` y el `precio` de la colección `tienda.frutas`
    # Hint: usa delete_one({ "nombre": nombre })

def agregarVenta(fruta, precio, cantidad, total, fecha):
    pass

    # TODO: Hacer un insert_one en la colección `tienda.ventas` con 
    # { "fruta": fruta, "precio": precio, "cantidad": cantidad, "total": total, "fecha": fecha }

def obtenerVentas():
    pass
    # TODO: Recorre cada venta de la colección `tienda.ventas`
    
    # TODO: haz un yield sobre venta["FRUTA"], venta["PRECIO"], venta["CANTIDAD"], venta["TOTAL"], venta["FECHA"]