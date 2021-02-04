from guizero import * 
import matplotlib as plt 
from random import randint
import string
import numpy as np
import matplotlib.pyplot as plt
import os 

def grafici():
    for riga in f:
        valori = str(riga)         
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordinateX.append(int(valori[0])) 
        coordinateY.append(int(valori[1]))  
    f.close()  

    coordinateX.sort()
    coordinateY.sort()
 
    plt.title("Grafico di dispersione", color='#007FFF')
    plt.ylabel('Asse Y')
    plt.xlabel('Asse X')
    plt.scatter(coordinateX,coordinateY)
    plt.ylabel('some numbers')
    plt.savefig("immagine_grafico.jpg")
   
def Scrittore():
    f = open("dati.txt", 'w')
    coppia = ""
    for x in range(100):
        for y in range(1):
            coppia = coppia + str(randint(1,100)) + "," + str(randint(1,100))
        coppia = coppia + "\n"
    f.write(coppia)
    f.close()

def creafile():
    if box_di_testo.value:
        nome=box_di_testo.value
        grafici()
        os.rename('dati.txt',nome)
        foto_grafico= Picture(interfaccia, image='immagine_grafico.jpg')      

    else:
        errore= Text(interfaccia, text=("Inserisci un nome!"), font=("helvetica",40), bg="red")

coordinateX = []
coordinateY = []
Scrittore()
f = open("dati.txt", 'r')

testo_titolo="Dai un nome al file con le coppie:"
interfaccia = App(title="Generatore file di cordinate", width=900, height=550, bg="#c0c0c0" )
inserisci_nome = Text(interfaccia, text=testo_titolo, font=("helvetica", 20))
box_di_testo= TextBox(interfaccia, width=60)
bottone_crea_file = PushButton(interfaccia, text=("Crea file"), command=creafile, width=10, height=2,)
interfaccia.display()