import pandas as pd

# usecols="<start>:<end>" | "<col>:<col>,<col>:<col>,<col>,..."
df = pd.read_excel("data/Analisis-IMC.xlsx", sheet_name="Hoja2", engine="openpyxl", usecols="B:F", skiprows=3)

print(df)