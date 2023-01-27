# finds a keyword in a text file and prints out the first word before, and after the keyword
# comments given within function definition
def findContext(keyword, file):
    # reads in words from the text file into a list
    content = []
    for line in file:
        for word in line.split():
            content.append(word)

    # finds the location of the keyword within the text file and stores it for later use
    location = []
    for i in range(len(content)):
        if content[i] == keyword:
            location.append(i)
    # prints an error message if the keyword is not in the file
    if not location:
        print("Error: keyword not in file")
        return

    # stores the keyword and its context into a list
    instance = []
    for i in range(len(location)):
        # if the keyword is the first word, append two blank characters to the list
        # if the keyword is the second word, append one blank character and the first word of the file
        # else, append the two words before the keyword
        # the blank characters are used later to print out the list easier
        if location[i] > 0:
            if location[i] > 1:
                instance.append(content[location[i]-2])
            else:
                instance.append('')
            instance.append(content[location[i]-1])
        else:
            instance.append('')
            instance.append('')

        # add the keyword to the list
        instance.append(content[location[i]])

        # if the keyword is the last word, append two blank characters to the list
        # if the keyword is the second to last word, append a blank character and the last word of the file
        # else, append the two words after the keyword
        # the blank characters serve the same function as they did before
        if location[i] < len(content) - 1:
            instance.append(content[location[i]+1])
            if location[i] < len(content) - 2:
                instance.append(content[location[i]+2])
            else:
                instance.append('')
        else:
            instance.append('')
            instance.append('')

    # since this must be stored as a dictionary, the list is then converted to a dictionary
    # first, the instance list is converted to a list of strings
    context = []
    temp = ""
    for i in range(len(instance)//5):
        for j in range(5):
            temp += instance[i*5+j]
            # add a space to the context if the character is neither blank nor the last sequence of 5
            if instance[i*5+j] != '':
                if j == 4:
                    continue
                temp += ' '
        context.append(temp)
        temp = ""

    # converts the list of contexts to a dictionary
    dict = {}
    for i in range(len(context)):
        dict.update({i: context[i]})

    # prints out the context of the keyword
    for i in range(len(location)):
        print(dict[i])
    return context


# tests findContext function with different examples
def main():
    # TEST 1: "example.txt"
    # uses the first paragraph of the project description with keyword "keyword"
    # mainly use for a test purpose

    # TEST 2: "first last.txt
    # contains a single sentence and uses the keyword "there"
    # this is used to test the first word and last word case of the file

    # TEST 3: "pg10.txt"
    # uses the attached file on the Moodle page with keyword "LORD"
    # used to test a file with many instances of the same keyword (i.e. a large file)

    # all outputs are attached in "Outputs.txt"

    # creates a dictionary of keywords
    keywords = {}

    # reads in the file and asks for user input
    # if the input is Q, the program terminates
    while True:
        file = open('first last.txt', 'r')
        print('Input a keyword to find')
        keyword = input()
        if keyword == 'Q':
            break
        # prints keyword context and adds it to a dictionary
        context = findContext(keyword, file)
        keywords.update({keyword: context})
        file.close()

    # prints the dictionary of keywords asked for
    print(keywords)


# runs main function
if __name__ == '__main__':
    main()
