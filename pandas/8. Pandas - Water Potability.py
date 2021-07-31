import pandas as pd

df = pd.read_excel("data/Analisis-IMC.xlsx", sheet_name="Hoja4", usecols="A:J", skiprows=0, engine="openpyxl")

print(df)

df["Efecto1"] = df["Hardness"] / df["Solids"] * df["Turbidity"]

print(df)

df3 = pd.DataFrame({
    "PH": df["ph"],
    "Dureza": df["Hardness"],
    "Solidos": df["Solids"]
})

print(df3)

import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(df3)

plt.show()

# plt.savefig("gx.png")