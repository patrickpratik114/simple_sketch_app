from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def move_back():
    tim.back(10)


def clear_s():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_back, "s")
screen.onkey(clear_s, "c")

screen.exitonclick()