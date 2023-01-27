import turtle
import math


class SolarSystem:
  def __init__(self, width, height):
    self.__theSun = None
    self.__planets = []
    self.__ssTurtle = turtle.Turtle()
    self.__ssTurtle.hideturtle()
    self.__ssScreen = turtle.Screen()
    self.__ssScreen.setworldcoordinates(-width / 2.0, -height / 2.0,
                      width / 2.0, height / 2.0)

  def addPlanet(self, aPlanet):
    self.__planets.append(aPlanet)

  def addSun(self, aSun):
    self.__theSun = aSun

  def showPlanets(self):
    for aPlanet in self.__planets:
      print(aPlanet)

  def movePlanets(self):
    G = .1
    dt = .001

    for p in self.__planets:
      p.moveTo(p.getXPos() + dt * p.getXVel(),
           p.getYPos() + dt * p.getYVel())

      rX = self.__theSun.getXPos() - p.getXPos()
      rY = self.__theSun.getYPos() - p.getYPos()

      r = math.sqrt(rX ** 2 + rY ** 2)

      accX = G * self.__theSun.getMass() * rX / r ** 3
      accY = G * self.__theSun.getMass() * rY / r ** 3

      p.setXVel(p.getXVel() + dt * accX)
      p.setYVel(p.getYVel() + dt * accY)

  def freeze(self):
    self.__ssScreen.exitonclick()


class Sun:
  def __init__(self, iName, iRad, iM, iTemp):
    self.__name = iName
    self.__radius = iRad
    self.__mass = iM
    self.__temp = iTemp
    self.__x = 0
    self.__y = 0

    self.__sTurtle = turtle.Turtle()
    self.__sTurtle.shape("circle")
    self.__sTurtle.color("yellow")

  def getMass(self):
    return self.__mass

  def getXPos(self):
    return self.__x

  def getYPos(self):
    return self.__y

  def __lt__(self, other):
    return self.__mass < other.__mass

  def __str__(self):
    return self.__name + str(self.__mass)


class Planet:
  __name: object

  def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
    self.__name = iName
    self.__radius = iRad
    self.__mass = iM
    self.__distance = iDist
    self.__velX = iVx
    self.__velY = iVy

    self.__x = self.__distance
    self.__y = 0
    self.__color = iC

    self.__pTurtle = turtle.Turtle()

    self.__pTurtle.color(self.__color)
    self.__pTurtle.shape("circle")

    self.__pTurtle.up()
    self.__pTurtle.goto(self.__x, self.__y)
    self.__pTurtle.down()

  def getXPos(self):
    return self.__x

  def getYPos(self):
    return self.__y

  def moveTo(self, newX, newY):
    self.__x = newX
    self.__y = newY
    self.__pTurtle.goto(self.__x, self.__y)

  def getXVel(self):
    return self.__velX

  def getYVel(self):
    return self.__velY

  def setXVel(self, newVx):
    self.__velX = newVx

  def setYVel(self, newVy):
    self.__velY = newVy

  # problem 3 __repr__ method
  def __repr__(self):
    return 'Name:%s,Mass:%d,Distance:%.2f,Radius:%.1d' % (self.__name, self.__mass, self.__distance, self.__radius)

  # problem 4 __lt__ method
  def __lt__(self, other):
    return self.__mass < other.__mass


def createSSandAnimate():
  ss = SolarSystem(2, 2)

  planetList = []

  # smaller mass
  # sun = Sun("Sun", 5000, 10, 2000)
  # larger mass
  # sun = Sun("Sun", 5000, 10, 10000)
  # normal mass
  sun = Sun("Sun", 5000, 10, 5800)
  ss.addSun(sun)

  m = Planet("Jupiter", 100, 49000, 0.7, 0, 1, "black")
  ss.addPlanet(m)
  planetList.append(m)

  m = Planet("Mars", 50, 9000, 0.5, 0, 1.63, "red")
  ss.addPlanet(m)
  planetList.append(m)

  m = Planet("Earth", 47.5, 5000, 0.3, 0, 2.0, "green")
  ss.addPlanet(m)
  planetList.append(m)

  m = Planet("Mercury", 19.5, 1000, .25, 0, 2, "blue")
  ss.addPlanet(m)
  planetList.append(m)

  print(m)
  planetList.sort()
  print(planetList)

  numTimePeriods = 2000
  for aMove in range(numTimePeriods):
    ss.movePlanets()

  ss.freeze()


if __name__ == '__main__':
  createSSandAnimate()

# Problem 1
# Constructors:
# Solar System - __init__(self, width, height)
# Sun          - __init__(self, iName, iRad, iM, iTemp)
# Planet       - __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC)
# Accessors:
# Solar System - showPlanets(self)
# Sun          - getMass(self), getXPos(self), getYPos(self), getXVel(self), getYVel(self)
# Planet       - getXPos(self), getYPos(self)
# Mutators:
# Solar System - movePlanets(self)
# Sun          - N/A
# Planet       - moveTo(self, newX, newY), setXVel(self, newVx), setYVel(self, newVy)

# Problem 2
# When a smaller sun is used, the planets make a longer, more elliptical orbit around the sun
# When a larger sun is used, the planets make a shorter, more elliptical orbit around the sun

# Problem 3
# Before adding a __repr__(self):
# <__main__.Planet object at 0x0000013ACDB5B430>
# After adding a __repr__(self):
# Name:Mercury,Mass:1000,Distance:0.25,Radius:19
# Without adding the method function, the memory address is displayed to the screen
# With the method function, the elements of the object are displayed

# Problem 4
# Before adding __lt__(self):
# TypeError: '<' not supported between instances of 'Planet' and 'Planet'
# After adding __lt__(self):
# [Name:Mercury,Mass:1000,Distance:0.25,Radius:19, Name:Earth,Mass:5000,Distance:0.30,Radius:47,
#   Name:Mars,Mass:9000,Distance:0.50,Radius:50, Name:Jupiter,Mass:49000,Distance:0.70,Radius:100]
# Before adding the method function, there's no way to compare objects of type "Planet" and returns an error
# After adding a method function, the Planets are displayed in order of increasing mass
