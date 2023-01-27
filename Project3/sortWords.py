def getFreq(t):
    return t[1]  # return second item in the tuple


def sortWords(listOfWords, length):
    words = []
    for i in range(len(listOfWords)):
        notIn = True
        if len(listOfWords[i]) != length:
            continue
        for j in range(len(words)):
            if listOfWords[i] == words[j][0]:
                notIn = False
                words[j] = (words[j][0], words[j][1]+1)
                break
        if notIn:
            words.append((listOfWords[i], 1))
    words.sort(key=getFreq, reverse=True)
    return words
