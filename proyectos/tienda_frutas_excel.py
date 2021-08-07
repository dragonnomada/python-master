import pandas as pd
import openpyxl
import xlsxwriter
# TODO: Abre la hoja de Excel que contiene el DataFrame de frutas (NOMBRE | PRECIO)
df_frutas = pd.read_excel("tienda.xlsx", sheet_name="frutas", engine="openpyxl")

print(df_frutas)

# TODO: Abre la hoja de Excel que contiene el DataFrame de ventas (FRUTA | PRECIO | CANTIDAD | TOTAL | FECHA)
df_ventas = pd.read_excel("tienda.xlsx", sheet_name="ventas", engine="openpyxl")

print(df_ventas)

def obtenerFrutas():
    # pass
    # TODO: Recorre cada fruta del DataFrame de frutas
    for i in df_frutas.index:
      # TODO: haz un yield sobre df_frutas["NOMBRE"], df_frutas["PRECIO"]
      yield df_frutas["NOMBRE"][i], df_frutas["PRECIO"][i]

def agregarFruta(nombre, precio):
    global df_frutas
    # pass
    # TODO: Agrega una fila más al DataFrame de frutas con el `nombre` y `precio`
    # Hint: df_frutas.append(pd.DataFrame({ "NOMBRE": nombre, "PRECIO": precio }))
    df_frutas = df_frutas.append(pd.DataFrame({ "NOMBRE": [nombre], "PRECIO": [precio] }), ignore_index=True)
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)
    writer = pd.ExcelWriter("tienda.xlsx", engine = 'xlsxwriter')

    df_frutas.to_excel(writer, sheet_name="frutas", engine="xlsxwriter", index=None)
    df_ventas.to_excel(writer, sheet_name="ventas", engine="xlsxwriter", index=None)

    writer.save()
    # writer.close()

def buscarFruta(nombre):
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    # Hint: fruta = df_frutas.query("NOMBRE == '{}'".format(nombre))

    fruta = df_frutas.query("NOMBRE == '{}'".format(nombre))

    # TODO: En caso de que no devuelve None
    # HINT:
    if len(fruta) == 0:
      return None

    # TODO: Recupera el precio de la fruta con el `nombre`
    # HINT: precio = fruta["PRECIO"].iloc[0]
    # precio = None # SUSTITUIR POR EL REAL
    precio = fruta["PRECIO"].iloc[0]

    # Regresa el nombre y precio de la fruta
    return {
        "nombre": nombre,
        "precio": precio
    }

def editarFruta(nombre, precio):
    # pass
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    # Hint: fruta = df_frutas.query("NOMBRE == '{}'".format(nombre))
    fruta = df_frutas.query("NOMBRE == '{}'".format(nombre))

    # TODO: En caso de que no regresa
    # HINT:
    if len(fruta) == 0:
      return None

    # TODO: Actualiza el precio de la fruta con el `nombre`
    # HINT: df_frutas.loc[fruta.index, "PRECIO"] = 39.45
    df_frutas.loc[fruta.index, "PRECIO"] = precio
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)
    writer = pd.ExcelWriter("tienda.xlsx", engine = 'xlsxwriter')

    df_frutas.to_excel(writer, sheet_name="frutas", engine="xlsxwriter", index=None)
    df_ventas.to_excel(writer, sheet_name="ventas", engine="xlsxwriter", index=None)

    writer.save()

def eliminarFruta(nombre):
    global df_frutas
    # TODO: Determina si la fruta con el `nombre` está en el DataFrame de frutas
    fruta = df_frutas.query("NOMBRE == '{}'".format(nombre))

    # TODO: En caso de que no regresa
    if len(fruta) == 0:
      return None
    
    # TODO: Elimina el registro asociado a la fruta con el `nombre`
    df_frutas = df_frutas.drop(fruta.index)
    
    # TODO: Guarda el DataFrame de frutas de vuelta a la hoja de Excel
    # Hint: df_frutas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)
    writer = pd.ExcelWriter("tienda.xlsx", engine = 'xlsxwriter')

    df_frutas.to_excel(writer, sheet_name="frutas", engine="xlsxwriter", index=None)
    df_ventas.to_excel(writer, sheet_name="ventas", engine="xlsxwriter", index=None)

    writer.save()

def agregarVenta(fruta, precio, cantidad, total, fecha):
    pass

    # TODO: Agrega una fila más al DataFrame de ventas con la `fruta`, `precio`, `cantidad`, `total` y `fecha`
    
    # TODO: Guarda el DataFrame de ventas de vuelta a la hoja de Excel
    # Hint: df_ventas.to_excel(<ruta al archivo xlsx>, sheet_name="...", ...)

def obtenerVentas():
    pass
    # TODO: Recorre cada venta del DataFrame de ventas
    
    # TODO: haz un yield sobre df_ventas["FRUTA"], df_ventas["PRECIO"], df_ventas["CANTIDAD"], df_ventas["TOTAL"], df_ventas["FECHA"]