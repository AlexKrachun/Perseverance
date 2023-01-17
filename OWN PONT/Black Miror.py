import turtle, threading
from random import randint, uniform

p = turtle.Turtle()
p.speed(0)
p.width(4)
p.ht()

DirectionVecLength = 10000
TeakLength = 10


def PrintLine(Line):  ####
    # Рисуем отрезок
    p.goto(Line[0][0], Line[0][1])
    p.down()
    p.color(uniform(0.1, 1), uniform(0.1, 1), uniform(0.1, 1))
    p.goto(Line[1][0], Line[1][1])
    p.up()


def Paint(ListLines):  ####
    # Отрисовываем все отрезки
    p.up()
    for Line in ListLines:
        PrintLine(Line)
    p.up()


def Cross(A, B):  ####
    # находит точку пересечения двух отрезков А и В
    # если пересечение найдено, то возращает TRUE, координаты точки пересечения
    # если пересечение не найдено, то возращает FALSE

    tmp = (A[0][0] - A[1][0]) * (B[0][1] - B[1][1]) - (A[0][1] - A[1][1]) * (B[0][0] - B[1][0])

    if tmp == 0:
        return False, 0
    else:
        xp = ((A[0][0] * A[1][1] - A[0][1] * A[1][0]) * (B[0][0] - B[1][0]) - (A[0][0] - A[1][0]) * (
                    B[0][0] * B[1][1] - B[0][1] * B[1][0])) / tmp
        yp = ((A[0][0] * A[1][1] - A[0][1] * A[1][0]) * (B[0][1] - B[1][1]) - (A[0][1] - A[1][1]) * (
                    B[0][0] * B[1][1] - B[0][1] * B[1][0])) / tmp

        xp = round(xp, 5)
        yp = round(yp, 5)

        if ((A[0][0] <= xp <= A[1][0] or A[0][0] >= xp >= A[1][0]) and (
                A[0][1] <= yp <= A[1][1] or A[0][1] >= yp >= A[1][1])) and (
                ((B[0][0] <= xp <= B[1][0] or B[0][0] >= xp >= B[1][0]) and (
                        B[0][1] <= yp <= B[1][1] or B[0][1] >= yp >= B[1][1]))):
            return True, xp, yp
        else:
            return False, 0


def CrossAll(ListLines, Obj):
    # находит ближайшую точку пересечения среди всех прямых, кроме ExeptLine
    # если пересечение найдено, то возращает TRUE, координаты точки пересечения и прямую
    # если пересечение не найдено, то возращает FALSE

    bRes = False
    Per = []
    min = 1e9
    mx, my = 0, 0
    lineRes = []

    # Определяем координаты завершения отрезка
    EndPos = Obj.EndPoint()

    for line in ListLines:
        if line != Obj.ExeptLine:
            Per = list(Cross(line, [[Obj.Pos[0], Obj.Pos[1]], [EndPos[0], EndPos[1]]]))
            if Per[0]:
                tmp1 = ((Obj.Pos[0] - Per[1]) ** 2 + (Obj.Pos[1] - Per[2]) ** 2) ** 0.5
                if tmp1 < min:
                    min = tmp1
                    bRes = True
                    mx, my = Per[1], Per[2]
                    lineRes = line
    return bRes, mx, my, lineRes


def Reflex(B, Line):
    # Возвращает координаты точки отражения точки В относительно прямой Line
    m = Line[1][0] - Line[0][0]
    p = Line[1][1] - Line[0][1]
    t = (m * B[0] + p * B[1] - m * Line[0][0] - p * Line[0][1]) / (m ** 2 + p ** 2)
    xm = m * t + Line[0][0]
    ym = p * t + Line[0][1]
    return 2 * xm - B[0], 2 * ym - B[1]


class Ball():
    def __init__(self, Pos, Vec, Length):
        self.Pos = Pos  # Координаты точки
        self.Vec = Vec  # Вектор движения длиной DirectionVecLength
        self.Length = Length  # Длина перемещения в такте

        k = DirectionVecLength / (self.Vec[0] ** 2 + self.Vec[1] ** 2) ** 0.5
        self.Vec[0] *= k
        self.Vec[1] *= k

        self.move = turtle.Turtle()
        self.move.speed(0)
        # self.move.up()
        self.move.shape("circle")
        self.move.color(uniform(0.2, 1), uniform(0.2, 1), uniform(0.2, 1))

    ExeptLine = [[0, 0], [0, 0]]  # Последня прямая пересечения

    def EndPoint(self):
        # Возвращает координату последней точки отрезка перемещения
        k = self.Length / DirectionVecLength
        return [self.Pos[0] + self.Vec[0] * k, self.Pos[1] + self.Vec[1] * k]


