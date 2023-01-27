from pydoc import plain
import re


# finds the indices of a given value in a 2x2 array
def find(val, array):
  for i in range(len(array)):
    for j in range(len(array[i])):
      if array[i][j] == val:
        return [i, j]
# converts an array of chars to a string
def arrtostr(array):
  plainText = ""
  for i in range(len(array)):
    plainText += array[i][0]
    plainText += array[i][1]
  return plainText
# generates the key table from a given string of chars
def findKey(key):
  # eliminates whitespace from key
  key = re.sub(r"\s+", "", key, flags=re.UNICODE)

  # initializes variables
  key = key.replace("j", "")
  newKey = []
  temp = []
  alpha = 'abcdefghiklmnopqrstuvwxyz'

  # while key is not empty, add char of key[0] to temp
  # remove char from key and alpha
  # repeat for alpha
  # if temp is > 5, add to key table as new roll
  while key:
    temp.append(key[0])
    alpha = alpha.replace(key[0], "")
    key = key.replace(key[0], "")
    if len(temp) == 5:
      newKey.append(temp)
      temp = []
  while alpha:
    temp.append(alpha[0])
    alpha = alpha.replace(alpha[0], "")
    if len(temp) == 5:
      newKey.append(temp)
      temp = []
  return newKey


# encrypts and decrypts plaintext using playfair cypher
# the encrypt function first generates a dictionary of lists containing pairs of the plain text chars
# the key is then generated from the findKey function
# using the rules for the cipher algorithm, the pairs of chars is then converted to the cipher text
# using the "playfair example" key
# rules of the playfair cipher can be found at https://en.wikipedia.org/wiki/Playfair_cipher#Description
# the pairs are then converted back to a string as the cipher text
def playfairEncrypt(plainText):
  # removes whitespace from plaintext and initiaizes vars
  plainText = re.sub(r"\s+", "", plainText, flags=re.UNICODE)
  pairs = []
  n = 0
  x = len(plainText) // 2
  key = findKey('playfair example')

  # converts plain text to pair of chars
  if len(plainText) % 2 == 0:
    x += 1
  for i in range(x):
    if n == len(plainText) - 1:
      pairs.append([plainText[n], 'x'])
      n += 1
    elif plainText[n] == plainText[n + 1]:
      pairs.append([plainText[n], 'x'])
      n += 1
    else:
      pairs.append([plainText[n], plainText[n + 1]])
      n += 2

  # generates cipher text from pairs of chars and key table
  # follows rules provided to created cipher text
  for i in range(len(pairs)):
    a = find(pairs[i][0], key)
    b = find(pairs[i][1], key)
    if a[0] == b[0]:
      a[1] += 1
      b[1] += 1
      if a[1] == 5:
        a[1] = 0
      if b[1] == 5:
        b[1] = 0
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    elif a[1] == b[1]:
      a[0] += 1
      b[0] += 1
      if a[0] == 5:
        a[0] = 0
      if b[0] == 5:
        b[0] = 0
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    else:
      pairs[i][0] = key[a[0]][b[1]]
      pairs[i][1] = key[b[0]][a[1]]
  # converted new pairs of chars to a string and return
  plainText = arrtostr(pairs)
  return plainText

