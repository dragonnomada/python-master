import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "manzanas": [30, 40, 25, 28],
    "peras": [35, 36, 32, 38],
    "kiwis": [28, 48, 54, 45],
}

import pandas as pd

df = pd.DataFrame(data)

print(df)

sns.heatmap(df)

plt.show()