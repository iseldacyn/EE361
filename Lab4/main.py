def removeChar(string, idx):
    return string[:idx] + string[idx + 1:]
def removeDupes(myString):
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr
def removeMatches(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def genKeyFromPass(password):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    password = password.lower()
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = alphabet.find(lastChar)
    afterString = removeMatches(alphabet[lastIdx + 1:], password)
    beforeString = removeMatches(alphabet[:lastIdx], password)
    key = password + afterString + beforeString
    return key
def keyGen():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    key = ""
    for i in range(len(alphabet) - 1, -1, -1):
        idx = random.randint(0, i)
        key = key + alphabet[idx]
        alphabet = removeChar(alphabet, idx)
    return key

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText
def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

def scramble2EncryptMod(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = evenChars + oddChars
    return cipherText
def scramble2DecryptMod(cipherText):
    if len(cipherText) % 2 == 0:
        halfLength = len(cipherText) // 2
    else:
        halfLength = (len(cipherText) + 1) // 2
    evenChars = cipherText[:halfLength]
    oddChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        if i < len(oddChars):
            plainText = plainText + oddChars[i]

    return plainText

def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
def substitutionDecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = key.find(ch)
        plainText = plainText + alphabet[idx]
    return plainText

def isPalindrome(s):
    sr = s[::-1]
    pal = True
    for i in range(len(s)):
        if s[i]!=sr[i]:
            pal = False
    return pal

myPassword = "this is a transposition cypher"
myPassword = scramble2Encrypt(myPassword)
myPassword = scramble2Decrypt(myPassword)

myPassword = "this is an even cypher"
myPassword = scramble2EncryptMod(myPassword)
myPassword = scramble2DecryptMod(myPassword)

myPassword = "this is an odd cypher"
myPassword = scramble2EncryptMod(myPassword)
myPassword = scramble2DecryptMod(myPassword)

myPassword = "this is a substitution cypher"
myKey = genKeyFromPass(myPassword)
myPassword = substitutionEncrypt(myPassword, myKey)
myPassword = substitutionDecrypt(myPassword, myKey)

myPassword = "this is a substitution cypher"
myPassphrase = "this will generate a key"
myKey = genKeyFromPass(myPassphrase)
myPassword = substitutionEncrypt(myPassword, myKey)
myPassword = substitutionDecrypt(myPassword, myKey)

truePalin = isPalindrome("racecar")
falsePalin = isPalindrome("race car")