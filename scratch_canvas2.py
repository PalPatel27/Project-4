import turtle
length = 100
for i in range(10):
    while length <= 150:
        length += 0.5
        turtle.pencolor('red')
        turtle.right(89)
        turtle.forward(length)
        break
    length += 0.5
    turtle.pencolor('green')
    turtle.right(89)
    turtle.forward(length)
