import pandas as pd

# Creamos un dataframe a partir de un diccionario de listas
# Cada clave será el nombre de la columna
# Y cada lista serán los valores para cada fila en la columna
df = pd.DataFrame({
    "Nombre": ["Ana", "Beto", "Carla", "Eduardo"],
    "Edad": [23, 45, 67, 98],
    "Peso": [45, 78, 56, 60]
})

print(df)
#     Nombre  Edad  Peso
# 0      Ana    23    45
# 1     Beto    45    78
# 2    Carla    67    56
# 3  Eduardo    98    60

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3        
# Data columns (total 3 columns):      
#  #   Column  Non-Null Count  Dtype   
# ---  ------  --------------  -----   
#  0   Nombre  4 non-null      object  
#  1   Edad    4 non-null      int64
#  2   Peso    4 non-null      int64
# dtypes: int64(2), object(1)
# memory usage: 224.0+ bytes

print(df.describe())
#            Edad       Peso
# count   4.00000   4.000000
# mean   58.25000  59.750000
# std    32.01432  13.720423
# min    23.00000  45.000000
# 25%    39.50000  53.250000
# 50%    56.00000  58.000000
# 75%    74.75000  64.500000
# max    98.00000  78.000000

# 1. Obtener los valores de una columna

print(df["Nombre"]) # Serie Nombre
# 0        Ana
# 1       Beto
# 2      Carla
# 3    Eduardo
# Name: Nombre, dtype: object
print(df["Edad"])   # Serie Edad
# 0    23
# 1    45
# 2    67
# 3    98
# Name: Edad, dtype: int64
print(df["Peso"])   # Serie Peso
# 0    45
# 1    78
# 2    56
# 3    60
# Name: Peso, dtype: int64

# 2. Agregar una columna con operaciones entre otras columnas

df["Fuerza"] = 10 * df["Peso"] / df["Edad"] # Operación: Registro por registro

# Alternar comentarios VC: CTRL + }

print(df)
#     Nombre  Edad  Peso     Fuerza
# 0      Ana    23    45  19.565217
# 1     Beto    45    78  17.333333
# 2    Carla    67    56   8.358209
# 3  Eduardo    98    60   6.122449

# 3. Obtener los valores de una fila (un registro)

print(df.iloc[1]) # Registro de Beto ("Beto", 45, 78, 1.7333)
# Nombre       Beto
# Edad           45
# Peso           78
# Fuerza    17.3333
# Name: 1, dtype: object

# 4. Obtener el dataframe transpuesto (Columnas <-> Filas)

print(df.T)
#               0        1        2        3
# Nombre      Ana     Beto    Carla  Eduardo
# Edad         23       45       67       98
# Peso         45       78       56       60
# Fuerza  19.5652  17.3333  8.35821  6.12245

# 5. Obtener los valores de una fila mediante el dataframe transpuesto

print(df.T[1]) # Registro de Beto ("Beto", 45, 78, 1.7333)
# Nombre       Beto
# Edad           45
# Peso           78
# Fuerza    17.3333
# Name: 1, dtype: object