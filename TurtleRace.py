from turtle import *
from random import randint

speed(20)
penup()  
goto(-140, 140) 
for step in range(15):
    write(step, align="center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bobo = Turtle()
bobo.color("blue")
bobo.shape("turtle")

bobo.penup()
bobo.goto(-160, 70)
bobo.pendown()

rasa = Turtle()
rasa.color("green")
rasa.shape("turtle")

rasa.penup()
rasa.goto(-160, 40)
rasa.pendown()

re = Turtle()
re.color("purple")
re.shape("turtle")

re.penup()
re.goto(-160, 10)
re.pendown()

for turn in range(100): 
    ada.forward(randint(1, 5))
    bobo.forward(randint(1, 5))
    rasa.forward(randint(1, 5))
    re.forward(randint(1, 5))
