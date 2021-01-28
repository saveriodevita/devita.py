import tkinter as tk 
from tkinter import *
import matplotlib as plt 
from random import randint
import string
import numpy as np
import matplotlib.pyplot as plt
import os 
from PIL import Image 
from PIL import ImageTk

def grafici():
    f = open("dati.txt", 'r')

    coordinateX = []
    coordinateY = []

    for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n') 
        valori = valori.split(',')  
        valori = list(valori)       
        print(valori)
        coordinateX.append(int(valori[0])) 
        coordinateY.append(int(valori[1])) 

    f.close()  

    print ("X: ",coordinateX)
    print ("Y: ",coordinateY)

    coordinateX.sort()
    coordinateY.sort()

    print("liste ordinate:") 
    print ("X: ",coordinateX)
    print ("Y: ",coordinateY)

    print(type(coordinateX))
    print(type(coordinateY))

    plt.plot(coordinateX,coordinateY)
    plt.ylabel('some numbers')
    plt.savefig("immagine_grafico.jpg")
   
def Scrittore():
    f = open("dati.txt", 'w')
    coppia = ""
    for x in range(100):
        for y in range(1):
            coppia = coppia + str(randint(1,100)) + "," + str(randint(1,100))
        coppia = coppia + "\n"
    print(coppia)
    f.write(coppia)
    f.close()

def creafile():
    if box_di_testo.get():
        nome=box_di_testo.get()
        Scrittore()
        grafici()
        os.rename('dati.txt',nome)
        foto_grafico= tk.PhotoImage(file='immagine_grafico.jpg')
        foto= tk.Label(interfaccia, foto_grafico.pack, side=BOTTOM)
        

    else:
        errore= tk.Label(interfaccia, text=("Inserisci un nome!"), font=("helvetica",40), background="red")
        errore.grid(row=3, pady=30)

interfaccia = tk.Tk()
interfaccia.geometry("900x550")
interfaccia.title("Grafici_matplotlib_gui")
interfaccia.grid_columnconfigure(0, weight=1) 

inserisci_nome = tk.Label(interfaccia, text="Dai un nome al file con le coppie:", font=("helvetica", 20))
inserisci_nome.grid(row=0, column=0, sticky="N", padx=20, pady=10)

box_di_testo= tk.Entry(width=60)
box_di_testo.grid(row=1, column=0, padx=20)

bottone_crea_file = tk.Button(text=("Crea file"), command=creafile)
bottone_crea_file.grid(row=2, column=0, padx=20)

interfaccia.mainloop()
