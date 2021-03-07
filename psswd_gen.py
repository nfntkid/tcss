import random, time, os, string

# SIMPLE PASSWORD GENERATOR
################################################
#
# weak    - lowercase and numbers only,
#            5 to 10 characters
#
# medium  - lowercase, numbers &
#           uppercase required
#           10 to 15 characters
#
# strong  - lowercase, numbers, symbols
#           and uppercase all required
#           15 to 20 characters
#
################################################




symbols = list(string.punctuation)
numbers = list(string.digits)
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)



# the clr function clears the
# screen for x amount of seconds
def clr(x):
  time.sleep(x)
  os.system('clear')
 

# the printWord function
# displays the password
# letter by letter
def printWord(word):
  for i in word:
    time.sleep(0.05)
    print i,


# parameter is input for a function
# example if youre cooking, the amount of certain ingredients
# would be your parameter
def createPassword(strength):

  weakList = numbers + lower ; random.shuffle(weakList)
  weakLength = random.randint(5,10)

  mediumList = numbers + lower + upper; random.shuffle(mediumList)
  mediumLength = random.randint(10,15)

  strongList = numbers + lower + upper + symbols; random.shuffle(strongList)
  strongLength = random.randint(15,20)



  password = [ ]
  if strength == "weak":
      for x in range(weakLength):
          x = random.choice(weakList)
          password.append(x)
      print("\nPASSWORD")
      printWord(password)

  elif strength == "medium":
    for x in range(mediumLength):
      x = random.choice(mediumList)
      password.append(x)
    print("\nPASSWORD")
    printWord(password)

  elif strength == "strong":
    for x in range(strongLength):
      x = random.choice(strongList)
      password.append(x)
    print("\nPASSWORD")
    printWord(password)

  else:
    print("please select a valid password strength")
    createPassword(strength)



def menu():
  time.sleep(1)
  os.system("clear")
  print("SECURE PASSWORD GENERATOR")
  print("\n-Select your password Strength")
  print("1| WEAK")
  print("2| MEDIUM")
  print("3| STRONG")

  choice = input("select 1 - 3: ")
  if choice == "1":
    createPassword("weak")

  elif choice == "2":
    createPassword("medium")

  elif choice == "3":
    createPassword("strong")

  else:
    print("Invalid option. Try Again")
    menu()

while True:
  menu()
  carryOn = input("\n\npress enter to continue")
