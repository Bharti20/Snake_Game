from ast import arg
import random
import turtle
import tkinter as TK
import time

# screen
screen = turtle.Screen()
screen.setup (width=500, height=400, startx=0, starty=0)
screen.title('Snack Game')
screen.bgcolor('green')
# screen.tracer(1)

    
 #snake part
snakeHead = turtle.Turtle()
snakeHead.shape("square")
snakeHead.color('black')
snakeHead.shapesize(0.60, 0.60)
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = 'stop'

#score board
# board = turtle.Turtle()
# board.shape('square')
# board.color('brown')
# board.write('Score:0 High score:0', align='left', font=("Arial", 20, "normal"))


def move():
    print('moveeeeeeeeeee')
    if snakeHead.direction == "up":
        y = snakeHead.ycor() #y coordinate of the turtle
        snakeHead.sety(y + 20)
 
    if snakeHead.direction == "down":
        y = snakeHead.ycor() #y coordinate of the turtle
        snakeHead.sety(y - 20)
 
    if snakeHead.direction == "right":
        x = snakeHead.xcor() #y coordinate of the turtle
        snakeHead.setx(x + 20)
 
    if snakeHead.direction == "left":
        x = snakeHead.xcor() #y coordinate of the turtle
        snakeHead.setx(x - 20)

def goUp():
    print('uppppppp')
    if snakeHead.direction != "down":
        snakeHead.direction = "up"

def goDown():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

def goRight():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
def goLeft():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"


screen.listen()
screen.onkey(goUp, 'Up' )
screen.onkey(goDown, 'Down')
screen.onkey(goRight, 'Right')
screen.onkey(goLeft, 'Left')

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.shapesize(0.50, 0.50)
food.penup()
food.goto(0,0)

#Increase snake body length
snake_list = []
delay = 0.15
while True:
    screen.update()
    # move()
    time.sleep(delay)
    if snakeHead.distance(food)<15:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x, y)
        new_snake = turtle.Turtle()
        new_snake.speed(0)
        new_snake.shapesize(0.70, 0.70)
        new_snake.shape('square')
        new_snake.color('white')
        new_snake.penup()
        snake_list.append(new_snake)

    for i in range(len(snake_list)-1, 0,-1):
        x = snake_list[i-1].xcor()    
        y = snake_list[i-1].ycor()
        snake_list[i].goto(x,y)
    
    if len(snake_list)>0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        snake_list[0].goto(x,y)
    move()
    for b in snake_list:
        if b.distance(snakeHead) < 20:
            time.sleep(1)
            snakeHead.goto(0,0)
            snakeHead.direction ='stop'

            for b in snake_list:
                b.ht()
            snake_list.clear()
            delay = 0.1
    time.sleep(delay)


    
