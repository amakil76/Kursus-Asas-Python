#Bunga bulat
import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(36):  # Ulang 36 kali
    t.circle(50)
    t.right(10)  # Pusing sedikit untuk corak bunga

turtle.done()
