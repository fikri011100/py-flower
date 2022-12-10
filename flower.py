
import turtle
 
 
turtle.penup ()
turtle.left (100)
turtle.fd (50)
turtle.pendown ()
turtle.right (100)

for i in range(4):
  turtle.right (90)
  turtle.circle (30,180)
  turtle.left (180)
  turtle.circle (30,180)
  turtle.left (90)
  turtle.forward(-100)
  turtle.left (180)
  turtle.circle (30,180)
  turtle.left(90)
  turtle.forward(60)
  turtle.left (90)
  turtle.circle (30,180)
  turtle.forward(180)
  turtle.left(30)
  turtle.circle (80,70)

# turtle.forward(180)
# turtle.left(30)
# turtle.circle (80,60)

turtle.done()