import turtle, math
hr=turtle.Turtle()
hr.speed(0)
hr.ht()
hr.width(0)
hr.up()
hr.goto(0,-600)
hr.down()
hr.left(90)
def tree(i):
    if i<=1.5:
        return
    else:
        hr.forward(i)
        hr.left(45)
        tree(i/math.sqrt(2))
        hr.right(90)
        tree(i/math.sqrt(2))
        hr.left(45)
        hr.backward(i)
tree(400)
turtle.done()