# the decrypt function first regenerates the key and converts the cipher text to pairs of chars
# the reverse algorithm is then applied to the pairs of chars, decoding the cipher text back to the plain text
# the pairs of chars are converted back to a string and returned to the user as the plain text
# the returned plain text does not include any white space and has added 'x's to the text, however
def playfairDecrypt(cipherText):
  # initializes vars
  pairs = []
  n = 0
  key = findKey('playfaire example')

  # converts cipher text to pairs of chars
  for i in range(len(cipherText) // 2):
    if (cipherText[n] == cipherText[n + 1]) | (n + 1 == len(cipherText)):
      pairs.append([cipherText[n], 'x'])
      n += 1
    else:
      pairs.append([cipherText[n], cipherText[n + 1]])
      n += 2

  # decodes to plain text through opposite process of generating cipher text
  for i in range(len(pairs)):
    a = find(pairs[i][0], key)
    b = find(pairs[i][1], key)
    if (a[0] != b[0]) & (a[1] != b[1]):
      pairs[i][0] = key[a[0]][b[1]]
      pairs[i][1] = key[b[0]][a[1]]
    elif a[1] == b[1]:
      a[0] -= 1
      b[0] -= 1
      if a[0] == -1:
        a[0] = 4
      if b[0] == -1:
        b[0] = 4
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    if a[0] == b[0]:
      a[1] -= 1
      b[1] -= 1
      if a[1] == -1:
        a[1] = 4
      if b[1] == -1:
        b[1] = 4
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
  # converts back to a string and returns it
  cipherText = arrtostr(pairs)
  return cipherText


# uses playfair cypher and generates key from a given string
# uses the same process as traditional playfairEncrypt and playfairDecrypt
def playfairSpecialEncrypt(plainText, key):
  plainText = re.sub(r"\s+", "", plainText, flags=re.UNICODE)
  pairs = []
  n = 0
  x = len(plainText) // 2
  if len(plainText) % 2 == 0:
    x += 1
  for i in range(x):
    if n == len(plainText) - 1:
      pairs.append([plainText[n], 'x'])
      n += 1
    elif plainText[n] == plainText[n + 1]:
      pairs.append([plainText[n], 'x'])
      n += 1
    else:
      pairs.append([plainText[n], plainText[n + 1]])
      n += 2
  key = findKey(key)
  for i in range(len(pairs)):
    a = find(pairs[i][0], key)
    b = find(pairs[i][1], key)
    if a[0] == b[0]:
      a[1] += 1
      b[1] += 1
      if a[1] == 5:
        a[1] = 0
      if b[1] == 5:
        b[1] = 0
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    elif a[1] == b[1]:
      a[0] += 1
      b[0] += 1
      if a[0] == 5:
        a[0] = 0
      if b[0] == 5:
        b[0] = 0
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    else:
      pairs[i][0] = key[a[0]][b[1]]
      pairs[i][1] = key[b[0]][a[1]]
  plainText = arrtostr(pairs)
  return plainText

def playfairSpecialDecrypt(cipherText, key):
  pairs = []
  n = 0
  for i in range(len(cipherText) // 2):
    if (cipherText[n] == cipherText[n + 1]) | (n + 1 == len(cipherText)):
      pairs.append([cipherText[n], 'x'])
      n += 1
    else:
      pairs.append([cipherText[n], cipherText[n + 1]])
      n += 2
  key = findKey(key)
  for i in range(len(pairs)):
    a = find(pairs[i][0], key)
    b = find(pairs[i][1], key)
    if (a[0] != b[0]) & (a[1] != b[1]):
      pairs[i][0] = key[a[0]][b[1]]
      pairs[i][1] = key[b[0]][a[1]]
    elif a[1] == b[1]:
      a[0] -= 1
      b[0] -= 1
      if a[0] == -1:
        a[0] = 4
      if b[0] == -1:
        b[0] = 4
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
    if a[0] == b[0]:
      a[1] -= 1
      b[1] -= 1
      if a[1] == -1:
        a[1] = 4
      if b[1] == -1:
        b[1] = 4
      pairs[i][0] = key[a[0]][a[1]]
      pairs[i][1] = key[b[0]][b[1]]
  cipherText = arrtostr(pairs)
  return cipherText


# tests different cases of plain text and keys for the different algorithms
def main():
  # tests playfair encrypt and decrypt with various keys and plain texts
  plainText = 'hello world'
  cipherText = playfairEncrypt(plainText)
  print(cipherText)
  plainText = playfairDecrypt(cipherText)
  print(plainText)

  plainText = 'this is a different plain text'
  cipherText = playfairEncrypt(plainText)
  print(cipherText)
  plainText = playfairDecrypt(cipherText)
  print(plainText)

  plainText = 'hello world'
  key = 'this is a special key'
  cipherText = playfairSpecialEncrypt(plainText, key)
  print(cipherText)
  plainText = playfairSpecialDecrypt(cipherText, key)
  print(plainText)

  plainText = 'this is a different plain text'
  key = 'this is a special key'
  cipherText = playfairSpecialEncrypt(plainText, key)
  print(cipherText)
  plainText = playfairSpecialDecrypt(cipherText, key)
  print(plainText)

  plainText = 'hello world with a different key'
  key = 'this is a different key'
  cipherText = playfairSpecialEncrypt(plainText, key)
  print(cipherText)
  plainText = playfairSpecialDecrypt(cipherText, key)
  print(plainText)

  plainText = 'this is a different plain text with a different key'
  key = 'this is a different key'
  cipherText = playfairSpecialEncrypt(plainText, key)
  print(cipherText)
  plainText = playfairSpecialDecrypt(cipherText, key)
  print(plainText)


# runs main function
if __name__ == '__main__':
  main()
