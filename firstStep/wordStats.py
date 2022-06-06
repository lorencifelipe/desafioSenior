import pandas as pd

def wordCountStats(data):
    stats = {}
    wordCountMonths = {}
    months = data["Date"].dt.month.unique()
    for m in months:
        wordCountMonths[m] = data.query("Date.dt.month == @m").Word_Count
    for m in wordCountMonths:
        stats[m] = {}
        stats[m]["Max"] = wordCountMonths[m].max()
        stats[m]["Min"] = wordCountMonths[m].min()
        stats[m]["Media"] = wordCountMonths[m].mean()
        stats[m]["Mediana"] = wordCountMonths[m].median()
        stats[m]["Desvio"] = wordCountMonths[m].std()
        stats[m]["Variancia"] = wordCountMonths[m].var()
    for m in months:
        print("Mês " + str(m) + ":")
        for j in stats[m]:
            print(str(j) + " = " + str(stats[m][j]))
        print("\n")
