import pandas as pd

edades = pd.Series([23, 34, 56, 32, 25, 17], name="Edades") # 6-Longitud

print(edades)

import matplotlib.pyplot as plt

plt.hist(edades)

plt.show()