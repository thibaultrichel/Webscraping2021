import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import mplcursors

figure(figsize=(8, 10), dpi=80)

df = pd.read_csv('dftest.csv', sep=',')

dates = df['Date'].iloc[::-1]
nbCases = df['NbCases'].iloc[::-1]
nbDeaths = df['NbDeaths'].iloc[::-1]
barrelPrice = df['BarrelPrice'].iloc[::-1]
newsTitles = df['news Titles'].iloc[::-1]



#plt.title('prix baril')

# graph nb de cas
ax1 = plt.subplot(3, 1, 1)
plt.bar(dates, nbCases, label='Nombre de cas de COVID-19')
plt.ylim(4000000)
plt.ylabel('nombre de cas')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.legend()
#plt.title('nb de cas de COVID-19')
#plt.show()



# graph nb de décès
ax2 = plt.subplot(3, 1, 2)
plt.plot(dates, nbDeaths, label='Nombre de décès', )

plt.ylabel('nombre de décès')
plt.setp(ax2.get_xticklabels(), visible=False)
plt.legend()
#plt.title('nb de decès')
#plt.show()

# graph prix du baril
ax3 = plt.subplot(3, 1, 3)
plt.plot(dates, barrelPrice, label='Prix du baril')
plt.xlabel('Dates')
plt.ylabel('prix baril en $')
plt.xticks(dates, rotation='vertical')
plt.setp(ax3.get_xticklabels(), visible=True)
plt.legend()


mplcursors.cursor(hover=True)
plt.show()
