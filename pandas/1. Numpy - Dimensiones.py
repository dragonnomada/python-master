import numpy as np

# N Dimensional Array
# Arreglo de datos con N elementos
x = np.array([1, 2, 3, 4, 5]) # 5 (1-EJE edades)

# Figura de NDArray -> Dimensión (Ejes / Longitud)

print(x.shape) # (5,) 1-EJE (1-tupla) 5-Longitud

A = np.array([
  [1, 2, 3],     # Fila 1 (índice 0)
  [4, 5, 6],     # Fila 2 (índice 1)
  [7, 8, 9],     # Fila 3 (índice 2)
  [10, 11, 12],  # Fila 4 (índice 3)
]) # 4 x 3 | 2E (4, 3) (2-EJES edades, pesos, alturas)

print(A.shape) # (4, 3) 2-EJES (2-tupla) 4-Longitud, 3-Longitud

T = np.array([
  [[255, 0, 127], [0, 255, 98]],
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]],
  [[0, 0, 0], [0, 0, 0]]
]) # 7 x 2 x 3 | 3E (7, 2, 3) (3-EJES imágenes)

print(T.shape) # (7, 2, 3)

# 768 x 1280 x 3 (Imagen de 1280x768)