from tkinter import *
from turtle import left
#tout est commenté => Romain meilleur dev 

fenetre = Tk()
fenetre.geometry("400x600")
fenetre.iconbitmap("style/reveil.ico")
fenetre.title(string='SmartClock3000') # titre de la page

#création des trois sous frame principales : (voir maquette.png)

#niveau 1
frameNiv1 = Frame(fenetre,height=250, borderwidth=2,bg='red')
frameNiv1.pack(fill=X)

frameEfreiClock = Frame(frameNiv1,width=150,height=130, borderwidth=2,bg='purple')
frameEfreiClock.pack(side=RIGHT)

frameTempsAvtAlarme = Frame(frameNiv1,width=200,height=130, borderwidth=2,bg='orange')
frameTempsAvtAlarme.pack(side=LEFT)

#niveau 2
frameNiv2 = Frame(fenetre,height=150,borderwidth=2,bg="blue")
frameNiv2.pack(fill=X)

#niveau 3
frameNiv3 = Frame(fenetre,height=300,borderwidth=2,bg="green")
frameNiv3.pack(fill=X)



fenetre.mainloop()