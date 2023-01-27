import turtle
import draw
import pi

aT = turtle.Turtle()
aT.up()
aT.left(90)
aT.forward(100)
aT.down()
aT.right(90)
draw.drawCircle(aT,100)
aT.up()
aT.right(90)
aT.forward(100)
aT.right(150)
aT.forward(100)
aT.down()
aT.right(120)
draw.drawPolygon(aT,100,6)
turtle.exitonclick()

print(pi.archimedes(1000))
print(pi.leibniz(1000))
print(pi.wallis(500))
print(pi.montePi(1000))