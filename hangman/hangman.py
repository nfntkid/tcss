import random
import turtle
import os
import time



# THIS IS FILE INPUT TO USE TO THE WORDS
# IN THE WORD BANK (WORD.TXT)
# FILE INPUT / OUTPUT OPTIONS


# w = write - overwrites info to the file
# r = read - reads the information from the file
# a = append - adds information to the file
# x = execute - runs the file (if possible)



def drawPost():
  draw = turtle.Turtle()
  draw.speed(0)
  draw.penup()
  draw.goto(100,50)
  #----------------
  draw.left(90)
  draw.pendown()
  draw.forward(80)
  draw.left(90)
  #----------------
  draw.forward(100)
  draw.left(90)
  draw.forward(300)
  draw.left(90)
  #----------------
  draw.forward(100)
  draw.left(180)
  draw.forward(200)
  draw.hideturtle()


def drawHead():
  head = turtle.Turtle()
  head.speed(0)
  head.penup()
  head.goto(100,10)
  head.pendown()
  head.circle(20)
  head.hideturtle()


def drawBody():
  body = turtle.Turtle()
  body.speed(0)
  body.penup()
  body.goto(100,10)
  body.right(90)
  body.pendown()
  body.forward(80) # draw a downward straight line
  body.hideturtle() # hides body

def drawArm1():
  arm1 = turtle.Turtle()
  arm1.speed(0)
  arm1.penup()
  arm1.goto(100,-10)
  arm1.pendown()
  arm1.right(45)
  arm1.forward(40)
  arm1.hideturtle()

def drawArm2():
  arm2 = turtle.Turtle()
  arm2.speed(0)
  arm2.penup()
  arm2.goto(100,-10)
  arm2.pendown()
  arm2.left(45)
  arm2.forward(40)
  arm2.hideturtle()

def drawLeg1():
  leg1 = turtle.Turtle()
  leg1.speed(0)
  leg1.penup()
  leg1.goto(100,-70)
  leg1.pendown()
  leg1.right(135)
  leg1.forward(40)
  leg1.hideturtle()

def drawLeg2():
  leg2 = turtle.Turtle()
  leg2.speed(0)
  leg2.penup()
  leg2.goto(100,-70)
  leg2.pendown()
  leg2.right(45)
  leg2.forward(40)
  leg2.hideturtle()

def drawFace():
  #DRAW EYE 1
  face = turtle.Turtle()
  face.speed(0)
  face.penup()
  face.goto(90,30)
  face.pendown()
  face.circle(5)

  #DRAW EYE 2
  face.penup()
  face.goto(110,30)
  face.pendown()
  face.circle(5)

  #DRAW MOUTH
  face.penup()
  face.goto(90,20)
  face.pendown()
  face.forward(20)
  face.hideturtle()



letters_guessed = [ ]
words = [ ]
myFile = open("words.txt", 'r')
for x in myFile:
  x = x.strip("\n")
  words.append(x)


#Save randomly chosen word to a variable
hidden_word = random.choice(words).lower()
numDashes = len(hidden_word)
wordLength = len(hidden_word)




def drawBodyPart(guesses):
  # x equals the amount of guesses we have
  if guesses == 6:
    drawHead()

  elif guesses == 5:
    drawBody()

  elif guesses == 4:
    drawArm1()

  elif guesses == 3:
    drawArm2()

  elif guesses == 2:
    drawLeg1()

  elif guesses == 1:
    drawLeg2()

  elif guesses == 0:
    drawFace()
    print("YOU lose")
  else:
    print("***ERROR***") # Error validation

def clr(x): # clear function for 'x' amount of seconds
    time.sleep(x)
    os.system('clear')


##################################################
def get_guess():
  drawPost()
  dashes = []
  for i in range(wordLength): # creates a placeholder that is word length
    dashes.append("*")
  guesses_left = 7  # 7 body parts == 7 guesses
  clr(2)
  while guesses_left > 0 and not dashes == hidden_word:
    if numDashes < 1:
      print ("Congrats! You win. The word was: " + str(hidden_word))
      clr(3)
      exit(0) #ends everything / stops all
    print(" ".join(dashes))
    print(numDashes)
    print("Word Length: " + str(wordLength - 1))
    print ("Guesses Left: " + str(guesses_left))
    guess = input("Guess:")

    #1.
    if len(guess) != 1:       # If they guess multiple letters
      print ("Your guess must have exactly one character!")
      clr(.5)
    #2.
    elif guess in letters_guessed:
      print("that letter has been used")
      clr(.5)
    elif guess in hidden_word:# Guess is correct
      print ("That letter is in the secret word!")
      dashes = update_dashes(hidden_word, dashes, guess)
      clr(.5)
    #3.
    else:                     # incorrect guess
      print ("That letter is not in the secret word!")
      guesses_left -= 1
      drawBodyPart(guesses_left)
      clr(.5) #always clear the screen before the end of function
    letters_guessed.append(guess)
  if guesses_left == 0:          # STRAIGHT LOSER
    print ("You lose. The word was: " + str(hidden_word))
    clr(3)
  else:                         #YOU WINN
    pass



def update_dashes(secret, current_dash, recent_guess):
  global numDashes
  result = ""
  for i in range(len(secret)):
    if secret[i] == recent_guess:
      result = result + recent_guess
      numDashes -= 1
    else:
      result = result + current_dash[i]
  return result                       # only return the value to be passed
                                      # to the next function


while True:
  start = input("New game? y/n: ")
  if start == 'y':
    time.sleep(1)
    os.system('clear')
    get_guess() # call the guess function
  else:
    exit(0)
    
