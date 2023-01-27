# This function draws a polygon of side length, n, and number of sides, m
# This is done by moving forward by length n and turning by 360 / m
def drawPolygon(myTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

# This function draws a circle of radius r
# This is done by calculating the circumference, then using that to create a polygon with 360 sides
def drawCircle(myTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(myTurtle, sideLength, 360)