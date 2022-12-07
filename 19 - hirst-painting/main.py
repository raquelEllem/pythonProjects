# obtem a lista de cores baseado na imagem

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (139, 27, 49), (222, 206, 109), (132, 176, 202), (45, 55, 103), (158, 46, 83), (169, 159, 39), (129, 189, 143), (83, 20, 44), (38, 43, 66), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (79, 153, 164), (195, 79, 73), (161, 201, 219), (45, 74, 77), (79, 74, 44), (58, 125, 122), (218, 176, 188), (167, 206, 169), (219, 182, 168)]

#start no lugar certo
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    #sobe uma linha e desenha
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

