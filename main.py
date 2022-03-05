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
snakeHead.shapesize(0.50, 0.50)
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

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black')
food.shapesize(0.50, 0.50)
food.penup()
food.goto(80,0)


def main():
    while True:
        screen.update()
        move()
        time.sleep(0.30)
        screen.listen()
        screen.onkey(goUp, 'Up' )
        screen.onkey(goDown, 'Down')
        screen.onkey(goRight, 'Right')
        screen.onkey(goLeft, 'Left')
        
main()











# turtle.speed(1)
# turtle.goto(10, 10)
# turtle.towards(0,0)
# turtle.position()
# turtle.forward(100)
# turtle.left(90)
# # turtle.setx(10)
# turtle.heading()
# # turtle.home()
# turtle.stamp()
# turtle.circle(50)
# turtle.forward(100)
 #hold screen 


