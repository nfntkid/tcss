import car_class as cc
import garage_class as gc
import os,time

# CREATE OBJECTS FOR CARS USING THE MAKE,MODEL, AND YEAR
# STORE THESE OBJECTS IN A CSV FILE


new_garage = gc.Garage(0)

def scan_garage():
  garage_file = open("my_garage.txt", "r")
  new_garage.cars = []
  for i in garage_file:
    i = i.strip("\n")
    i = i.split(",")
    new_car = cc.Car(i[0], i[1], i[2], i[3])
    new_garage.cars.append(new_car)
  new_garage.display_cars()
  garage_file.close()

while True:
  os.system("clear")
  scan_garage()
  choice=input("Add new vehicle? (y/n)")
  if choice =="y":
    new_garage.add_car()

  elif choice =="n":
    os.system("clear")
    scan_garage()
    break

  else:
    print("type y or n.")
    time.sleep(1)






  
