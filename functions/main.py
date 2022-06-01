import readSenior as r
import generateCloud as c
import wordFreq as w
import traceMonthGraph as t

def main():
    data = r.read("/sms_senior.csv")  # Read file
    wf = w.wordsFreq(data) #Word frequences
    c.genCloud(wf) #First Step, Pt. 1
    t.spamsMonthly(data) #First Step, Pt. 2


main()
