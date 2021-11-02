import turtle
import time
import random

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
snake.color('green')
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

def go_up() :
    if snake.direction != 'down' :
        snake.direction = 'up'
def go_down() :
    if snake.direction != 'up' :
        snake.direction = 'down'
def go_right() :
    if snake.direction != 'left' :
        snake.direction = 'right'
def go_left() :
    if snake.direction != 'right' :
        snake.direction = 'left'

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
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_right, 'Right')
screen.onkeypress(go_left, 'Left')

while True :
    screen.update()
    
    if snake.distance(fruit) < 20 :
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)

        fruit.goto(x, y)

        score += 1
        scoring.clear()
        scoring.write(f'Score : {score}', align = 'center', font = ('times', 24, 'bold'))

        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('dark green')
        new_fruit.penup()

        old_fruit.append(new_fruit)

    for index in range(len(old_fruit) - 1, 0, - 1) :
        x = old_fruit[index - 1].xcor()
        y = old_fruit[index - 1].ycor()

        old_fruit[index].goto(x, y)

    if len(old_fruit) > 0 :
        x = snake.xcor()
        y = snake.ycor()

        old_fruit[0].goto(x, y)

    snake_move()

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240 :
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write('    GAME OVER \n Your Score Is {}'.format(score), align = "center", font = ('Courier', 30, 'bold'))

    for food in old_fruit :
        if snake.distance(food) < 20 :
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0, 0)
            scoring.write('    GAME OVER \n Your Score Is {}'.format(score), align = "center", font = ('Courier', 30, 'bold'))

    time.sleep(delay)