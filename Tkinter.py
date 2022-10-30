from tkinter import *
from turtle import left
#tout est commenté => Romain meilleur dev 

fenetre = Tk()
fenetre.iconbitmap("style/reveil.ico")
fenetre.title(string='SmartClock3000') # titre de la page

#création des sous frame principales : (voir maquette.png)

#containerRight 
frameRIGHT = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameRIGHT.pack(side=RIGHT, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameRIGHT, text="Frame right").pack(padx=10, pady=10)


#containerLeft
frameLeft = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameLeft.pack(side=LEFT, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameLeft, text="Frame Left").pack(padx=10, pady=10)

#Les sous container de Left
frameEfreiLogo = Frame(frameLeft, borderwidth=2, relief=GROOVE)
frameEfreiLogo.pack(side=TOP, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameEfreiLogo, text="Frame Logo Efrei").pack(padx=10, pady=10)

frameTRAA = Frame(frameLeft, borderwidth=2, relief=GROOVE) # TRAA = Temps restant avant alarme
frameTRAA.pack(side=BOTTOM, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameTRAA, text="Frame TRAA").pack(padx=10, pady=10)

fenetre.mainloop()