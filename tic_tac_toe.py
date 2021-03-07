import turtle
import random
import time


#TWO PLAYER TIC TAC TOE
pen = turtle.Turtle()
pen.speed(1000)
omoves = [] #this stores all o moves that the player makes
xmoves = [] #this stores all x moves that the player makes
moves = []

# these are the coordinates for the x player to go to
Xspots = { 1:(-150,150),
           2:(0,150 ),
           3:(150,150),
           4:(-150,0),
           5:(0,0 ),
           6:(150,0),
           7:(-150,-150),
           8:(0,-150 ),
           9:(150,-150)}

# these are the coordinates for the O player to go to

Ospots = { 1:(-150,120),
           2:(0,120 ),
           3:(150,120),
           4:(-150,-30),
           5:(0,-30 ),
           6:(150,-30),
           7:(-150,-180),
           8:(0,-180 ),
           9:(150,-180)}

#this is the total possible moves we can win with
winMoves =[ [1,2,3], [4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9],
            [1,5,9],[3,5,7] ]

def checkWin(player):
  for x in winMoves:
    if (x[0] in player and x[1] in player and x[2] in player):
      for x in range(5): #  checks to see if we have any of the
        if player == omoves:# possible winning moves in our moves
          print(" O is Winner!!")
          time.sleep(1)
        elif player == xmoves:
          print(" X is Winner!!")
          time.sleep(1)
        else:
          print("TIE")
      exit()




def makeboard():
  pen.up()  # this is the left vertical line
  pen.goto(-90, 250)
  pen.down()
  pen.right(90)
  pen.forward(500)

  pen.up() #this is the right vertical line
  pen.goto(90, 250)
  pen.down()
  pen.forward(500)

  pen.up() # this is the top horizontal line
  pen.goto(-250, 90)
  pen.down()
  pen.left(90)
  pen.forward(500)

  pen.up() #this is the bottom horizontal line
  pen.goto(-250, -90)
  pen.down()
  pen.forward(500)




def drawx():
  pen.pendown()
  for i in range(4):
    pen.forward(45)
    pen.back(45)
    pen.right(90)

def drawo():
  pen.pendown()
  pen.circle(45)


def playerGoX():
  position = int(input("Enter a position X: "))
  if position in moves:
    print("Choose another spot")
    playerGoX()
  else: # if you choose a valid spot
    coord = Xspots[position] # find the right coordinate
    moves.append(position)   # add that move to the list of moves so you cant do it again
    xmoves.append(position)  # add that move to the x moves so we can see if they win
    xmoves.sort()            # put the  moves in numerical order
    pen.penup()              #pen up
    pen.goto(coord)          # go to the coordinate
    pen.pendown()            # pen down
    drawx()                  # draw a x mark
    checkWin(xmoves)         # see if the X player won yet
    playerGoO()              # let the O player go





def playerGoO():
  position = int(input("Enter a position O: "))
  if position in moves:
    print("Choose another spot")
    playerGoO()
  else:
    coord = Ospots[position]
    moves.append(position)
    omoves.append(position)
    omoves.sort()
    pen.penup()
    pen.goto(coord)
    pen.pendown()
    drawo()
    checkWin(omoves)
    playerGoX()






def menu():
  makeboard()
  x_turn = False
  o_turn = False

  print("welcome to Tic tac toe. ")
  player1 = input("Player 1 whats your name?")
  player2 = input("Player 2 whats your name?")
  start = random.randint(0,100)

  print("Guess a number between 0 and 100 to see who starts")
  answer1 = int(input("PLAYER1: "))
  answer2 = int(input("PLAYER2: "))




  if answer1 > 100 or answer1 < 0:
    print("Sorry X You messed up. It's " + player2 + "'s turn")
    playerGoO()
   # If a player guesses out of range, give the turn to the other player

  if answer2 > 100 or answer2 < 0:
    print("Sorry O You messed up "+ "It's " + player2 + "'s turn")
    playerGoX()



  #START HEHRE
  #Check to see who guessed correct

  if (start - answer1) < (start - answer2) or (start == answer1):
    print ("The number was " + str(start) + " " + player1 + " GOES!")
    x_turn = True
  else:
    print ("The number was " + str(start) + " " + player2 + " GOES!")
    o_turn = True

  while True:
    if x_turn == True:
      playerGoX()
    elif o_turn == True:
      playerGoO()


menu()
