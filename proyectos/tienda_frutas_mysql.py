# TODO: Crea un cliente de conexión a la base de datos de MySQL

# TODO: Recupera la base de datos `tienda`

# TODO: Recupera la tabla `tienda.frutas`

# TODO: Recupera la tabla `tienda.ventas`

def obtenerFrutas():
    pass
    # TODO: Recorrer cada fruta de la tabla `tienda.frutas`
    
    # TODO: hacer un yield sobre fruta["nombre"], fruta["precio"]

def agregarFruta(nombre, precio):
    pass
    # TODO: Hacer un INSERT en la tabla `tienda.frutas` con { "nombre": nombre, "precio": precio }

def buscarFruta(nombre):
    # TODO: Recupera el documento con la fruta de nombre `nombre` en la tabla `tienda.frutas`

    # TODO: Si el documento es None regresa None

    fruta = {} # SUSTITUIR POR EL OBTENIDO

    # Regresa el documento nombre y precio de la fruta
    return {
        "nombre": fruta["nombre"],
        "precio": fruta["precio"]
    }

def editarFruta(nombre, precio):
    pass
    # TODO: Actualiza la fruta con el nombre `nombre` y el `precio` de la tabla `tienda.frutas`
    # Hint: usa UPDATE ({ "nombre": nombre })

def eliminarFruta(nombre):
    pass
    # TODO: Elimina la fruta con el nombre `nombre` y el `precio` de la tabla `tienda.frutas`
    # Hint: usa DELETE ({ "nombre": nombre })

def agregarVenta(fruta, precio, cantidad, total, fecha):
    pass

    # TODO: Hacer un insert_one en la tabla `tienda.ventas` con 
    # { "fruta": fruta, "precio": precio, "cantidad": cantidad, "total": total, "fecha": fecha }

def obtenerVentas():
    pass
    # TODO: Recorre cada venta de la tabla `tienda.ventas`
    
    # TODO: haz un yield sobre venta["FRUTA"], venta["PRECIO"], venta["CANTIDAD"], venta["TOTAL"], venta["FECHA"]