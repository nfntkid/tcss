import os
import time


# All the accounts are stored in a dictionary
accounts = [ {"FirstName":"Steve",
              "LastName":"Minton",
              "Pin":"1111",
              "Balance":500000000},

              {"FirstName":"Harry",
              "LastName":"Newman",
              "Pin":"2222",
              "Balance":10000000},

              {"FirstName":"Johansen",
              "LastName":"Janowski",
              "Pin":"3333",
              "Balance":30900000}]

pins = []
for i in range(len(accounts)):
  pins.append(accounts[i]['Pin'])



class ATM:
  def __init__(self, pin): # constructor function, sets the object
    self.pin = pin         #feed the pin input into a pin variable
    self.balance = 0       #initialize the balance to zero


    for i in range(len(accounts)):
      if self.pin in pins: # if the pin matches a pin in our system
        if self.pin == accounts[i]['Pin']:
          self.name = (accounts[i]["FirstName"]) + " " + (accounts[i]["LastName"]) #set the name to account owner
          self.balance = (accounts[i]["Balance"]) # set the balance to the account balance
          os.system("clear")
          print("WELCOME " + self.name ) #welcome screen
          self.menu() # start the menu

      elif self.pin not in pins: #if pin doesnt match up deny access
        print("Invalid Pin \n")
        time.sleep(1)
        os.system("clear")
        break



  def deposit(self, amount):
    amount = int(input("Deposit Funds/Select Amount: $"))
    if amount > 10000:
      print("Amount Too Large. Try again \n")       # If you go over the 10k limit, try again
    else:                                           # else, add the amount to balance.                                             # balance. Then go back to the
      self.balance += amount                        # then go back to the menu
    self.menu()



  def withdraw(self, amount):#same as the deposit function, just reverse
    amount = int(input("Withdraw Funds/Select Amount: $"))
    try:
      if amount > self.balance:
          print("Try again \n")
      else:
        self.balance -= amount
      self.menu()
    except ValueError:
      print("INVALID")
      self.withdraw()



  def menu(self):
    print("Current Balance:  %d" % (self.balance)) # show balance
    choice = input('''
    ENTER 1 FOR DEPOSIT
    ENTER 2 FOR WITHDRAWAL
    ENTER 3 TO EXIT\n''')
    amount = 0 # set temporary ammount to save as placeholder

    if choice == '1':
      self.deposit(amount)
    elif choice == '2':
      self.withdraw(amount)
    elif choice == '3':
      print("GOODBYE")
      time.sleep(2)
      os.system("clear")
      exit(0)
    else:
      self.menu()
      # always return to the menu if you dont have a valid entry

while True:
  # this will make a new instance of the ATM object
  newAccount = ATM(input("ENTER YOUR PIN: "))








    
