import matplotlib.pyplot as plt
import seaborn as sns

personas = [
    {
        "peso": 60,
        "altura": 1.7
    },
    {
        "peso": 50,
        "altura": 1.6
    },
    {
        "peso": 70,
        "altura": 1.8
    },
    {
        "peso": 45,
        "altura": 1.5
    },
    {
        "peso": 56,
        "altura": 1.67
    },
    {
        "peso": 85,
        "altura": 1.62
    },
]

pesos = [ persona["peso"] for persona in personas ]

print("Pesos:", pesos)

sns.histplot(pesos, kde=True)

plt.savefig("g1.png")

plt.clf()

alturas = [ persona["altura"] for persona in personas ]

print("Alturas:", alturas)

sns.histplot(alturas, kde=True)

plt.savefig("g2.png")

plt.clf()

imc = [ persona["peso"] / persona["altura"] ** 2 for persona in personas ]

print("IMCs:", imc)

sns.histplot(imc)

plt.savefig("g3.png")

plt.clf()

sns.boxplot(imc)

plt.savefig("g4.png")

plt.clf()

figure, ax = plt.subplots()

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
bar1 = ax.bar(["Persona {}".format(i) for i in range(len(imc))], imc)

ax.bar_label(bar1, padding=3)

plt.savefig("g5.png")