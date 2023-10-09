import math
import turtle

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * \
           math.cos(2 * t) - 2 * \
           math.cos(3 * t)

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

# Agrega una frase en la ventana
frase = turtle.Turtle()
frase.penup()
frase.goto(0, 250)  # Posición de la frase
frase.color('white')  # Color del texto
frase.hideturtle()   # Oculta el cursor de la tortuga

frase2 = turtle.Turtle()
frase2.penup()
frase2.goto(0, 300)  # Posición de la frase
frase2.color('white')  # Color del texto
frase2.hideturtle()   # Oculta el cursor de la tortuga

frase.write("TE AMO MI AMOR ", align="center", font=("Algerian", 20, "normal"))
frase2.write("SUERTE EN TUS EXAMENES", align="center", font=("Algerian", 20, "normal"))

for i in range(2550):
    t.goto(xt(i) * 20, yt(i) * 20)
    t.pencolor('red')

t.goto(0, 0)

turtle.done()
