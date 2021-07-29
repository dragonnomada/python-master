import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Ana", "Beto", "Carla", "Daniel", "Edna"],
    "Peso": [50, 67, 78, 59, 63],
    "Estatura": [1.56, 1.72, 1.70, 1.57, 1.45]
})

# Calcular la columna del IMC

# Creamos una nueva columna llamada IMC con la operación entre las otras dos columnas (Peso, Estatura)
df["IMC"] = df["Peso"] / df["Estatura"] ** 2

# Calcular la columna Etiqueta

# Definimos una función que transforme un valor de imc (ejemplo 20.5456 en "PESO NORMAL")
def imc_to_etiqueta(imc):
    if imc < 16:
        return "BAJO PESO"
    if imc >= 16 and imc < 21:
        return "PESO NORMAL"
    if imc >= 21 and imc < 26:
        return "SOBRE PESO"
    return "ALTO PESO"

# Creamos una nueva columna llamada Etiqueta que resulte a partir de transformar la columna IMC
# usando la función `imc_to_etiqueta`
df["Etiqueta"] = df["IMC"].map(imc_to_etiqueta)

print(df)

# Corrige los rangos de acuardo a:

# El IMC (Kg/m2) tiene 5 categorías de acuerdo a un rango 
# Bajo de peso = menor a 18.5 ; 
# Normal = 18.5 a 24.9 ; 
# Sobrepeso = 25 a 29.9; 
# Obesidad grado I = 30 -24.9; 
# Obesidad Grado II = 35 - 39.9
# Obesidad Grado III = más de 40. 
# Algunos agregan una categoría 6 o Superobesidad cuando están en 60 IMC

