import turtle

layar = turtle.Screen()
layar.title("Persegi Warna-Warni")

kura = turtle.Turtle()
kura.pensize(5)

warna_sisi = ["red", "blue", "green", "yellow"]

for warna in warna_sisi:
    kura.pencolor(warna)
    kura.forward(100)
    kura.left(90)

turtle.done()
