import pandas as pd

df = pd.read_excel("data/Analisis-IMC.xlsx", sheet_name="Hoja1", engine="openpyxl")

print(df)