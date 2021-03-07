class Garage:
  def __init__(self, capacity):
    self.capacity = capacity # number of cars that fit
    self.cars = []

  def display_cars(self):
      print("------------MY GARAGE------------\n\n")
      for car in self.cars:
        print(car.make + " " + car.model)

  def add_car(self):
    garage_file = open("my_garage.txt", "a")
    make = input("input a make: ")
    model = input("input a model: ")
    year = input("input a year: ")
    color = input("input a color: ")
    garage_file.write('\n'+ make+","+model+","+year+","+color)
