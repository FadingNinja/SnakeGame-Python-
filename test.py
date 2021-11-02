import turtle
import time

screen = turtle.Screen()
screen.title("Snake Game")
turtle.bgcolor("turquoise")
screen.setup(width = 700, height = 700)
turtle.tracer(0)

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('dark green')
snake.direction = 'stop'
snake.penup()
snake.goto(0, 0)

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30, 30)

scoring = turtle.Turtle()
scoring.speed(0)
scoring.penup()
scoring.goto(0, 300)
scoring.color('black')
scoring.hideturtle()
scoring.write('Score : 0', align = 'center', font = ('times', 24, 'bold'))

score = 0
old_fruit = []
delay  = 0.1

def snake_go_up():
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

def snake_move() :
    if snake.direction == 'up' :
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == 'down' :
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == 'right' :
        x = snake.xcor()
        snake.setx(x + 20)
    elif snake.direction == 'left' :
        x = snake.xcor()
        snake.setx(x - 20)

screen.listen()
screen.onkeypress(snake_go_up, 'Up')
screen.onkeypress(snake_go_down, 'Down')
screen.onkeypress(snake_go_right, 'Right')
screen.onkeypress(snake_go_left, 'Left')

while True :
    screen.update()    
    snake_move()
    print(snake.direction)
    time.sleep(delay)