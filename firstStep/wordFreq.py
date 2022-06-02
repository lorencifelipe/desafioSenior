#Return a dictionary with frequencies to each word 
def wordsFreq(data):
    wordFreq = {}
    for header in data:
        if(header != "Full_Text" and header != "Common_Word_Count" and header != "Word_Count" and header != "Date" and header != "IsSpam"):
            wordFreq[header] = int(data[header].sum())
    return(wordFreq)
