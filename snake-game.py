#importing libraries
#importing libraries
import turtle
import random
import time


#creating turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width=800, height=800)
screen.tracer(0)
turtle.bgcolor('black')
turtle.bgpic('head.png')

# creating a border for our game
turtle.speed(5)
turtle.pensize(10)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
turtle.color('red')
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()

#score
score = 0
delay = 0.1


#snake
snake = turtle.Turtle()
snake.speed(0)
turtle.addshape('head1.gif')
snake.shape('head1.gif')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'


#food
fruit = turtle.Turtle()
fruit.speed(0)
turtle.addshape('fruit.gif')
fruit.shape('fruit.gif')
fruit.penup()
fruit.goto(30, 30)

old_fruit = []

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score :", align="center", font=("Courier", 24, "bold"))

# name tag
name = turtle.Turtle()
name.speed(0)
name.color("white")
name.penup()
name.hideturtle()
name.goto(0, -350)
name.write("Developed by: Kavi Castelo", align="center", font=("Courier", 18, "bold"))

# define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def pause():
    if snake.direction != "up""down""right""left":
        snake.direction = "pause"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    if snake.direction == "pause":
        x = snake.xcor()
        snake.setx(x)
        y = snake.ycor()
        snake.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")
screen.onkeypress(pause, "space")

#main loop
while True:
        screen.update()
        # snake and fruit collisions
        if snake.distance(fruit) < 20:
                x = random.randint(-290, 270)
                y = random.randint(-240, 240)
                fruit.goto(x, y)
                scoring.clear()
                score += 1
                scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
                delay -= 0.001
                
                # creating new_ball
                new_fruit = turtle.Turtle()
                new_fruit.speed(0)
                turtle.addshape('body.gif')
                new_fruit.shape('body.gif')
                new_fruit.penup()
                old_fruit.append(new_fruit)

        # adding ball to snake
        for index in range(len(old_fruit)-1, 0, -1):
                a = old_fruit[index-1].xcor()
                b = old_fruit[index-1].ycor()

                old_fruit[index].goto(a, b)
                                     
        if len(old_fruit) > 0:
                a = snake.xcor()
                b = snake.ycor()
                old_fruit[0].goto(a, b)
        snake_move()

        # snake and border collision
        if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 280 or snake.ycor() < - 280:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('purple')
                scoring.goto(0, 0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),
                              align="center", font=("Courier", 30, "bold"))

        time.sleep(delay)

        turtle.Terminator()
