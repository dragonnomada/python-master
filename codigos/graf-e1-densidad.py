import seaborn as sns
import matplotlib.pyplot as plt

serie = [28, 23, 25, 34, 33, 30, 19, 17, 23, 45, 29]
serie_h = [28, 34, 33, 30, 19, 29]
serie_m = [23, 25, 19, 17, 23, 45]

# sns.histplot(serie, bins=8)
sns.kdeplot(serie, shade=True, color="purple")
sns.kdeplot(serie_h, shade=True, color="cornflowerblue")
sns.kdeplot(serie_m, shade=True, color="hotpink")

plt.show()