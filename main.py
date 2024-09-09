import random
import turtle as t

from PIL.ImImagePlugin import number
from PIL.ImageChops import screen

# import colorgram
# colors = colorgram.extract('hirst-1.jpg', 30)

# rgb_colors = []
# for color in colors:
#    r = color.rgb.r
#    g= color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)
tadpole = t.Turtle()
tadpole.speed("fastest")
tadpole.penup()
tadpole.hideturtle()
color_list = [(230, 228, 224), (198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

tadpole.setheading(225)
tadpole.forward(350)
tadpole.setheading(0)
num_of_dots=120
for dot_count in range(1,num_of_dots+1):
    tadpole.dot(15, random.choice(color_list))
    tadpole.forward(40)
    if dot_count % 12 == 0:
        tadpole.setheading(90)
        tadpole.forward(40)
        tadpole.setheading(180)
        tadpole.forward(480)
        tadpole.setheading(0)



screen= t.Screen()
screen.exitonclick()