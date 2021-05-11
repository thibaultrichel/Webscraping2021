import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(8, 10), dpi=80)

df = pd.read_csv('./dftest.csv', sep=',')

dates = df['Date'].iloc[::-1]
nbCases = df['NbCases'].iloc[::-1]
nbDeaths = df['NbDeaths'].iloc[::-1]
barrelPrice = df['BarrelPrice'].iloc[::-1]
newsTitles = df['News Titles'].iloc[::-1]

datesWithNews = [date for i, date in enumerate(dates.values) if type(newsTitles.values[i]) != float]
datesWithNews = [str(datesWithNews[i]) for i in range(len(datesWithNews)) if i % 5 == 0]
barrelPriceWithNews = [price for i, price in enumerate(barrelPrice.values) if type(newsTitles.values[i]) != float]
barrelPriceWithNews = [barrelPriceWithNews[i] for i in range(len(barrelPriceWithNews)) if i % 5 == 0]
newsTitlesOk = [title for i, title in enumerate(newsTitles) if type(newsTitles.values[i]) != float]
newsTitlesOk = [newsTitlesOk[i] for i in range(len(newsTitlesOk)) if i % 5 == 0]

# graph nb de cas
ax1 = plt.subplot(2, 1, 1)
ax1.grid(zorder=0, linestyle='--')
plt.bar(dates, nbCases, label='Nombre de cas de COVID-19', zorder=3)
ax1.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.ylabel('Nombre de cas (cumul)')
plt.setp(ax1.get_xticklabels(), visible=False)
plt.xticks(np.arange(0, len(dates), 20), rotation='vertical')
plt.legend()

# graph nb de décès
ax2 = plt.subplot(2, 1, 2)
plt.bar(dates, nbDeaths, label='Nombre de décès')
plt.grid(linestyle='--')
plt.ylabel('Nombre de décès (cumul)')
# plt.setp(ax2.get_xticklabels(), visible=False)
plt.xticks(np.arange(0, len(dates), 20), rotation='vertical')
plt.legend()

# graph prix du baril
fig, ax = plt.subplots()
pl = plt.plot(dates, barrelPrice, label='Prix du baril')
sc = plt.scatter(datesWithNews, barrelPriceWithNews, color='r')
plt.grid(linestyle='--')
plt.xlabel('Dates')
plt.ylabel('Prix du baril en €')
plt.xticks(np.arange(0, len(dates), 20), rotation='vertical')
plt.legend()

annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)


def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}: {}".format(" ".join([datesWithNews[n] for n in ind["ind"]]),
                           " ".join([newsTitlesOk[n] for n in ind["ind"]]))
    annot.set_text(text)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", hover)


def showPlots():
    plt.show()
