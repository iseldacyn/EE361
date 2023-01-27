import math
import random

# This function estimates pi by estimating the circumference of a circle
# The angle of each triangle is found based off of the sides inputted
# The side length is then found, and then added up and divided by 2 to find pi
def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2

    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2

    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi

# This function estimates pi using a mathematical function
# This runs through a summation of the Leibniz function, based off the number of terms inputted
# The result is multiplied by 4, as the Leibniz function estimates pi/4
def leibniz(terms):
    acc = 0
    num = 4    #numerator is constant
    den = 1     #denominator starts at 1

    for aTerm in range(terms):
        nextTerm = num / den
        if (aTerm%2==1):
             nextTerm = nextTerm * (-1)
        acc = acc + nextTerm    #add term to accumulator
        den = den + 2                  #prepare for next term
    return acc

# This function estimates pi using a mathematical formula
# This runs through a summation of the Wallis function, using pairs of digits based on the value inputted
# The result is multiplied by 2, as the Wallis function estimates pi/2
def wallis(pairs):
    acc = 1  # initialize accumulator to 1 for multiplication
    num = 2  # numerator starts at 2
    for aPair in range(pairs):
        leftTerm = num / (num - 1)  # denominator is numerator - 1
        rightTerm = num / (num + 1)  # denominator is numerator + 1

        acc = acc * leftTerm * rightTerm  # compute running product

        num = num + 2  # prepare for next term

    pi = acc * 2
    return pi

# This function runs a variant of the Monte Carlo Simulation to estimate pi
# Random numbers between 0 and 1 are found, depending on the value inputted
# If their squares add up to 1 then they are added to inCircle
# The ratio between inCircle and the total darts are found, then multiplied by 4 to estimate pi
def montePi(numDarts):
    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x ** 2 + y ** 2)  # compute distance from (0, 0)
        if d <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi
