import seaborn as sns
import matplotlib.pyplot as plt

manzanas = [60, 64, 67, 55, 63, 64, 62]
peras = [44, 48, 43, 46, 44, 47, 55]
kiwis = [23, 24, 33, 28, 21, 23, 27]

import pandas as pd

df = pd.DataFrame({ "manzanas": manzanas, "peras": peras, "kiwis": kiwis, "e1": manzanas, "e2": manzanas, "e3": manzanas })

sns.boxplot(data=df.loc[:, ['manzanas', 'peras', 'kiwis', "e1", "e2", "e3"]])

plt.show()