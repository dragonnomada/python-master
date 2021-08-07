# TODO: Abre la hoja de Excel que contiene el DataFrame de frutas (NOMBRE | PRECIO)

# TODO: Abre la hoja de Excel que contiene el DataFrame de ventas (FRUTA | PRECIO | CANTIDAD | TOTAL | FECHA)

def obtenerFrutas():
    pass
    # TODO: Recorre cada fruta del DataFrame de frutas
    
    # TODO: haz un yield sobre df_frutas["NOMBRE"], df_frutas["PRECIO"]

def agregarFruta(nombre, precio):
    pass
    # TODO: Agrega una fila más al DataFrame de frutas con el `nombre` y `precio`
    # Hint: df_frutas.append(pd.DataFrame({ "NOMBRE": nombre, "PRECIO": precio }))
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)

def buscarFruta(nombre):
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    
    # TODO: En caso de que no devuelve None
    
    # TODO: Recupera el precio de la fruta con el `nombre`
    precio = None # SUSTITUIR POR EL REAL

    # Regresa el nombre y precio de la fruta
    return {
        "nombre": nombre,
        "precio": precio
    }

def editarFruta(nombre, precio):
    pass
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    
    # TODO: En caso de que no regresa
    
    # TODO: Actualiza el precio de la fruta con el `nombre`
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)

def eliminarFruta(nombre):
    pass
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    
    # TODO: En caso de que no regresa
    
    # TODO: Elimina el registro asociado a la fruta con el `nombre`
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)

def agregarVenta(fruta, precio, cantidad, total, fecha):
    pass

    # TODO: Agrega una fila más al DataFrame de ventas con la `fruta`, `precio`, `cantidad`, `total` y `fecha`
    
    # TODO: Guarda el DataFrame de ventas de vuelta a la hoja de Excel
    # Hint: df_ventas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)

def obtenerVentas():
    pass
    # TODO: Recorre cada venta del DataFrame de ventas
    
    # TODO: haz un yield sobre df_ventas["FRUTA"], df_ventas["PRECIO"], df_ventas["CANTIDAD"], df_ventas["TOTAL"], df_ventas["FECHA"]