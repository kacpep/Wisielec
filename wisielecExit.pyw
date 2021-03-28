from tkinter import *
from tkinter import messagebox
import tkinter as tk
from wisielec import *

class WisielecExit(object):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Wisielec")
        self.root.geometry("800x600")
        self.font = ("Ariel" ,30,"bold")
        self.root.overrideredirect()
        self.root.iconbitmap("pliki/img/panther.ico")
        self.root.resizable(0,0)
       
        C = Canvas(self.root, height=800, width=600)
        background = PhotoImage( file = "pliki/img/tlo.png")
        background_label = Label(self.root, image=background)
        background_label.image = background
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #C = Canvas(self.root, height=800, width=600)
        #background = PhotoImage( file = "pliki/img/podgląd.png")
        ##background_label = Label(self.root, image=background)
        #background_label.image = background
        #background_label.place(x = 470, y = 15)

        lbl = Label(self.root, text = "Game Over!",font = self.font, fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 270, y = 10, width = 250, height = 50)

        lbl = Label(self.root, text = "Rekord:",font = self.font, fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 20, y = 150, width = 175, height = 50)

        lbl = Label(self.root, text = "Twój wynik:",font = self.font, fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 20, y = 230, width = 225, height = 50)

        lbl = Label(self.root, text = "Odgadnięte słowa:",font = self.font, fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 20, y = 310, width = 355, height = 50)

        lbl = Label(self.root, text = "Nie odgadnięte słowa:",font = self.font, fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 20, y = 390, width = 420, height = 50)

        lbl = Label(self.root, text = "Gra autorstwa Kacper Ostrowski wszelkie prawa zastrzeżone (c)",font = ("Ariel" ,10), fg = "black", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 200, y = 550, width = 420, height = 30)

        

        self.score()
        self.win()
        self.lost()
        self.record()

    def score(self):
        plik = open('pliki\pliki\score', 'r')
        try:
            self.liczba = plik.read()
        finally:
             plik.close()
    
        lbl = Label(self.root, text = self.liczba,font = self.font, fg = "black", bg = "white",bd = 2, relief = "solid")
        lbl.place(x = 250, y = 230, width = 210, height = 50)

    def win(self):
        plik = open('pliki\pliki\win', 'r')
        try:
            win = plik.read()
        finally:
            plik.close()
             
        lbl = Label(self.root, text = win,font = self.font, fg = "black", bg = "white",bd = 2, relief = "solid")
        lbl.place(x = 380, y = 310, width = 150, height = 50)

    def lost(self):
        plik = open('pliki\pliki\lost', 'r')
        try:
            lost = plik.read()
        finally:
            plik.close()
        lbl = Label(self.root, text = lost,font = self.font, fg = "black", bg = "white",bd = 2, relief = "solid")
        lbl.place(x = 445, y = 390, width = 150, height = 50)
    
    def run(self):
        self.root.mainloop()

    def record(self):
        plik = open('pliki\pliki\plik', 'r')
        try:
            rekord = plik.read()
        finally:
             plik.close()
        lbl = Label(self.root, text = rekord,font = self.font, fg = "black", bg = "white",bd = 2, relief = "solid")
        lbl.place(x = 200, y = 150, width = 210, height = 50)

if __name__ == '__main__':
    wisielec = WisielecExit()
    wisielec.run()

