# from turtle import *
#
# my_turtle = Turtle()
# my_turtle.speed(0)
# my_turtle.screen.setup(1200, 800)
#
# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(100)
#
# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(1)
#
# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# my_turtle.screen.mainloop()

'''Мое животное ("Голова голодной кошки над твоим лицом в 5-00")'''
import turtle

# Создание экземпляра черепашки
t = turtle.Turtle()

# Рисование формы животного (кошки)
t.fillcolor("gray")
t.begin_fill()
t.circle(50)  # голова
t.end_fill()

t.penup()
t.goto(-30, 20)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)  # левый глаз
t.end_fill()

t.penup()
t.goto(30, 20)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)  # правый глаз
t.end_fill()

t.penup()
t.goto(0, -10)
t.pendown()
t.width(5)
t.goto(0, -30)  # нос

t.penup()
t.goto(-20, -40)
t.pendown()
t.width(3)
t.goto(-30, -70)  # левое ухо

t.penup()
t.goto(20, -40)
t.pendown()
t.width(3)
t.goto(30, -70)  # правое ухо

# Скрытие черепашки
t.hideturtle()

# Завершение рисования
turtle.done()
