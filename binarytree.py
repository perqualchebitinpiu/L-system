# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma per generare frattali tramite L-system

from turtle import Screen, Turtle, setup

W = 840
H = 600
num_steps = 8

if __name__ == "__main__":

    axiom = "0"
    rules = {"0":"1[0]0","1":"11", "[":"[","]":"]"}

    start_point = axiom

    for t in range(num_steps):
        output = ""
        for s in start_point:
            output += rules[s] 
        start_point  =  output

    print(output)

    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel
    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()          #popola il foglio con la tartaruga uga


    # traccia la riga dell'asse delle ascisse
    uga.speed(15)
    uga.penup()
    uga.setheading(90)

    uga.goto(0,-H/2)
    uga.pendown()
    stack = []

    for s in output:
        if s == '1':
            uga.forward(2)
        if s == '0':
            uga.forward(2)
        elif s == '[':
            stack.append((uga.pos(), uga.heading()))
            uga.left(45)          
        elif s == ']':
            pos, angle = stack.pop()
            uga.penup()
            uga.setheading(angle)
            uga.goto(pos[0],pos[1])
            uga.pendown()
            uga.right(45)
     

    myWin.exitonclick()  #aspetta il click del mouse
