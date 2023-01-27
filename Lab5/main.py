import turtle


def frequencyChart(aList):
    countDict = {}

    for item in aList:  # generate dictionary of counts
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1

    itemlist = list(countDict.keys())  # get list of keys
    minitem = 0
    maxitem = len(itemlist) - 1

    countlist = countDict.values()  # get list of counts
    maxcount = max(countlist)

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1, -1, maxitem + 1, maxcount + 1)
    chartT.hideturtle()
    chartT.up()  # draw baseline
    chartT.goto(0, 0)
    chartT.down()
    chartT.goto(maxitem, 0)
    chartT.up()

    chartT.goto(-1, 0)  # show min and max
    chartT.write("0", font=("Helvetica", 16, "bold"))
    chartT.goto(-1, maxcount)
    chartT.write(str(maxcount), font=("Helvetica", 16, "bold"))

    for index in range(len(itemlist)):
        chartT.goto(index, -1)  # label item value
        chartT.write(str(itemlist[index]), font=("Helvetica", 16, "bold"))

        chartT.goto(index, 0)  # draw line to height of count
        chartT.down()
        chartT.goto(index, countDict[itemlist[index]])
        chartT.up()
    wn.exitonclick()


list1 = [1, 1, 1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 12]
list2 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]

frequencyChart(list1)

#frequencyChart(list2)