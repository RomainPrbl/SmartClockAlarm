from tkinter import *
from turtle import left
from PIL import ImageTk, Image
import GetData

fenetre = Tk()
fenetre.geometry('750x250')
fenetre.iconbitmap("style/reveil.ico")
fenetre.title(string='SmartClock3000') # titre de la page

#containerRight 
frameRIGHT = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameRIGHT.pack(side=RIGHT, padx=5, pady=5,expand=True,fill=BOTH)

#Creation des sous containers Right:
frameStatus = Frame(frameRIGHT, borderwidth=2, relief=GROOVE)
frameStatus.pack(side=TOP, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameStatus, text="Status de la connection :").pack(padx=10, pady=10)
Label(frameStatus, text="connecte").pack()

frameAlarmeDate = Frame(frameRIGHT, borderwidth=2, relief=GROOVE)
frameAlarmeDate.pack(side=BOTTOM, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameAlarmeDate, text="La prochaine alarme et prevu pour : ").pack(padx=10, pady=10)
Label(frameAlarmeDate, text=str(GetData.recupererLeProchainCours()["start"])).pack()
#containerLeft
frameLeft = Frame(fenetre, borderwidth=2, relief=GROOVE)
frameLeft.pack(side=LEFT, padx=5, pady=5,expand=True,fill=BOTH)

#sous container de Left : 
frameEfreiLogo = Frame(frameLeft, borderwidth=2, relief=GROOVE)
frameEfreiLogo.pack(side=TOP, padx=5, pady=5,expand=True,fill=BOTH)

img = ImageTk.PhotoImage(Image.open("style/efrei_logo.png").resize((200,100)))
label = Label(frameEfreiLogo, image = img)
label.pack()

frameTRAA = Frame(frameLeft, borderwidth=2, relief=GROOVE) # TRAA = Temps restant avant alarme
frameTRAA.pack(side=BOTTOM, padx=5, pady=5,expand=True,fill=BOTH)
Label(frameTRAA, text="Temps restant avant la prochaine alarme :").pack(padx=10, pady=10)
Label(frameTRAA, text="2h 36min et 32s").pack()
fenetre.mainloop()