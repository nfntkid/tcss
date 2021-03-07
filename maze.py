import turtle
screen = turtle.Screen()
# set the screen background

turtle.speed(0)
screen = turtle.Screen()
# set the screen background
# Or, set the shape of a turtle


out_ = turtle.Turtle()
out_.shape("square")
out_.color("red")
out_.speed(0)
out_.penup()
out_.left(90)
out_.goto(177,190)

in_ = turtle.Turtle()
in_.shape("circle")
in_.color("red")
in_.speed(0)
in_.penup()
in_.left(90)
in_.goto(-141,-177)



def make_perimeter():
  turtle.color("red")
  turtle.penup()
  turtle.goto(-120,-170)
  turtle.pendown()
  turtle.forward(315)
  turtle.left(90)
  turtle.forward(350)
  turtle.left(90)
  turtle.penup()
  turtle.forward(35)
  turtle.pendown()
  turtle.forward(315)
  turtle.left(90)
  turtle.forward(350)
make_perimeter()





def make_mid_path():
  turtle.color("blue")
  turtle.penup()
  turtle.goto(-120,-130)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(280)
  turtle.penup()
  turtle.goto(-70,-130)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(75)
  turtle.penup()
  turtle.goto(70,-130)
  turtle.pendown()
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(75)
  turtle.right(90)
  turtle.forward(175)
  turtle.backward(75)
  turtle.left(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(75)
  turtle.penup()
make_mid_path()


def make_outside_path():
  turtle.color("green")
  turtle.goto(-155,-50)
  turtle.pendown()
  turtle.right(90)
  turtle.forward(47.5)
  turtle.penup()
  turtle.goto(-57,180)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(75)
  turtle.penup()
  turtle.goto(195,120)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(150)
  turtle.left(90)
  turtle.forward(125)
  turtle.left(90)
  turtle.forward(75)
  turtle.right(90)
  turtle.forward(90)


make_outside_path()


def solutions():
  turtle.penup()
  turtle.goto(in_)
  turtle.speed(3)
  turtle.right(180)
  turtle.pendown()
  turtle.color("black")
  turtle.forward(25)
  turtle.right(90)
  turtle.forward(317)
  turtle.left(90)
  turtle.forward(45)
  turtle.left(90)
  turtle.forward(75)
  turtle.right(90)
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(75)
  turtle.right(90)
  turtle.forward(175)
  turtle.right(90)
  turtle.forward(145)
  turtle.left(90)
  turtle.forward(47)
  turtle.penup()
  turtle.goto(in_)
  turtle.pendown()
  turtle.forward(60)
  turtle.right(90)
  turtle.forward(45)
  turtle.left(90)
  turtle.forward(140)
  turtle.left(90)
  turtle.forward(45)
  turtle.right(90)
  turtle.forward(125)
  turtle.right(90)
  turtle.forward(55)
  turtle.right(90)
  turtle.forward(75)
  turtle.left(90)
  turtle.forward(60)
  turtle.left(90)
  turtle.forward(85)
  turtle.right(90)
  turtle.forward(197)
  turtle.left(90)
  turtle.forward(35)
  print("!!!YOU WIN!!!")



# Or, set the shape of a turtle
smiley = turtle.Turtle()
smiley.shape("turtle")
smiley.left(90)
smiley.penup()
smiley.goto(-141,-177)
move_speed = 5
turn_speed = 20


# these defs control the movement of our "turtle"

def forward():
  smiley.forward(move_speed)

def backward():
  smiley.backward(move_speed)

def left():
  smiley.left(turn_speed)

def right():
  smiley.right(turn_speed)

screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

def limit():
  import time, os
  def clr(sec):
    time.sleep(sec)
    os.system("clear")
  smxy = sx,sy = smiley.position()
  print(smxy)
  while True:
    smxy = sx,sy = smiley.position()
    if sx < -140: # left border
      smiley.setx(-135)

    if sx > 185:  # right border
      smiley.setx(180)

    if sy < -160: # bottom border
      smiley.sety(-155)

    if sy > 170:  # top border
      smiley.sety(165)

    if sy > -140 and sy < -124 and sx > -115 and sx < 160:
      smiley.back(5) #bottom blue border

    if sy > 35 and sy < 55 and sx > -111 and sx < 0:
      smiley.back(5) #top blue border

    if sy > -65 and sy < -46 and sx > -12 and sx < 75:
      smiley.back(5) #middle blue border

    if sy > -60 and sy < -40 and sx > -140 and sx < -97:
      smiley.back(5) #bottom green border

    if sy > 110 and sy < 130 and sx > 35 and sx < 185:
      smiley.back(5) #top green border

    if sy > -15 and sy < 5 and sx > 36 and sx < 129:
      smiley.back(5) #middle green border

    if sy > -121 and sy < -45 and sx > -79 and sx < -61:
      smiley.back(5) #bottom left vertical blue border

    if sy > -46 and sy < 128 and sx > -14 and sx < 2:
      smiley.back(5) #middle vertical blue border

    if sy > -120 and sy < -65 and sx > 60 and sx < 79:
      smiley.back(5) #bottom right vertical blue border

    if sy > 35 and sy < 129 and sx > -114 and sx < -95:
      smiley.back(5) #top blue vertical border

    if sy > 95 and sy < 170 and sx > -65 and sx < -49:
      smiley.back(5) #top green vertical border

    if sy > 5 and sy < 110 and sx > 35 and sx < 52:
      smiley.back(5) #middle green vertical border

    if sy > -96 and sy < -15 and sx > 112 and sx < 128:
      smiley.back(5) #bottom green vertical border

    if sy > 164 and sy < 170 and sx > 158 and sx < 185:
      print("!!!YOU WIN!!!") #where "YOU WIN" shows up
      break



    clr(.005)
    print(smxy)
limit()
