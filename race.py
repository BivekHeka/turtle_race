from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=1000, height=600)
user_bet=screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter the color: ")
colors=["red","blue","green","yellow","black","orange","purple"]
y_position=[-150,-100,-50,0,50,100,150]
all_turtles=[]

for turtle_index in range (0,7):
    tim=Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-485,y=y_position[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on=True
    
while is_race_on:


    for turtle in all_turtles:
        distance=random.randint(0,10)
        turtle.forward(distance)

        if turtle.xcor()>490:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")   



# tom=Turtle()
# tom.penup()
# tom.goto(x=-485,y=-100)

# bob=Turtle()
# bob.penup()
# bob.goto(x=-485,y=-50)

# tam=Turtle()
# tam.penup()
# tam.goto(x=-485,y=0)

# pop=Turtle()
# pop.penup()
# pop.goto(x=-485,y=50)

# bab=Turtle()
# bab.penup()
# bab.goto(x=-485,y=100)

# lam=Turtle()
# lam.penup()
# lam.goto(x=-485,y=150)

screen.exitonclick()






