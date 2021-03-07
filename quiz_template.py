import time
import os

def clr(x): #this functions
    time.sleep(x)
    os.system('clear')


qBank = {
          "How long was world war 2" : "10 years", #Q1
          "What is gravity" : "a force",#Q2
          "In Which state is New Brunswick located?" : "New Jersey",#Q3
          "Who is the Owner of Amazon?":"jeff bezos", #Q4
          "What year did the great depression hit": "1933"} #Q5


ansKey = [
    {"a": '1 year',     "b": '5 years',    "c": '10 years' ,     "d": '3 years'}, #Q1

    {"a": 'a car',     "b": 'a force',    "c": 'a food' ,     "d": 'a wave'}, #Q2

    {"a": 'New Mexico',     "b": 'Texas',    "c": 'New Jersey' ,     "d": 'Iowa'}, #Q3

    {"a": 'Mark Zuckerberg',     "b": 'Steve Jobs',    "c": 'jeff bezos' ,     "d": 'Will Frasier'}, #Q4

    {"a": '1933',     "b": '1929',    "c": '1940' ,     "d": '1890'}  #Q5
        ]






def execute():
    global qNum
    global score
    print("\nQuestion %s\n %s\n" % (qNum+1, x ))
    print("a: "+ ansKey[qNum]["a"] )
    print("b: "+ ansKey[qNum]["b"] )
    print("c: "+ ansKey[qNum]["c"] )
    print("d: "+ ansKey[qNum]["d"] )

    correctAns = qBank[x]
    answer = input(">>")
    if answer not in ['a','b','c','d']:
      print("invalid response")
      clr(1)
      execute()
    else:
      answer = ansKey[qNum][answer]

      if answer == correctAns:
        print("correct")
        score += 1
      else:
        print("incorrect")
      qNum+=1
      clr(.5)







while True:
  score = 0 # creates a score that will be totaled into a percentage
  qNum = 0   # used as the demoninator in the percentage

  for x in qBank: # for each question in our list
    execute()


  percentage = (score/qNum) * 100 #find the actual percentage of the score result
  print("\nYou got a " + str(percentage) + "%")

###################### vvv THIS IS RESPONSIBLE FOR RUNNING THE WHILE LOOP vvv ###

  again = input("Take the quiz Again? y/n")                                   ###
  if again == "y":                                                            ###
    clr(1)                                                                    ###
    continue                                                                  ###
  else:                                                                       ###
    clr(.5)                                                                   ###
    if percentage < 70:                                                       ###
      print("GoodBye loser")                                                  ###
      break                                                                   ###
    else:                                                                     ###
      print("Champion!")                                                      ###
      break                                                                   ###
###################### ^^^ THIS IS RESPONSIBLE FOR RUNNING THE WHILE LOOP ^^^ ###
