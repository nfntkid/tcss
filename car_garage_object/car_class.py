class Car:
  def __init__(self,make,model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def car_specs(self):
    print("make: " + self.make)
    print("model: " + self.model)
    print("year: " + self.year)
    print("color: " + self.color)
    
