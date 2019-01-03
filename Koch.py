# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma per generare frattali tramite L-system

from turtle import Screen, Turtle, setup

W = 840
H = 600
num_steps = 4 

if __name__ == "__main__":

    axiom = "A"
    rules = {"A":"A+A-A-A+A", "+":"+","-":"-"}

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

    uga.speed(13)
    # traccia la riga dell'asse delle ascisse
    uga.penup()                    #tira su la penna
    uga.goto(-W/2+10,-H/2+10)            #spostati sul bordo in basso a sinistra
    uga.pendown()                  #metti la penna sul foglio


    for s in output:
        if s == 'A':
            uga.forward(10)
        elif s == '+':
            uga.left(90)          
        elif s == '-':
            uga.right(90)     

    myWin.exitonclick()  #aspetta il click del mouse
