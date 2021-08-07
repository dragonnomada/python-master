frutas = {
    "manzana": 38.5,
    "mango": 26.85
}

ventas = [
    {
        "fruta": "manzana",
        "precio": 30,
        "cantidad": 0.5,
        "total": 15,
        "fecha": "2021-08-05T15:00:00.000"
    },
    {
        "fruta": "manzana",
        "precio": 35,
        "cantidad": 1,
        "total": 35,
        "fecha": "2021-08-05T16:00:00.000"
    },
    {
        "fruta": "manzana",
        "precio": 40,
        "cantidad": 1.5,
        "total": 60,
        "fecha": "2021-08-05T17:00:00.000"
    },
    {
        "fruta": "mango",
        "precio": 40,
        "cantidad": 1.5,
        "total": 60,
        "fecha": "2021-08-05T15:00:00.000"
    },
    {
        "fruta": "mango",
        "precio": 45,
        "cantidad": 1,
        "total": 45,
        "fecha": "2021-08-05T16:00:00.000"
    },
    {
        "fruta": "mango",
        "precio": 50,
        "cantidad": 0.5,
        "total": 25,
        "fecha": "2021-08-05T17:00:00.000"
    },
]

def obtenerFrutas():
    for fruta in frutas:
        yield fruta, frutas[fruta]

def agregarFruta(nombre, precio):
    frutas[nombre] = precio

def buscarFruta(nombre):
    if not nombre in frutas:
        return None

    precio = frutas[nombre]

    return {
        "nombre": nombre,
        "precio": precio
    }

def editarFruta(nombre, precio):
    frutas[nombre] = precio

def eliminarFruta(nombre):
    if not nombre in frutas:
        return False

    del frutas[nombre]

    return True

def agregarVenta(nombre, precio, cantidad, total, fecha):
    ventas.append({
        "fruta": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total": total,
        "fecha": fecha
    })

def obtenerVentas():
    for venta in ventas:
        yield venta["fruta"], venta["precio"], venta["cantidad"], venta["total"], venta["fecha"]