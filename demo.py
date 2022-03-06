    # if snakeHead.xcor()>290:
    #     snakeHead.setx(-290)
    # if snakeHead.xcor()> -290:
    #     snakeHead.setx(290)
    # if snakeHead.ycor()>290:
    #     snakeHead.sety(-290)
    # if snakeHead.ycor()> -290:
    #     snakeHead.sety(290)

a = []
x = 0
b = 0
while b <10:
    if len(a) <15:
        x= x+1
        a.append(x)
        # print(a)

    for i in a:
        print(i)
    b = b+1