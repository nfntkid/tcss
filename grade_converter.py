# TAKE A LIST OF GRADS AND DISPLAY THE NUMERICAL AND LETTER GRADE AVERAGE
# this creates a new empty list
tests = [ ]


# this function only takes 1 parameter
# the parameter is the input for the function
# this function will turn our number grade into a letter grade
def grade_converter(grade):
  if grade >= 90 and grade <= 100:
    return "A"

  elif grade >= 80 and grade <= 89:
    return "B"

  elif grade >= 70 and grade <= 79:
    return "C"
  elif grade >= 65 and grade <= 69:
    return "D"
  else:
    return "F"







# Create a function that averages the scores
# and creates a list variable called "testScores"
# we can feed our list into this function
def averageScore(testScores):
  mysum = 0 # set the variable to 0 so it doesnt interfere
  for eachScore in testScores:
    mysum += eachScore
  average = mysum/len(testScores)
  print("Your Test average is a " + grade_converter(average))







# THIS THE MENU OR THE FACE OF THE PROGRAM

#THIS IS THE FRONT END OF THE PROGRAM

x = 1 # creates the numbers that will show next to each test
print("It is time to grade the exams")
numTests = int(input("How many test Scores? "))

for i in range(numTests):
  y = int(input("Test score " + str(x) + ":" ))
  tests.append(y)
  print str(grade_converter(y)) # print the letter score of each test
  x+=1
averageScore(tests) # print the average of all testss


#int(input) means number input
  # you have to put str() around x because numbers can
  # not be combined with text. they have to be changed into text
# call the average function to take
# all the scores and output their average
# when we return a value from a function, we need to print
# the function when we call it
# If the function is not returning, we only have to call it
# without a print statement
