import turtle
import random

# Functions: a group of related statements that perform a specific task
# functions help us breakdown our program into sections
# DRY: Don't repeat yourself
# Formula:
# def functionName (parameters:
#   Body
#   optional 'return' statement

visham = turtle.Turtle()
isham = turtle.Turtle()
sham = turtle.Turtle()
ham = turtle.Turtle()
am = turtle.Turtle()

def drawTrack(length): 
  cameraMan = turtle.Turtle()
  cameraMan.shape("triangle")

  cameraMan.penup()
  cameraMan.goto(-175, 140)
  cameraMan.speed(0)

  for i in range(length):
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

def createTurtles():
  visham.shape("turtle")
  visham.penup()
  visham.goto(-200, 100)
  visham.color("red")

  # Create 4 more turtles, with different colors
  # Set their locations

  isham.shape("turtle")
  isham.penup()
  isham.goto(-200, 60)
  isham.color("blue")

  sham.shape("turtle")
  sham.penup()
  sham.goto(-200, 20)
  sham.color("green")

  ham.shape("turtle")
  ham.penup()
  ham.goto(-200, -20)
  ham.color("pink")

  am.shape("turtle")
  am.penup()
  am.goto(-200,-60)
  am.color("black")

def startRace():
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

drawTrack(16) # function call
createTurtles()
startRace()
