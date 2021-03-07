import turtle, random, time, os
#DODGE THE ASTEROIDS!!!


#SCREEN
screen = turtle.Screen()
screen.addshape("asteroid2.png")
screen.addshape("spaceship2.png")
screen.setup(600,600)
screen.bgpic("space3.png")


#SPACESHIP
spaceShip = turtle.Turtle()
spaceShip.penup()
spaceShip.goto(0,-100)
spaceShip.shape("spaceship2.png")


#ASTEROID
asteroid = turtle.Turtle()
asteroid.shape("asteroid2.png")
asteroid.penup()
asteroid.speed(0)
asteroid.right(90)
asteroid.goto(0,500)


# MOVE/TURN SPEEDS
move_speed = 15
turn_speed = 25
lives = 5

def clr(x):
  time.sleep(x)
  os.system("clear")

def collision_check(projectile, player):
  global lives
  projectileY = projectile.ycor()
  projectileX = projectile.xcor()
  playerY = player.ycor()
  playerX = player.xcor()

  aRadX1 =  projectileX - 70
  aRadX2 =  projectileX + 70
  aRadY1 =  projectileY - 50
  aRadY2 =  projectileY + 50

  if aRadX2 > playerX > aRadX1 and aRadY2 > playerY > aRadY1:
    lives -= 0.05

  if lives <= 0:
    lives = 0
    print("GAME OVER")
    spaceShip.hideturtle()
    exit(0)
  print(playerX, playerY)
  print(projectileX, projectileY)
  print("Lives: " + str(int(round(lives))))





def forward():
  spaceShip.forward(move_speed)
def backward():
  spaceShip.back(move_speed)
def left():
  spaceShip.left(turn_speed)
def right():
  spaceShip.right(turn_speed)

def keyBoard():
  screen.onkey(forward, "up")
  screen.onkey(backward, "down")
  screen.onkey(left, "left")
  screen.onkey(right, "right")
  screen.listen()



def infiniteScroll(spaceShip,asteroid):
  spaceShipX = spaceShip.xcor()
  spaceShipY = spaceShip.ycor()
  spaceShipPos = (spaceShipX,spaceShipY)

  if spaceShipY > 300:
    spaceShip.speed(0)
    spaceShip.goto(spaceShipX,-300)

  if spaceShipY < -300:
    spaceShip.speed(0)
    spaceShip.goto(spaceShipX,300)

  if spaceShipX > 300:
    spaceShip.speed(0)
    spaceShip.goto(-300,spaceShipY)

  if spaceShipX < -300:
    spaceShip.speed(0)
    spaceShip.goto(300,spaceShipY)

  if asteroid.ycor() < -300:
    randPos = random.randint(-200,200)
    asteroid.goto(randPos,500)




while True:
  clr(0.001)
  keyBoard()
  collision_check(asteroid,spaceShip)
  infiniteScroll(spaceShip,asteroid)
  asteroid.forward(5)










  
