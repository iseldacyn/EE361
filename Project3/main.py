from letterfrequency import *
from sortWords import *


def main():
    cipher = readFile('cipherText-project3.txt')

    # displays all 3-letter words
    words = cipher.split()
    threeLetter = sortWords(words, 3)
    # print(threeLetter)

    # sorts and displays letters by freq
    lf_cipher = letterFrequency(cipher)
    lf_cipher_list = list(lf_cipher.items())
    lf_cipher_list.sort(key=getFreq, reverse=True)
    # print(lf_cipher_list)

    # 'y' and 'a' are most freq
    # 'ybm' -> 'THE' , 'axh' -> 'AND' , 'atm' -> 'ARE'
    cipher = cipher.replace('y', 'T')
    cipher = cipher.replace('b', 'H')
    cipher = cipher.replace('m', 'E')
    cipher = cipher.replace('a', 'A')
    cipher = cipher.replace('x', 'N')
    cipher = cipher.replace('h', 'D')
    cipher = cipher.replace('t', 'R')

    # the plaintext was then printed to the screen using the code at the bottom of this function
    # from there, visual analysis was used to determine missing letters
    # 'THErE' -> 'THESE'
    cipher = cipher.replace('r', 'S')

    # 'STATEsENTS' -> 'STATEMENTS
    cipher = cipher.replace('s', 'M')
    # 'STiDENTS' -> 'STUDENTS'
    cipher = cipher.replace('i', 'U')

    # 'UNcvERScTw' -> 'UNIVERSITY'
    cipher = cipher.replace('c', 'I')
    cipher = cipher.replace('v', 'V')
    cipher = cipher.replace('w', 'Y')
    # 'REpUgATcfNS' -> 'REGULATIONS'
    cipher = cipher.replace('p', 'G')
    cipher = cipher.replace('g', 'L')
    cipher = cipher.replace('f', 'O')

    # 'uLARdSON' -> 'CLARKSON'
    cipher = cipher.replace('u', 'C')
    cipher = cipher.replace('d', 'K')
    # 'nOR' -> 'FOR'
    cipher = cipher.replace('n', 'F')
    # 'OoN' -> 'OWN'
    cipher = cipher.replace('o', 'W')
    # 'zENEnIT' -> 'BENEFIT'
    cipher = cipher.replace('z', 'B')
    # 'kORTIONS' -> 'PORTIONS'
    cipher = cipher.replace('k', 'P')

    plainText = ''
    for wrds in cipher:
        plainText += wrds
    print(plainText)


if __name__ == '__main__':
    main()
