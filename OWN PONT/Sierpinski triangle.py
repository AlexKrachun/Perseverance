import turtle

turtle.tracer(0)
hr = turtle.Turtle()
hr.speed(0)
hr.width(1)
hr.ht()
hr.up()
hr.goto(-450, -400)
hr.right(90)
hr.down()
hr.left(90)


def tree(i):
    if i < 3:
        return
    else:
        for n in range(3):
            hr.forward(i)
            hr.left(120)
            tree(i / 2)


tree(900)
turtle.update()
turtle.done()