def RefEnd(Obj, ListLines):
    global DirectionVecLength, TeakLength

    # Ищем ближйшую точку пересечения объекта и прямых из ListLines
    Confluence = list(CrossAll(ListLines, Obj))  # Определяем отрезок точку пересечения

    if Confluence[0]:  # Если пересечение есть:
        # Устанавливаем последнюю линию пересечени в объект
        Obj.ExeptLine = Confluence[3]

        # Рассчитываем расстояние от точки объекта до точки перечечения
        Distance = ((Obj.Pos[0] - Confluence[1]) ** 2 + (Obj.Pos[1] - Confluence[2]) ** 2) ** 0.5

        # Строим отражение вектора направления
        RefPos = Reflex([Obj.Pos[0] + Obj.Vec[0], Obj.Pos[1] + Obj.Vec[1]], Obj.ExeptLine)

        # Формируем новый вектор направления
        Obj.Vec[0] = RefPos[0] - Confluence[1]
        Obj.Vec[1] = RefPos[1] - Confluence[2]

        # Масштабируем вектор направлени до длины DirectionVecLength
        k = DirectionVecLength / (Obj.Vec[0] ** 2 + Obj.Vec[1] ** 2) ** 0.5
        Obj.Vec[0] *= k
        Obj.Vec[1] *= k

        # Устанавливаем новую координату объекта
        Obj.Pos[0] = Confluence[1]
        Obj.Pos[1] = Confluence[2]

        # Рисуем объект
        Obj.move.goto(Obj.Pos[0], Obj.Pos[1])

        # Проверяем, находится ли конечная точка на пересекаемой прямой
        if Obj.Length == Distance:
            # Конечная точка лежит на прямой
            # Устанавливаем в объекте полную длину перемещения за такт
            Obj.Length = TeakLength

        else:
            # Конечная точка лежит за прямой
            # Уменьшаем оставшуюся длину до конца тика
            Obj.Length -= Distance

            # Рекурсивно вызываем функцию для посторения следующего отрезка
            Obj = RefEnd(Obj, ListLines)
    else:
        # Пересечения не было
        # Обнуляем последнюю линию пересечения
        Obj.ExeptLine = [[0, 0], [0, 0]]

        # Вектор движения не изменяется
        # Определяем координаты завершения отрезка
        EndPos = Obj.EndPoint()

        # Устанавливаем новую координату объекта
        Obj.Pos[0] = EndPos[0]
        Obj.Pos[1] = EndPos[1]

        # Устанавливаем в объекте полную длину перемещения за такт
        Obj.Length = TeakLength

        # Рисуем объект
        Obj.move.goto(Obj.Pos[0], Obj.Pos[1])

    return Obj


def Printer(n):
    # Создаем массив линий
    xRect, yRect = 600, 300  # Координаты вершины прямоуголбника

    ListLines = [[[randint(-xRect, xRect), randint(-yRect, yRect)] for i in range(2)] for i in range(n)]
    ListLines.append([[xRect, yRect], [xRect, -yRect]])
    ListLines.append([[xRect, -yRect], [-xRect, -yRect]])
    ListLines.append([[-xRect, -yRect], [-xRect, yRect]])
    ListLines.append([[-xRect, yRect], [xRect, yRect]])

    # Избражаем все линии
    Paint(ListLines)
    return ListLines


def Fly(ObjNum):
    global LisLines
    Object = [Ball([0, 0], [randint(-100, 100), randint(-100, 100)], 1) for i in range(ObjNum)]

    while True:
        for i in range(ObjNum):
            Object[i] = RefEnd(Object[i], ListLines)


ThreadNum = 1  # Количество потоков
ObjNum = 20  # Количество обьектов в одном потоке
LineNum = 10  # Количество отрезков

ListLines = Printer(LineNum)
ListThreads = []
for i in range(ThreadNum):
    ListThreads.append(threading.Thread(target=Fly, args=(ObjNum,), daemon=True))
    ListThreads[i].start()

turtle.done()
