import turtle, math

turtle.tracer(0)
hr = turtle.Turtle()
hr.speed(0)
hr.ht()
hr.width(0)
hr.up()
hr.goto(0, -500)
hr.down()
hr.left(90)


def tree(i, angle):
    if i <= 2:
        return
    else:
        hr.forward(i)
        hr.left(angle)
        tree(i / math.sqrt(2), angle)
        hr.right(angle * 2)
        tree(i / math.sqrt(2), angle)
        hr.left(angle)
        hr.backward(i)

tree(300, 45)
turtle.update()
turtle.done()
