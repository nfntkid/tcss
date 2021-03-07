import turtle

# CREATE SHAPES BY INPUTTING DIFFERENT ANGLES

shapes = ["Line", "angle", "Triangle", "Square", "Pentagon",
          "Hexagon", "septagon", "octagon", "nonagon",
          "decagon", "undefined"]

#only for equal sided shapes
#new function to convert angle into shapes
def shape(angle):
  print("enter an angle to draw a shape")
  angle = int(input(">>> ")) # get a number input
  sides = int(360/angle) #divide the angle by 360 to find num of sides

  if sides < 2:
    print("this is a " + str(shapes[0]))

  elif sides == 2:
    print("this is a " + str(shapes[1]))

  elif sides == 3:
    print("this is a " + str(shapes[2]))

  elif sides == 4:
    print("this is a " + str(shapes[3]))

  elif sides == 5:
    print("this is a " + str(shapes[4]))

  elif sides == 6:
    print("this is a " + str(shapes[5]))

  elif sides == 7:
    print("this is a " + str(shapes[6]))

  elif sides == 8:
    print("this is a " + str(shapes[7]))

  elif sides == 9:
    print("this is a " + str(shapes[8]))

  elif sides == 10:
    print("this is a " + str(shapes[9]))

  else:
    print("this shape is " + str(shapes[10]))

  a = turtle.Turtle() #new turtle obj
  for i in range(0,sides):
    a.forward(20)
    a.right(angle)
shape(input)
