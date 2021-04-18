import turtle
from math import sin,cos
p = turtle.Turtle()
p.ht()
p.speed(0)
p.width(0)

def Creator(n,PiecePast,angle):
    if n<=0:
        return PiecePast
    PieceFuture=PiecePast+f"\np.right({-angle})\n"+PiecePast+f"\np.right({2*angle})\n"+PiecePast+f"\np.right({-angle})\n"+PiecePast
    return Creator(n-1,PieceFuture,angle)

def Star(n,length,vertices):
    angle=360/vertices
    p.up()
    p.goto(-200, 200)
    p.down()
    length=((length/3**(n-1))/vertices)*2

    Piece = f"""p.forward({length})"""
    Piece=Creator(n,Piece,angle)

    for i in range(vertices//2+1):
        for Command in Piece.split():
            eval(Command)
        p.right(2*angle)

length=1000  # Размер одной стороны
deep=4       # Подробность прорисовки
Vertices=5   # Количество вершин n-угольной звезды
Star(deep,length,Vertices)
