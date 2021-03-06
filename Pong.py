import turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

# Score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("red")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.pendown()
scoreboard.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_p1 = 0
score_p2 = 0

# Paddle 1
paddle_p1 = turtle.Turtle()
paddle_p1.speed(0)
paddle_p1.shape("square")
paddle_p1.color("red")
paddle_p1.penup()
paddle_p1.goto(-350, 0)

# Paddle B
paddle_p2 = turtle.Turtle()
paddle_p2.speed(0)
paddle_p2.shape("square")
paddle_p2.color("red")
paddle_p2.penup()
paddle_p2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 7
ball.dy = -2



# Function
def paddle_p1_up():
	y = paddle_p1.ycor()
	y += 20
	paddle_p1.sety(y)


def paddle_p1_down():
	y = paddle_p1.ycor()
	y -= 20
	paddle_p1.sety(y)


def paddle_p2_up():
	y = paddle_p2.ycor()
	y += 20
	paddle_p2.sety(y)


def paddle_p2_down():
	y = paddle_p2.ycor()
	y -= 20
	paddle_p2.sety(y)

# Keyboard binding
screen.onkey(paddle_p1_up, "w")
screen.onkey(paddle_p1_down, "s")
screen.onkey(paddle_p2_up, "Up")
screen.onkey(paddle_p2_down, "down")
screen.listen()

# Main game loop
while True:

	# Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_p1 += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_p2 += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_p1, score_p2), align="center", font=("Courier", 24, "normal"))







    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_p2.ycor() + 40 and ball.ycor() > paddle_p2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_p1.ycor() + 40 and ball.ycor() > paddle_p1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
