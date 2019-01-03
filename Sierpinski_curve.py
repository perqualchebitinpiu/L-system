# Author: Alfonso Breglia
# Email:  perqualchebitinpiu@gmail.com
# Date:   27/12/2018
# Description: programma per generare frattali tramite L-system

from turtle import Screen, Turtle, setup

W = 840     #larghezza della finestra di visualizzazione
H = 600     #altezza  della finestra di visualizzazione

num_steps = 7 #numero di volte  in cui applicano le regole

if __name__ == "__main__":

    axiom = "A"         #assioma di partenza del L-System
    rules = {"A":"B-A-B","B":"A+B+A" ,"+":"+","-":"-"}  #Regole 

    start_point = axiom
    print(start_point)
    for t in range(num_steps):
        output = ""             #striga di uscita di questo passo 
        for s in start_point:   #per ogni carattere nella stringa di questo passo
            output += rules[s]  #prendi dal dizionario la stringa sostitutiva del carattere
        start_point  =  output  #il nuovo punto di partenza della prossima iterazione 
                                #è il risultato di quella corrente
        print(output)           #stampa il passo corrente



    setup(W,H)              #fissa le dimensioni dello schermo a 600 x 600 pixel
    myWin = Screen()        #crea lo schermo con il foglio da disegno 
    uga = Turtle()          #popola il foglio con la tartaruga uga

    uga.speed(20)           #aumenta la velocità della tartaruga
    # traccia la riga dell'asse delle ascisse
    uga.penup()                    #tira su la penna
    uga.goto(-W/2+10,-H/2+10)            #spostati sul bordo in basso a sinistra
    uga.pendown()                  #metti la penna sul foglio


    for s in output:
        if s == 'A' or s == "B":    #se trovi A o B 
            uga.forward(5)          #avanza di 5
        elif s == '-':              
            uga.left(60)            #ruota di 60° a sinistra
        elif s == '+':
            uga.right(60)           #ruota di 60° a destra

    myWin.exitonclick()  #aspetta il click del mouse
