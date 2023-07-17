from extract_color import extract_colors
import turtle as turtle_module
import random

turtle_module.colormode(255)
color_list = extract_colors('image.jpg', 40)
# for this image the first  item is white, so I will start from the 3rd
final_colors = color_list[3:]

tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot in range(1, number_of_dots + 1):
    tim.dot(15, random.choice(final_colors))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
