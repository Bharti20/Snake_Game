from ast import arg
import random
import turtle
import tkinter as TK
import time

# screen
screen = turtle.Screen()
screen.setup (width=600, height=600, startx=0, starty=0)
screen.title('Snack Game')
screen.bgcolor('green')
# screen.tracer(1)

    
 #snake part
snakeHead = turtle.Turtle()
snakeHead.shape("square")
snakeHead.color('black')
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = 'stop'

# score board
scores = 0
high_scores = 0
board = turtle.Turtle()
board.speed(0)
board.color('white')
board.penup()
board.hideturtle()
board.goto(0,240)
board.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

def move():
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
food.penup()
food.goto(0,0)

#Increase snake body length
snake_list = []
delay = 0.15
while True:
    screen.update()
    time.sleep(delay)
    if snakeHead.distance(food)<15:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x, y)
        new_snake = turtle.Turtle()
        new_snake.speed(0)
        new_snake.shape('square')
        new_snake.color('grey')
        new_snake.penup()
        snake_list.append(new_snake)
        
        scores = scores+10
        if scores > high_scores:
            high_scores = scores
        board.clear()
        board.write("score: {} High Score: {}".format(scores, high_scores), align="center", font=("Courier", 24, "normal"))

    for i in range(len(snake_list)-1, 0,-1):
        x = snake_list[i-1].xcor()    
        y = snake_list[i-1].ycor()
        snake_list[i].goto(x,y)
    
    if len(snake_list)>0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        snake_list[0].goto(x,y)

    #Border Collisions
    if snakeHead.xcor()> 290 or snakeHead.xcor()< -290 or snakeHead.ycor()>290 or snakeHead.ycor() <-290:
        time.sleep(1)
        snakeHead.goto(0,0)
        snakeHead.direction = 'stop'
        
        for s in snake_list:
            s.goto(1000, 1000)
        snake_list.clear()
        scores = 0
        high_scores =0
        board.clear()
        board.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

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


    
