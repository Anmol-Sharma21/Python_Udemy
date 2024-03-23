# from turtle import *
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#
import random
import turtle

# from turtle import Turtle, Screen
# tt_turtle_obj = Turtle()
#
# for _ in range(15):
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.penup()
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.pendown()
#
# screen = Screen()
# screen.exitonclick()


# from turtle import Turtle, Screen
# tim=Turtle()
#
# colour=[]
#
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range (num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_n in range(3,11):
#     draw_shape(shape_n)
#
# screen = Screen()
# screen.exitonclick()
#


from colorgram import *

rgb_colors = []

colors = colorgram.extract('download.jpeg', 40)

for color in colors:

    r= color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors=(r,g,b)
    rgb_colors.append(new_colors)

print(rgb_colors)

from turtle import *
import random

turtle.colormode(255)
tim = Turtle()
colors_list = [(168, 79, 36), (240, 224, 83), (212, 153, 90), (48, 36, 28), (143, 28, 41), (24, 24, 65), (44, 43, 117), (150, 54, 85), (55, 87, 150), (130, 160, 212), (163, 22, 18), (205, 87, 128), (26, 39, 28), (142, 180, 141), (209, 83, 65), (65, 30, 35), (115, 108, 194), (196, 131, 157), (78, 116, 63), (162, 178, 228), (156, 209, 190), (84, 149, 114), (78, 84, 34), (190, 133, 57), (65, 147, 168), (56, 100, 22), (250, 221, 2), (227, 172, 185), (231, 174, 166), (168, 206, 211)]

tim.speed('fast')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots=100
for dot_count in range(1, num_dots + 1 ):

    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()




















