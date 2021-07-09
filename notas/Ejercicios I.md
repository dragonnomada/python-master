# Ejercicios - Parte I

Por [Dragón Nómada](https://dragonnomada.medium.com)

## 1. Imprimir un menú

Imprime un menú con al menos 3 opciones.

## 2. Repetir un menú indeterminadamente

Imprime un menú con al menos 3 opciones, de las cuáles una sea salir.

Captura el número de opción y si es distinto de salir, borra la pantalla y repite el menú.

## 3. Contador

Crea una variable que retenga un número entero a modo de contador.

En un menú muestra el valor actual del contador y la opción de incrementar, la opción de decrementar y la opción de salir.

Según la opción, incrementa o decrementa el contador y vuelve a mostrar el menú.

* Intenta hacer una pausa para especificar de qué valor a qué valor incremento o decremento.

## 4. Número en el rango

Crea dos variables para establecer un rango (límite inferior y superior).

Crea un menú que muestre el rango, la opción de determinar si un número esta en el rango y la opción de salir.

Haz una pausa para mostrar si el número está en el rango antes de volver al menú.

## 5. La canasta de frutas

Crea una lista vacía de frutas.

Crea un menú que muestre las frutas actuales de la lista, la opción de agregar una fruta y la opción de salir.

Considera que al agregar la fruta el usuario el nombre y este se deberá agregar a la lista como un texto.

## 6. Lista de números

Crea un menú que muestre una lista inicialmente vacía y permita capturar más números enteros.

Agrega la opción para mostrar la suma, la opción para mostrar el promedio, la opción para mostrar el mínimo y el máximo.

## 7. El contador de frutas

Crea un menú basado en [**La canasta de frutas**].

Agrega la opción de contar cuántas veces aparece una fruta. Solicita el nombre de la fruta y determina cuántas veces está en la canasta.

## 8. Las frutas distintas

Crea un menú basado en [**La canasta de frutas**].

Agrega la opción para mostrar las frutas distintas. Es decir, obtén todas las frutas distintas.

> Algoritmo para obtener las frutas distintas

```text
Crea una lista vacía para guardar las `frutas distintas`

Para cada `fruta` en la lista de `frutas`:
    Determina si la `fruta` no está en la lista de `frutas distintas`:
        Agrega la `fruta` en la lista de `frutas distintas`
```

## 9. El contador automático de frutas

Crea un menú basado en [**Las frutas distintas**].

Agrega la opción para mostrar las frutas distintas y cuántas veces aparece en la canasta.

## 10. Mover frutas entre canastas

Crea dos listas de frutas, para simular dos canastas distintas de frutas.

En un menú con la opción salir, muestra el contenido de cada canasta de frutas.

Agrega la opción de agregar una fruta en la primer canasta.

Agrega la opción para mover una fruta de la primer canasta a la segunda canasta. Considera que si la fruta no está en la canasta muestre un mensaje de imposibilidad.

## 11. Selección aleatoria

Crea una lista vacía para guardar números.

En un menú con la opción de salir muestra los números de la lista y la opción de agregar un número a la lista.

Agrega la opción de mostrar un número aleatorio de la lista.

**Nota:** Usa `import random` y `random.randint(0, N - 1)` para obtener un índice aleatorio entre 0 y `N`, dónde `N` es el tamaño de la lista. Luego recupera el elemento con ese índice en la lista y muéstralo.

## 12. Perros contra gatos

Crea una lista que contenga 20 textos con "P" y 50 textos con "G", que representarán un perro o un gato.

Crea una lista vacía llamada torneo.

En un menú con la opción salir, muestra la lista del torneo y la opción para seleccionar 6 elementos aleatorios y copialos en otra lista del torneo.

Agrega la opción para iniciar la pelea. Determina si ganan los perros si los elementos `"P"` superan a los `G`, empate si hay la misma cantidad o si ganan los gatos.

## 13. Lanzamiento de un misil

Crea una 2-tupla que acople dos valores para `x` y `y`.

En un menú con la opción salir, muestra el valor de la coordenada de lanzamiento.

Agrega la opción de modificar la coordenada. Captura la nueva `x` y `y` para modificar la `2-tupla`

Agrega la opción de lanzar misil. Esta opción imprimirá la coordenada `x`, `y` con el formato: `ATACANDO LA COORDENADA [{} : {}]`.

## 14. Distancia entre dos puntos

Crea dos `2-tupla` llamadas `punto_a` y `punto_b`.

Crea un menú para capturar los valores de cada punto `x` y `y`.

Agrega una opción para indicar la distancia entre ellos.

## 15. Polígono

Crea una lista vacía y un menú para agregar puntos.

Agrega una opción al menú para mostrar los puntos.

Agrega una opción al menú para mostrar el perímetro. El perímetro se calcula sumando la distancia entre sus puntos.

## 16. Contador de perros y gatos

Crea un diccionario con la clave `P` igual a 0 y la clave `G` igual a 0.

Agrega una opción para contar un perro (si escribe `P`) o contar un gato (si escribe `G`). Actualiza el diccionario en la clave correspondiente y muéstra el diccionario en el menú.

## 17. Contador de perros y gatos automático

Modifica el programa [*Contador de perros y gatos*].

Agrega una opción para leer una cadena de letras `P` y `G`. Incrementa los perros por cada `P` en la cadena y los gatos por cada `G`.

## 18. Robot

Crea un diccionario con las claves `x`, `y` y `angulo`.

Crea un menú con la opción de avanzar enfrente, retroceder hacía atrás , girar a la izquierda y girar a la derecha, y realiza los cálculos según las instrucciones.

> Actualizar la posición del robot

```text
Avanzar: 
    x_nueva = x + d * cos(a)
    y_nueva = y + d * sin(a)
Retroceder:
    x_nueva = x - d * cos(a)
    y_nueva = y - d * sin(a)
Girar izquierda:
    angulo_nuevo = angulo_anterior + radianes
Girar derecha:
    angulo_nuevo = angulo_anterior - radianes
```

Muestra en el menú la posición del robot y considera pedir los valores de distancia de desplazamiento o radianes a girar.

* Si puedes solicita grados y haz la conversión a radianes. Usa `import math`, `math.cos` y `math.sin`

## 19. Robot aleatorio

Modifica el programa [**Robot**] para agregar una opción que mueva aleatoriamente al robot, se debe determinar si girar o avanzar/retroceder.

Guarda en una lista las posiciones del robot en cada movimiento aleatorio.

## 20. Agenda

Crea un programa con menú que guarde una lista de diccionarios. Cada diccionario debe contener los datos de una persona.

> Ejemplo de los datos de un persona

```py
{
    "nombre": "Okia Ogul",
    "edad": 24,
    "telefono": "+525504526735",
    "direccion": {
        "calle": "Av. Siempre Viva",
        "num_ext": "123",
        "num_int": "Edif H 456",
        "delegacion": "Álvaro Obregón",
        "ciudad": "Ciudad de México",
        "pais": "México",
        "cp": "15950"
    }
}
```

Considera imprimir los datos en un forma similar al siguiente.

> Ejemplo de impresión de datos

```text
+---------------------------------------+
| Okia Ogul                  /  24 años |
+---------------------------------------+
| Teléfono:               +525504526735 |
+---------------------------------------+
| Dirección:                            |
| Av. Siempre Viva 123 (Edif H 456)     |
| Álvaro Obregón, Ciudad de México      |
| México                  / C.P.  15950 |
+---------------------------------------+
```
