import turtle, math
turtle.tracer(0)
p = turtle.Turtle()
p.ht()
p.speed(0)
a = math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(2))))))))))))
def dlog(i):
    if i<=0.8:
        return
    else:
        p.circle(i,-90)
        dlog(i/(a))
        p.up()
        p.left(180)
        p.circle(i, -90)
        p.down()
        dlog(i/(a**2))

def gold(i):
    if i >= 1000:
        return
    else:
        p.circle(i,90)
        gold(i * a)
        dlog(i)


gold(1)
turtle.update()
turtle.done()
