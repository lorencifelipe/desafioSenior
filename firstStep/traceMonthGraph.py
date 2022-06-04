import matplotlib.pyplot as plt
import numpy as np
import os

MONTHS = {"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril", "05": "Maio", "06": "Junho",
          "07": "Julho", "08": "Agosto", "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"}


def percent(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} e-mails)".format(pct, absolute)


def graphMonth(month, spam, notSpam, dir):
    labels = ["É spam", "Não é spam"]
    c = ["#B22222", "#4169E1"]
    data = [spam, notSpam]
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(
        data, autopct=lambda pct: percent(pct, data), textprops=dict(color="w"), colors=c, shadow=True, explode=(0.1, 0))
    ax.legend(wedges, labels, title="Classificação",
              loc="lower left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title("Classificação de e-mails no mês de " + MONTHS[month])
    plt.subplots_adjust(top=0.929,
                        bottom=0.028,
                        left=0.02,
                        right=0.907,
                        hspace=0.2,
                        wspace=0.2)
    if not os.path.exists(dir+"/graphics"):
        os.makedirs("graphics")
    os.chdir(dir+"/graphics")
    if not os.path.isfile(dir+"/graphics/"+month+".png"):
        plt.savefig(month+".png")
    os.chdir(dir+"/..")
   # plt.show()


def filterMonthly(data):
    spamMonths = {}
    j = 0
    for i in data["Date"]:
        m = i[5:-12]  # month
        isSpam = data["IsSpam"][j]  # Is spam?
        if(m not in spamMonths):
            spamMonths[m] = {}
            spamMonths[m]["spam"] = 0
            spamMonths[m]["notSpam"] = 0
        if(isSpam == "yes"):
            spamMonths[m]["spam"] += 1
        else:
            spamMonths[m]["notSpam"] += 1
        j += 1
    return(spamMonths)


def spamsMonthly(data):
    dir = os.getcwd()
    spamMonths = filterMonthly(data)
    for month in spamMonths:
        graphMonth(month, spamMonths[month]["spam"],
                   spamMonths[month]["notSpam"], dir)
