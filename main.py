import turtle
import random

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")

cameraMan.penup()
cameraMan.goto(-175, 140)
cameraMan.speed(0)

for i in range(16):
  cameraMan.write(i)
  cameraMan.right(90)
  cameraMan.forward(20)
  cameraMan.pendown()
  cameraMan.forward(200)
  cameraMan.left(180)
  cameraMan.penup()
  cameraMan.forward(220)
  cameraMan.right(90)
  cameraMan.forward(20)
cameraMan.hideturtle()

visham = turtle.Turtle()
visham.shape("turtle")
visham.penup()
visham.goto(-200, 100)
visham.color("red")

# Create 4 more turtles, with different colors
# Set their locations

isham = turtle.Turtle()
isham.shape("turtle")
isham.penup()
isham.goto(-200, 60)
isham.color("blue")

sham = turtle.Turtle()
sham.shape("turtle")
sham.penup()
sham.goto(-200, 20)
sham.color("green")

ham = turtle.Turtle()
ham.shape("turtle")
ham.penup()
ham.goto(-200, -20)
ham.color("pink")

am = turtle.Turtle()
am.shape("turtle")
am.penup()
am.goto(-200,-60)
am.color("black")

visham.pendown()
isham.pendown()
sham.pendown()
ham.pendown()
am.pendown()

for i in range(40):
  visham.forward(random.randint(1,15))
  isham.forward(random.randint(1,15))
  sham.forward(random.randint(1,15))
  ham.forward(random.randint(1,15))
  am.forward(random.randint(1,15))
