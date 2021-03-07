import random
import turtle
import time
import os

# GUESS THE AMOUNT OF TURTLE THAT POP UP ON THE SCREEN

turtle_objects = []
randomnumber = random.randint(0, 50)
x = -190
y = 190


for number in range(randomnumber):
  i = turtle.Turtle()
  i.penup()
  i.shape("turtle")
  i.color("blue")
  i.speed(100)
  i.right(random.randint(0, 360))
  i.goto(x, y)
  turtle_objects.append(i)
  x += random.randint (30, 60)
  if (number % random.randint(4, 7) == 0) and (number!=0):
    y -= random.randint(20, 40)
    x = -190


print("You have 5 seconds to count the turtles.")
time.sleep(5)
os.system("clear")


for i in turtle_objects:
  i.hideturtle()

tries = 5
while tries>0:
  time.sleep(.5)
  os.system("clear")
  print "guess how many turtles there were."
  guess = int(input(">>>"))

  if guess == randomnumber:
    print "CORRECT!!!!!"
    break
  elif guess < randomnumber:
    print "guess higher."

  elif guess > randomnumber:
    print "guess lower."
  tries-=1

print("Sorry you lose. The correct number was " + str(randomnumber))
