"""
    Unit 21 [TurtleGraphics]


    import turtle as turtle
    angle = int(input("각 입력"))
    turtle.shape('turtle')
    for i in range(angle):
        turtle.forward(100)
        turtle.right(360/angle)

    turtle.exitonclick()


    import turtle as t
    n = 6
    t.shape("turtle")
    t.color('red')
    t.begin_fill()
    for i in range(n):
        t.forward(100)
        t.right(360/n)
    t.end_fill()


    import turtle as t
    t.shape("turtle")
    t.circle(120)


    import turtle as t
    n = 60
    t.shape("turtle")
    t.speed("fastest")
    for i in range(n):
        t.circle(120)
        t.right(360/n)

    t.exitonclick()


    import turtle as t
    t.shape("turtle")
    t.speed("fastest")
    for i in range(300):
        t.forward(i)
        t.right(91)

    t.exitonclick()
"""
import turtle as t
t.shape("turtle")
angle = int(input("angle : \n"))
length = int(input("length : \n"))

for i in range(angle):
    t.forward(length)
    t.right(360/angle*2)
    t.forward(length)
    t.left(360/angle)

t.exitonclick()