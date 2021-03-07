import turtle

# KEY DETECTION USING THE TURTLE MODULE

pen = turtle.Turtle() #create a new turtle object
screen = turtle.Screen()# turn on the screen settings
pen.shape("turtle")
pen.penup()
move_speed = 20
turn_speed = 30


# these defs control the movement of our "pen"
def forward():
  pen.forward(move_speed)

def backward():
  pen.backward(move_speed)

def left():
  pen.left(turn_speed)

def right():
  pen.right(turn_speed)

def pennOn():
  pen.pendown()

def pennOff():
  pen.penup()

def red():
  pen.color("red")

def blue():
  pen.color("blue")

def green():
  pen.color("green")

def yellow():
  pen.color("yellow")



screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(pennOn, "Z")
screen.onkey(pennOff, "A")
screen.onkey(red, "R")
screen.onkey(blue, "B")
screen.onkey(green, "G")
screen.onkey(yellow, "Y")

screen.listen()
