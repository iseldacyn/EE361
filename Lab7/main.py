from letterfrequency import *
from checkword import *

# Decrypts the cipher text, all print() statements are commented out for running purposes
def main():
    # Read in the file and print letter frequency
    plain = readFile('wells.txt')
    lf_plain = letterFrequency(plain)
    cipher = readFile('cipherText.txt')
    lf_cipher = letterFrequency(cipher)
    lf_plain_list = list(lf_plain.items())
    lf_plain_list.sort(key=getFreq)
    # print(lf_plain_list)
    lf_cipher_list = list(lf_cipher.items())
    lf_cipher_list.sort(key=getFreq)
    # print(lf_cipher_list)

    # Print frequency of neighboring letters
    pf_plain = neighborCount(plain)
    pf_cipher = neighborCount(cipher)
    # print(pf_plain)
    # print(pf_cipher)

    # Find E <- l and A <- h from neighboring freq
    cipher = cipher.replace('l', 'E')
    cipher = cipher.replace('h', 'A')

    # Print out each word in text and replace letters for common words
    # i.e. kuE -> THE, Abe -> AND
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)
    cipher = cipher.replace('k', 'T')
    cipher = cipher.replace('u', 'H')
    cipher = cipher.replace('b', 'N')
    cipher = cipher.replace('e', 'D')

    # AiiInAL -> ARRIVAL, ex from book
    unused = 'bcjkmpqruvwxyz'
    # print(findLetters(unused,'AiilnAL'))
    cipher = cipher.replace('i', 'R')
    cipher = cipher.replace('n', 'V')
    unused = 'bcjkmpquwxyz'

    # wcaacN -> COMMON
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)
    # print(findLetters(unused, 'wcaacN'))
    cipher = cipher.replace('w', 'C')
    cipher = cipher.replace('c', 'O')
    cipher = cipher.replace('a', 'M')

    # Uses letter analysis for some more common words
    # i.e. -vNt -> -ING, -j -> -S, REMEMgER -> REMEMBER
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)
    cipher = cipher.replace('v', 'I')
    cipher = cipher.replace('t', 'G')
    cipher = cipher.replace('j', 'S')
    cipher = cipher.replace('g', 'B')

    # xmST -> MUST, ONzq -> ONLY (C and E already mapped), sROM -> FROM
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)
    cipher = cipher.replace('x', 'M')
    cipher = cipher.replace('m', 'U')
    cipher = cipher.replace('z', 'L')
    cipher = cipher.replace('q', 'Y')
    cipher = cipher.replace('s', 'F')

    # AddEARANCE -> APPEARANCE, oNDERFULLY -> WONDERFULLY, BREErE -> BREEZE
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)
    cipher = cipher.replace('d', 'P')
    cipher = cipher.replace('o', 'W')
    cipher = cipher.replace('r', 'Z')

    # Checks all words are decrypted
    words = cipher.split()
    words.sort(key=sortByLen)
    # print(words)

    # Prints the decrypted cipher text
    print(cipher)

if __name__ == '__main__':
    main()
