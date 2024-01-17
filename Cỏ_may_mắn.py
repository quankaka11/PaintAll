import turtle  


def heart1(color,size,x,t) :
    # t = turtle.Turtle()

    t.color(color)
    t.pensize(size)

    t.left(50+x)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
