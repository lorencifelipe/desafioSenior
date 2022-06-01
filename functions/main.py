import readSenior as r
import generateCloud as c
import wordFreq as w

def main():
    data = r.read("/sms_senior.csv") 
    wf = w.wordsFreq(data) 
    c.cloud(wf) #First Step, Pt. 1

main()
