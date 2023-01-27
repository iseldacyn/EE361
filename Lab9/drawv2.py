import turtle


class Canvas:
  def __init__(self, w, h):
    self.__visibleObjects = []  # list of shapes to draw
    self.__turtle = turtle.Turtle()
    self.__screen = turtle.Screen()
    self.__screen.setup(width=w, height=h)
    self.__turtle.hideturtle()

  def drawAll(self):
    self.__turtle.reset()
    self.__turtle.up()
    self.__screen.tracer(0)
    for shape in self.__visibleObjects:  # draw all shapes in order
      shape._draw(self.__turtle)
    self.__screen.tracer(1)
    self.__turtle.hideturtle()

  def addShape(self, shape):
    self.__visibleObjects.append(shape)

  def draw(self, gObject):
    gObject.setCanvas(self)
    gObject.setVisible(True)
    self.__turtle.up()
    self.__screen.tracer(0)
    gObject._draw(self.__turtle)
    self.__screen.tracer(1)
    self.addShape(gObject)


from abc import *
class GeometricObject(ABC):
  def __init__(self):
    self.__lineColor = 'black'
    self.__lineWidth = 1
    self.__visible = False
    self.__myCanvas = None

  def setColor(self, color):  # modified to redraw visible shapes
    self.__lineColor = color
    if self.__visible:
      self.__myCanvas.drawAll()

  def setWidth(self, width):  # modified to redraw visible shapes
    self.__lineWidth = width
    if self.__visible:
      self.__myCanvas.drawAll()

  def getColor(self):
    return self.__lineColor

  def getWidth(self):
    return self.__lineWidth

  @abstractmethod
  def _draw(self, turtle):
    pass

  def setVisible(self, vFlag):
    self.__visible = vFlag

  def getVisible(self):
    return self.__visible

  def setCanvas(self, theCanvas):
    self.__myCanvas = theCanvas

  def getCanvas(self):
    return self.__myCanvas


class Point(GeometricObject):
  def __init__(self, x, y):
    super().__init__()
    self.__x = x
    self.__y = y

  def getCoord(self):
    return (self.__x, self.__y)

  def getX(self):
    return self.__x

  def getY(self):
    return self.__y

  def _draw(self, turtle):
    turtle.goto(self.__x, self.__y)
    # turtle.dot(self.__lineWidth, self.__lineColor)
    turtle.dot(self.getWidth(), self.getColor())


class Line(GeometricObject):
  def __init__(self, p1, p2):
    super().__init__()
    self.__p1 = p1
    self.__p2 = p2

  def getP1(self):
    return self.__p1

  def getP2(self):
    return self.__p2

  def _draw(self, turtle):
    turtle.color(self.getColor())
    turtle.width(self.getWidth())
    turtle.up()
    turtle.goto(self.__p1.getCoord())
    turtle.down()
    turtle.goto(self.__p2.getCoord())


class Shape(GeometricObject):
  def __init__(self, fillColor):
    super().__init__()
    self.__fillColor = fillColor

  def setFillColor(self, color):
    self.__fillColor = color

  def getFillColor(self):
    return self.__fillColor


from math import *
class Ellipse(Shape):
  def __init__(self, cx, cy, a, b, angle):
    super().__init__('white')
    self.__cx = cx
    self.__cy = cy
    self.__a = a
    self.__b = b
    self.__angle = angle

  def _draw(self, turtle):
    turtle.color(self.getColor())
    turtle.width(self.getWidth())
    t = 0
    x = self.__cx + self.__a * cos(t) * cos(radians(self.__angle)) \
      - self.__b * sin(t) * sin(radians(self.__angle))
    y = self.__cy + self.__a * cos(t) * sin(radians(self.__angle)) \
      + self.__b * sin(t) * cos(radians(self.__angle))
    turtle.up()
    turtle.goto(x, y)
    turtle.fillcolor(self.getFillColor())
    turtle.begin_fill()
    turtle.down()
    for i in range(2000):
      x = self.__cx + self.__a * cos(t) * cos(radians(self.__angle)) \
        - self.__b * sin(t) * sin(radians(self.__angle))
      y = self.__cy + self.__a * cos(t) * sin(radians(self.__angle)) \
        + self.__b * sin(t) * cos(radians(self.__angle))
      turtle.goto(x, y)
      t += 2 * pi / 2000
    turtle.end_fill()


class Circle(Ellipse):
  def __init__(self, c, r):
    super().__init__(c.getX(), c.getY(), r, r, 0)
    self.__c = c
    self.__r = r


class Polygon(Shape):
  def __init__(self, pointList):
    super().__init__('white')
    self.__pointList = pointList

  def addPoint(self, point):
    self.__pointList.append(point)

  def getPoints(self):
    return self.__pointList

  def _draw(self, turtle):
    turtle.color(self.getColor())
    turtle.width(self.getWidth())
    turtle.up()
    turtle.goto(self.__pointList[-1].getCoord())
    turtle.fillcolor(self.getFillColor())
    turtle.begin_fill()
    turtle.down()
    for i in self.__pointList:
      turtle.goto(i.getCoord())
    turtle.end_fill()


class Triangle(Polygon):
  def __init__(self, p1, p2, p3):
    super().__init__([p1, p2, p3])
    self.__p1 = p1
    self.__p2 = p2
    self.__p3 = p3

  def getP1(self):
    return self.__p1

  def getP2(self):
    return self.__p2

  def getP3(self):
    return self.__p3


class Rectangle(Polygon):
  def __init__(self, lowerLeft, upperRight):
    super().__init__([lowerLeft, Point(upperRight.getX(), lowerLeft.getY()),
              upperRight, Point(lowerLeft.getX(), upperRight.getY())])
    self.__lowerLeft = lowerLeft
    self.__upperRight = upperRight

  def getLowerLeft(self):
    return self.__lowerLeft

  def getUpperRight(self):
    return self.__upperRight


class Square(Rectangle):
  def __init__(self, corner, length):
    super().__init__(corner, Point(corner.getX()+length, corner.getY()+length))
    self.__corner = corner
    self.__length = length

  def getCorner(self):
    return self.__corner

  def getSideLength(self):
    return self.__length


def test2():
  myCanvas = Canvas(500, 500)
  line1 = Line(Point(-100, -100), Point(100, 100))
  line2 = Line(Point(-100, 100), Point(100, -100))
  line1.setWidth(4)
  myCanvas.draw(line1)
  myCanvas.draw(line2)
  line1.setColor('red')
  # line2.setWidth(4)
  turtle.exitonclick()


def drawHouse():
  myCanvas = Canvas(800, 600)  # create a canvas
  house = Rectangle(Point(-100, -100),
            Point(100, 100))  # draw a rectangle from 2 points - bottom left and top right corners
  house.setFillColor('blue')  # fill with color
  door = Rectangle(Point(-50, -100), Point(0, 75))
  door.setFillColor('brown')
  roof1 = Line(Point(-100, 100), Point(0, 200))  # draw a line from 2 points
  roof2 = Line(Point(0, 200), Point(100, 100))
  roof1.setWidth(3)  # set line width
  roof2.setWidth(3)
  myCanvas.draw(house)
  myCanvas.draw(door)
  myCanvas.draw(roof1)
  myCanvas.draw(roof2)
  sun = Circle(Point(150, 250), 20)  # draw a circle from point and radius
  sun.setFillColor('yellow')
  sun.setWidth(5)
  myCanvas.draw(sun)
  turtle.exitonclick()


if __name__ == '__main__':
  # test2()
  drawHouse()
