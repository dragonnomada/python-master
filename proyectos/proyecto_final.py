# TODO: Comenta esta línea y descomenta la tienda a implementar
import tienda_frutas_diccionarios as tienda
# import tienda_frutas_excel as tienda
# import tienda_frutas_mongo as tienda
# import tienda_frutas_mysql as tienda

# Librería para obtener la fecha actual en formato ISO
import datetime
# Librería para ejecutar comandos del sistema operativo
import os

# Borra la pantalla según el sistema operativo
def borrarPantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Imprime los precios de las frutas obtenidos desde la tienda
def imprimirListaPreciosPorFruta():
    print("+" + "-" * 45 + "+")
    print("| {:20} | {:20} |".format("FRUTA", "PRECIO X KILO"))
    print("+ {:20} + {:20} +".format("-" * 20, "-" * 20))
    for fruta, precio in tienda.obtenerFrutas():
        print("| {:20} | ${:13.2f} x Kg. |".format(fruta, precio))
    print("+" + "-" * 45 + "+")

# Crea un menú de opciones para la tienda
while True:
    borrarPantalla()
    print("Bienvenido a la tienda")
    print("=" * 47)
    print()
    print("Frutas en venta:")
    imprimirListaPreciosPorFruta()
    print()
    print("Selecciona una opción:")
    print("1. Agregar Fruta")
    print("2. Establecer precio por kilo de fruta")
    print("3. Eliminar Fruta")
    print("4. Vender fruta")
    print("5. Reporte de ventas")
    print("-" * 47)
    print("Q. Salir")
    print()

    # Captura la opción del menú del usuario
    opcion = input(":> ")

    # Si la opción es `1. Agregar Fruta`
    if opcion == "1":
        print("Datos de la Fruta:")
        print()
        
        # Captura el nombre y precio de la fruta
        nombre = input("Nombre: ")
        precio = float( input("Precio: ") )
        
        # Agrega la fruta con su precio en la tienda
        tienda.agregarFruta(nombre, precio)
    # Si la opción es `2. Establecer precio por kilo de fruta`
    elif opcion == "2":
        print("Datos de la Fruta:")
        print()
        
        # Captura el nombre de la fruta
        nombre = input("Nombre: ")

        # Busca la fruta en la tienda
        fruta = tienda.buscarFruta(nombre)

        # Si la fruta no existe
        if fruta == None:
            print()
            print("¡La fruta no existe!")
            print()
        # Si la fruta si existe
        else:
            # Captura el nuevo precio de la fruta
            precio = float( input("Precio: ") )
            
            # Actualiza el precio de la fruta en la tienda
            tienda.editarFruta(nombre, precio)
            
            print()
            print("Se actualizó el precio de la fruta {} a ${:.2f} x kg.".format(nombre, precio))
            print()
    # Si la opción es `3. Eliminar Fruta`
    elif opcion == "3":
        print("Datos de la Fruta:")
        print()

        # Captura el nombre la fruta
        nombre = input("Nombre: ")

        #  Busca la fruta en la tienda
        fruta = tienda.buscarFruta(nombre)

        # Si la fruta no existe
        if fruta == None:
            print()
            print("¡La fruta no existe!")
            print()
        # Si la fruta si existe
        else:
            # Elimina la fruta de la tienda
            tienda.eliminarFruta(nombre)

            print()
            print("¡Se eliminó la fruta {}!".format(nombre))
            print()
    # Si la opción es `4. Vender fruta`
    elif opcion == "4":
        print("Datos de la Fruta:")
        print()
        
        # Captura el nombre la fruta
        nombre = input("Nombre: ")

        #  Busca la fruta en la tienda
        fruta = tienda.buscarFruta(nombre)

        # Si la fruta no existe
        if fruta == None:
            print()
            print("¡La fruta no existe!")
            print()
        # Si la fruta si existe
        else:
            # Recupera el precio actual de la fruta
            precio = fruta["precio"]
            
            # Captura la cantidad de kilogramos a vender
            cantidad = float( input("Kilogramos: ") )

            # Calcula el total vendido (cantidad vendidad por precio actual)
            total = precio * cantidad

            # Obtén la fecha actual en formato ISO
            fecha = datetime.datetime.utcnow().isoformat()
            
            # Agrega la venta a la tienda
            tienda.agregarVenta(nombre, precio, cantidad, total, fecha)
            
            # Imprime un mini reporte de lo vendido
            print()
            print("Se vendieron {:.2f} kilos de la fruta {} a ${:.2f} x kg.".format(cantidad, nombre, precio))
            print("Total: ${:.2f}".format(total))
            print("Fecha: {}".format(fecha))
            print()
    # Si la opción es `5. Reporte de ventas`
    elif opcion == "5":
        # Calcula las frutas distintas
        frutas = []
        # Guarda los precios de cada fruta por cada venta usando un diccionario
        fruta_precios = {}
        # Guarda las cantidades vendidas de cada fruta usando un diccionario
        fruta_cantidades = {}
        # Guarda el total vendido de cada fruta por cada venta usando un diccionario
        fruta_totales = {}

        # Recorre cada venta de la tienda
        for fruta, precio, cantidad, total, fecha in tienda.obtenerVentas():
            # Si la fruta no está registrada
            if not fruta in frutas:
                # Agrega la fruta distinta
                frutas.append(fruta)
            # Si la fruta no está registrada en los precios
            if not fruta in fruta_precios:
                # Crea una lista de precios vacía para esa fruta
                fruta_precios[fruta] = []
            # Si la fruta no está registrada en los cantidades
            if not fruta in fruta_cantidades:
                # Crea una lista de cantidades vacía para esa fruta
                fruta_cantidades[fruta] = []
                # Crea una lista de totales vacía para esa fruta
            # Si la fruta no está registrada en los totales
            if not fruta in fruta_totales:
                fruta_totales[fruta] = []
            
            # Agrega el precio, la cantidad y el total respectivamente en cada lista
            fruta_precios[fruta].append(precio)
            fruta_cantidades[fruta].append(cantidad)
            fruta_totales[fruta].append(total)

        # Guarda las ventas totales de cada fruta por cada venta
        fruta_ventas = {}

        # Guarda la suma de las cantidades vendidas de cada fruta por cada venta
        fruta_suma_cantidades = {}
        # Guarda la suma del total vendido de cada fruta por cada venta
        fruta_suma_totales = {}

        # Guarda el precio mínimo vendido de cada fruta por cada venta
        fruta_precio_min = {}
        # Guarda el precio máximo vendido de cada fruta por cada venta
        fruta_precio_max = {}
        # Guarda el precio promedio vendido de cada fruta por cada venta
        fruta_precio_prom = {}

        # Guarda la cantidad mínima vendida de cada fruta por cada venta
        fruta_cantidad_min = {}
        # Guarda la cantidad promedio vendida de cada fruta por cada venta
        fruta_cantidad_max = {}
        # Guarda la cantidad máxima vendida de cada fruta por cada venta
        fruta_cantidad_prom = {}

        # Guarda el total mínimo vendido de cada fruta por cada venta
        fruta_total_min = {}
        # Guarda el total máximo vendido de cada fruta por cada venta
        fruta_total_max = {}
        # Guarda el total promedio vendido de cada fruta por cada venta
        fruta_total_prom = {}

        for fruta in frutas:
            # Recupera los precios, cantidades y totales
            precios = fruta_precios[fruta]
            cantidades = fruta_cantidades[fruta]
            totales = fruta_totales[fruta]
            
            # Calcula el número de ventas
            fruta_ventas[fruta] = len(precios)
            
            # Calcula la suma de cantidades y totales
            fruta_suma_cantidades[fruta] = sum(cantidades)
            fruta_suma_totales[fruta] = sum(totales)

            # Calcula los precios
            fruta_precio_min[fruta] = min(precios)
            fruta_precio_max[fruta] = max(precios)
            fruta_precio_prom[fruta] = sum(precios) / len(precios)
            
            # Calcula las cantidades
            fruta_cantidad_min[fruta] = min(cantidades)
            fruta_cantidad_max[fruta] = max(cantidades)
            fruta_cantidad_prom[fruta] = sum(cantidades) / len(cantidades)
            
            # Calcula los totales
            fruta_total_min[fruta] = min(totales)
            fruta_total_max[fruta] = max(totales)
            fruta_total_prom[fruta] = sum(totales) / len(totales)

        # Guarda los precios totales respecto al precio mínimo basado en la cantidad total vendida
        fruta_total_precio_min = {}
        fruta_total_precio_max = {}
        fruta_total_precio_prom = {}

        for fruta in frutas:
            # Calcula los totales respecto al precio mínimo, máximo y promedio
            fruta_total_precio_min[fruta] = fruta_suma_cantidades[fruta] * fruta_precio_min[fruta]
            fruta_total_precio_max[fruta] = fruta_suma_cantidades[fruta] * fruta_precio_max[fruta]
            fruta_total_precio_prom[fruta] = fruta_suma_cantidades[fruta] * fruta_precio_prom[fruta]

        # Guarda las diferencias de los totales respecto a los precios mínimo, máximo y promedio
        # Respecto al total vendido. Esta diferencia indica cuánto se ganó o perdió
        # Si el precio no ubiera subido o bajado
        fruta_diferencia_precio_min = {}
        fruta_diferencia_precio_prom = {}
        fruta_diferencia_precio_max = {}

        for fruta in frutas:
            # Calcula las diferencias de los totales respecto al total global de la fruta
            fruta_diferencia_precio_min[fruta] = fruta_suma_totales[fruta] - fruta_total_precio_min[fruta]
            fruta_diferencia_precio_prom[fruta] = fruta_suma_totales[fruta] - fruta_total_precio_prom[fruta]
            fruta_diferencia_precio_max[fruta] = fruta_suma_totales[fruta] - fruta_total_precio_max[fruta]

        # Cuanta cada fruta para el reporte
        total_frutas = len(frutas)
        contador = 1

        # Imprime un reporte por cada fruta
        for fruta in frutas:
            borrarPantalla()
            print("Reporte de Venta de Frutas ({} / {})".format(contador, total_frutas))
            print("+" + "-" * 68 + "+")
            print("| Fruta: {:59} |".format(fruta))
            print("+" + "-" * 68 + "+")
            print("| {:20} | {:20} | {:20} |".format("VENTAS", "KILOS VENDIDOS", "TOTAL VENDIDO"))
            print("+ {:20} + {:20} + {:20} +".format("-" * 20, "-" * 20, "-" * 20))
            print("| {:<20} | {:<20.2f} | ${:<19.2f} |".format(fruta_ventas[fruta], fruta_suma_cantidades[fruta], fruta_suma_totales[fruta]))
            print("+" + "-" * 68 + "+")
            print("| {:66} |".format("PRECIOS DE VENTA:"))
            print("+" + "-" * 68 + "+")
            print("| {:20} | {:20} | {:20} |".format("MÍNIMO", "PROMEDIO", "MÁXIMO"))
            print("+ {:20} + {:20} + {:20} +".format("-" * 20, "-" * 20, "-" * 20))
            print("| ${:<19.2f} | ${:<19.2f} | ${:<19.2f} |".format(fruta_precio_min[fruta], fruta_precio_prom[fruta], fruta_precio_max[fruta]))
            print("+" + "-" * 68 + "+")
            print("| {:66} |".format("CANTIDADES DE VENTA:"))
            print("+" + "-" * 68 + "+")
            print("| {:20} | {:20} | {:20} |".format("MÍNIMA", "PROMEDIO", "MÁXIMA"))
            print("+ {:20} + {:20} + {:20} +".format("-" * 20, "-" * 20, "-" * 20))
            print("| {:<20.2f} | {:<20.2f} | {:<20.2f} |".format(fruta_cantidad_min[fruta], fruta_cantidad_prom[fruta], fruta_cantidad_max[fruta]))
            print("+" + "-" * 68 + "+")
            print("| {:66} |".format("TOTALES DE VENTA:"))
            print("+" + "-" * 68 + "+")
            print("| {:20} | {:20} | {:20} |".format("MÍNIMO", "PROMEDIO", "MÁXIMO"))
            print("+ {:20} + {:20} + {:20} +".format("-" * 20, "-" * 20, "-" * 20))
            print("| ${:<19.2f} | ${:<19.2f} | ${:<19.2f} |".format(fruta_total_min[fruta], fruta_total_prom[fruta], fruta_total_max[fruta]))
            print("+" + "-" * 68 + "+")
            print("| {:66} |".format("TOTALES DE VENTA USANDO LA CANTIDAD DE KILOS DE VENTA TOTAL:"))
            print("+" + "-" * 68 + "+")
            print("| {:20} | {:20} | {:20} |".format("AL PRECIO MÍNIMO", "AL PRECIO PROMEDIO", "AL PRECIO MÁXIMO"))
            print("+ {:20} + {:20} + {:20} +".format("-" * 20, "-" * 20, "-" * 20))
            print("| ${:<19.2f} | ${:<19.2f} | ${:<19.2f} |".format(fruta_total_precio_min[fruta], fruta_total_precio_prom[fruta], fruta_total_precio_max[fruta]))
            print("| {:66} |".format("-" * 66))
            print("| {:66} |".format("DIFERENCIA SOBRE EL TOTAL VENDIDO (${:.2f})".format(fruta_suma_totales[fruta])))
            print("| {:66} |".format("-" * 66))
            print("| $ {:<+18.2f} | $ {:<+18.2f} | $ {:<+18.2f} |".format(fruta_diferencia_precio_min[fruta], fruta_diferencia_precio_prom[fruta], fruta_diferencia_precio_max[fruta]))
            print("+" + "-" * 68 + "+")
            print()

            opcion = input("[Pulsa Enter para continuar o Q para regresar al menú] (Restan {} frutas)".format(total_frutas - contador))

            contador += 1

            if opcion.lower() == "q":
                break

        continue
    # Si la opción es `Q. Salir` (puede ser "q" o "Q")
    elif opcion.lower() == "q":
        print()
        print("Gracias por visitar la tienda :D")
        break
    # Si es cualquier otra opción
    else:
        print()
        print("¡La opción no es válida!")
        print()

    input("[Presiona Enter para continuar...]")