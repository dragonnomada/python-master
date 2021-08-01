import matplotlib.pyplot as plt

labels = ["Cocina", "Dormitorio", "Jardín"]
sizes = [60, 25, 32]
colors = ["crimson", "lime", "indigo"]

plt.pie(sizes, labels=labels, colors=colors)

figure = plt.gcf()

figure.gca().add_artist(plt.Circle( (0,0), 0.7, color="white"))

plt.show()