def daysLessSpam(data):
    bestDay = {}
    j = 0
    for i in data["Date"]:
        d = i[8:-9]  # day
        m = i[5:-12]  # month
        if(m not in bestDay):  # new month
            counter = 0
            best = 0
            previous = int(d)
            bestDay[m] = 0
        if(data["IsSpam"][j] == "no" and d == previous):
            counter += 1
        elif(data["IsSpam"][j] == "no"):
            counter = 1
        else:
            counter = 0
        if(counter > best):
            best = counter
            bestDay[m] = d
        previous = d
        j += 1
    for i in bestDay:
        print("Mês " + str(i) + ": dia " + str(bestDay[i]) + "\n")
