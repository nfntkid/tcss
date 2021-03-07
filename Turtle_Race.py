# BET ON A TURTLE AND SEE IF YOU CAN GET TO THE DESIRED AMOUNT!

import time
import os
import random
import turtle
# we import our modules. These are toolkits that we use
# to perform more complex methods. There are thousands
# of modules in python all used for different reasons


pen = turtle.Turtle()
pen.speed(100)
x = -150
y = 100
pen.right(90)
# We create a new turtle object using the turtle module
# we set the speed to 100 so that the lines are drawn fast
# we make a x and y variable to start the pen at a certain point
# we rotate the pen 90 degrees to the right.


def makeLine():
  pen.penup()
  pen.goto(x,y)
  pen.pendown()
  pen.forward(300)
# the makeline function is what we use to make our race grid
# first we do penup() to make sure the pen doesnt draw
# then we use goto() to move the pen to our selected spot
# then we do pendown() to begin drawing
# pen.forward moves the turtle 300 steps forward

for i in range(7):
  makeLine()
  x+=50
pen.hideturtle()
# loops are used to do repetitive tasks.
# we use a for loop to run the makeline function 7 times
# x+=50 increases x by 50 so that the line shifts to the right
# we then hide the pen using hideturtle()



r1 = turtle.Turtle()
r2 = turtle.Turtle()
r3 = turtle.Turtle()
r4 = turtle.Turtle()
r5 = turtle.Turtle()
r6 = turtle.Turtle()
# we create a variable object for each turtle racer
# these variables store information for each turtle object
# objects closely resemble nouns



myRacers = [r1,r2,r3,r4,r5,r6] # stores the objects
myRacersStr = ['r1','r2','r3','r4','r5','r6']
colors = ['red', 'green', 'blue', 'brown', 'black','grey']
# we create a list for each of the racer objects
# we also create a list to store the names of each object as string
# we also create a list to hold the colors used



for eachTurtle in myRacers:
  randomColor = random.randint(0,5)
  eachTurtle.color(colors[randomColor])
  eachTurtle.speed(0)
  eachTurtle.shape('turtle')
  eachTurtle.penup()
  eachTurtle.right(90)
# the loop takes each individual turtle object and applys these settings to them
# We create a random number variable then feed it into a color list we created.
# by using the random number as an index



def readyPosition():
  r1.goto(-120,100)
  r2.goto(-70,100)
  r3.goto(-20,100)
  r4.goto(30,100)
  r5.goto(80,100)
  r6.goto(130,100)
# we put each turtle object in a specific location on the grid



tSpeeds = [] #holds speed for each turtle

def raceTurtles():
  for turtle in myRacers:
    speed = random.randint(20,80)
    turtle.speed(speed)
    tSpeeds.append(speed)
    turtle.forward(285)
# the loop takes each individual turtle object and applys these settings to them
# We assign the speed variable to a random number
# we add the current speed of the current turtle to a list of speeds
# we move the individual turtle forward
def bet(money):
#################################################
# 1.) CLEAR THE SYSTEM SET THE RANKS
  os.system('clear')
  readyPosition()
  ranks = ['Loser','Casual','Gambler','Expert']
  rank = " "
  if money < 5000:
    rank = ranks[0]
  elif money >= 5000 and money <=15000:
    rank = ranks[1]
  elif money >= 15000 and money <=20000:
    rank = ranks[2]
  else:
    rank = ranks[3]
#################################################
# 2.) PRINT THE RANKS, MONEY, RACERS
  print("Welcome to the casino, are you ready to LOSE ALL YOUR MONEY?")
  print("CASH: $" + str(money))
  print("RANK: " + rank)
  x = " "
  x = x.join(myRacersStr) # print the racer names to the screen
  print('\n' + x +'\n')
####################################################
# 3.) Start Betting on turtles
  betAmount = int(input("Wager Amount: "))
  if betAmount > money: #if you try to bet more than you have
    print("You need more money to do that!")
    time.sleep(1) #pause the screen
    bet(money) # run the function again
  else:
    if betAmount < 500:
      print("THATS NOT ALLOWED HERE! MORE MONEY PLEASE!")
      time.sleep(1)
      bet(money)
    elif betAmount > 10000:
      print("Wow thank you for your service! Free $1000 on me!")
      money += 1000
      betRacer = input("who do you bet on")
      if betRacer not in myRacersStr:
        print("INVALID")
        time.sleep(1)
        bet(money)
      else:
        print("AWESOME :)")
        raceTurtles()
    else:
      print("Amount locked in")
      betRacer = input("who do you bet on")
      if betRacer not in myRacersStr:
        print("INVALID")
        time.sleep(1)
        bet(money)
      else:
        print("AWESOME :)")
        raceTurtles()
######################################################
# 4.) Who won??
    winnerSpeed = max(tSpeeds) #finds the max speed
    winnerIndex = tSpeeds.index(winnerSpeed) #finds the index
    winner = myRacersStr[winnerIndex]
    print("the winner is "+ (winner))
    winnerList = dict(zip(myRacers, tSpeeds))
    if betRacer == winner:
      money += betAmount
    elif betRacer != winner:
      money -= betAmount
    time.sleep(1)
    del tSpeeds[:]
#############################################
# 5.) DETERMINE WIN OR LOSS
    if money < 500:
      print("YOU HAVE NO MONEY SIR")
      time.sleep(2)
      exit(0)
    elif money > 25000:
      print("YOU WIN THE SYSTEM")
      time.sleep(2)
      exit(0)
    bet(money)
bet(random.randint(5000,20000))
