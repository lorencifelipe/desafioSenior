import numpy as np
import readSenior as r
import statistics as st
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def model(train, trainLabels, test):
    # Model
    mnb = MultinomialNB()
    # Training the model
    mnb.fit(train, trainLabels)
    # Predicting with test set
    result = mnb.predict(test)
    return(result)


def main():
    data = r.read("/sms_senior.csv")  # Read file
    isSpam = np.array(data['IsSpam'])  # Select column IsSpam
    words = list(data.columns)[1:-4]  # Select the columns names (words)
    # Select the words freqs for each e-mail
    wordsFreqs = np.array(data[words])
    accuracies = []  # List to store accuracies

    # Test for 50 different seeds
    for seed in range(1, 51):
        # Prepare train/test sets
        train, test, trainLabels, testLabels = train_test_split(
            wordsFreqs, isSpam, test_size=0.3, random_state=seed)
        result = model(train, trainLabels, test)
        accuracies.append(accuracy_score(testLabels, result))
    print(st.mean(accuracies))  # Accuracies mean


main()
