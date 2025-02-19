import turtle  

# Tetapkan skrin
skrin = turtle.Screen()
skrin.title("Lukis Rumah dengan Turtle")

# Tetapkan pen (kura-kura)
pen = turtle.Turtle()
pen.speed(3)  # Kelajuan sederhana

# 🎯 1. Lukis Dinding Rumah (Segi Empat)
pen.penup()
pen.goto(-50, -50)  # Pergi ke kedudukan permulaan
pen.pendown()
pen.begin_fill()
pen.color("blue")  # Warna dinding
for _ in range(4):
    pen.forward(100)  # Panjang sisi
    pen.left(90)  
pen.end_fill()

# 🎯 2. Lukis Bumbung (Segi Tiga)
pen.penup()
pen.goto(-50, 50)  # Pergi ke atas dinding
pen.pendown()
pen.begin_fill()
pen.color("red")  # Warna bumbung
pen.goto(0, 100)  # Atas segi tiga
pen.goto(50, 50)  # Kanan bumbung
pen.goto(-50, 50)  # Kembali ke asal
pen.end_fill()

# Sembunyikan pen dan tamatkan
pen.hideturtle()
turtle.done()
