import turtle,datetime
def drawDp():
    turtle.penup()
    turtle.fd(10)
    turtle.seth(-90)
    turtle.fd(50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(2,360)
    turtle.end_fill()
    turtle.penup()
    turtle.bk(50)
    turtle.seth(0)
    turtle.fd(20)
def drawGap():
    turtle.penup()
    turtle.fd(7)
def drawline(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d):
    drawline(True) if d in[2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in[0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in[0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in[0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in[0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in[0,2,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in[0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i=='-':
            turtle.write('年',font=('楷体',35,"bold"))
            turtle.pencolor("blue")
            turtle.fd(50)
        elif i=='=':
            turtle.write('月',font=('楷体',35,"bold"))
            turtle.pencolor("yellow")
            turtle.fd(50)
        elif i=='+':
            turtle.write('日',font=('楷体',35,"bold"))
        elif i=='.':
            drawDp()
            turtle.pencolor('black')
        else:
            drawDigit(eval(i))
def main():
    i=input("请输入输入格式类似于‘2018-05=13+’或以小数点分隔的日期：")
    turtle.setup(800,350,300,300)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(6)
    drawDate(i)
    turtle.hideturtle()
main()
