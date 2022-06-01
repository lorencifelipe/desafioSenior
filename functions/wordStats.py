import statistics as st

def wordCountStats(data):
    stats = {}
    wordsMonth = {}
    j = 0
    for i in data["Date"]:
        m = i[5:-12]  # month
        if(m not in wordsMonth):
            stats[m] = {}
            wordsMonth[m] = []
        wordsMonth[m].append(data["Word_Count"][j])
        j += 1
    for i in wordsMonth:
        stats[i]["Max"] = max(wordsMonth[i])
        stats[i]["Min"] = min(wordsMonth[i])
        stats[i]["Media"] = st.fmean(wordsMonth[i])
        stats[i]["Mediana"] = st.median(wordsMonth[i])
        stats[i]["Desvio"] = st.pstdev(wordsMonth[i])
        stats[i]["Variancia"] = st.variance(wordsMonth[i])
    for i in wordsMonth:
        print("Mês " + str(i) + ":")
        for j in stats[i]:
            print(str(j) + " = " + str(stats[i][j]))
        print("\n")
