def daysLessSpam(data):
    bestDays = {}
    months = data["Date"].dt.month.unique()
    for m in months:
        best = 0
        days = data.query("Date.dt.month == @m")["Date"].dt.day.unique()
        for d in days:
            counter = 0
            spamsDaily = data.query(
                "Date.dt.month == @m & Date.dt.day == @d")["IsSpam"]
            for mail in spamsDaily:
                if(mail == "no"):
                    counter += 1
                else:
                    counter = 0
                if(counter > best):
                    best = counter
                    bestDays[m] = d
    for i in bestDays:
        print("Mês " + str(i) + ": dia " + str(bestDays[i]) + "\n")
