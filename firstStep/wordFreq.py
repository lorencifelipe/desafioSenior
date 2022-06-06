# Return a dictionary with frequencies to each word
def wordsFreq(data):
    wordFreq = {}
    header = list(data.columns)
    for col in header[1:-4]:
        wordFreq[col] = int(data[col].sum())
    return(wordFreq)
