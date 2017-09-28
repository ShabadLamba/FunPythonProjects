__author__ = 'shabadlamba'

import turtle
#import random

def draw_shapes():
#bring a screen
    window = turtle.Screen()
    window.bgcolor("blue")

#making a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(8)
    brad.tracer(None,5)
    brad.angle = 0
    graph = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    for j in graph:
        for i in range(0,4):
            brad.forward(100)
            brad.right(90)
            #brad.forward(100)
        brad.right(10)

        window.exitonclick()

draw_shapes()