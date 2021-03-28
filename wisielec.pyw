from tkinter import *
from tkinter import messagebox
import tkinter as tk
import random
import linecache
from wisielecExit import *

class Wisielec(object):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Wisielec")
        self.root.geometry("800x600")
        self.font = ("Ariel" ,20,"bold")
        self.font2 = ("Ariel" ,15,"bold")
        self.root.iconbitmap("pliki/img/panther.ico")
        self.font3 = ("Ariel" ,19,"bold")
        self.root.overrideredirect()
        self.root.resizable(0,0)
        #self.root["bg"] = "white"
        #self.root.iconbitmap(r'C:\Users\CYBERBACIA\Desktop\wisielec python\znak.ico')
        C = Canvas(self.root, height=800, width=600)
        background = PhotoImage( file = "pliki/img/tlo.png")
        background_label = Label(self.root, image=background)
        background_label.image = background
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        self.password = ""
        self.category = ""

        self.number = 0
        self.errors = 0
        self.letters_ok = 0
        self.win = 0
        self.lost = 0
        self.liczba = 0

        self.passLabels = []
        self.letters = []

        alphabet = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŻŹ"
        
        letterX = 10
        letterY = 260
        
        for letter in alphabet:
            lbl = Label(self.root, text = letter, font = self.font, fg = "black", bg = "white", bd = 2, relief = "solid")
            lbl.place(x = letterX, y = letterY, width = 35, height = 35)
            lbl.bind("<Button-1>", self.checkLetter)
            letterX += 40
            if (letterX > 405):
                letterY += 80
                letterX = 10
            self.letters.append(lbl)



        lbl = Label(self.root, text = "",font = self.font2, fg = "white", bg = "gold",bd = 1, relief = "solid")
        lbl.place(x = 0, y = 85, width = 400, height = 5)

        lbl = Label(self.root, text = "Wyjdź",font = self.font2, fg = "white", bg = "red", bd = 2, relief = "solid")
        lbl.place(x = 5, y = 560, width = 70, height = 35)
        lbl.bind("<Button-1>", self.exit)

        lbl = Label(self.root, text = "Twój wynik!", font=self.font3, bg = "white", bd = 2, relief = "solid")
        lbl.place(x = 250, y =538, width = 150, height = 40)   
        lbl = Label(self.root, text = self.number, font=self.font, bg = "white", bd = 2, relief = "solid")
        lbl.place(x = 250, y = 500, width = 150, height = 40)
        
        self.ploton = Canvas(self.root, bg = "gold", border = 0)
        self.ploton.place(x=450, y=10, width=340, height=580)

        self.password = self.randomText()

        self.createPassLetters()

        self.reckord()
        
        self.txt = ("Zacznij grać!\n"+"Auktualny rekord to: " + self.reckord + " punktów.\n"+"Sprubuj go pobić. :-)")

        messagebox.showinfo("Zaczynamy!", self.txt)


    def createPassLetters(self):
        category = ("Kategoria: " + self.category1)
        
        lbl = Label(self.root, text = category, font=self.font, bg="white", bd=2, relief="solid")
        lbl.place(x = 10, y =40, width = 280, height = 35)
        
        letterX = 10
        for letter in self.password:
            lbl = Label(self.root, text="", font=self.font, bg="white", bd=2, relief="solid")
            lbl.place(x=letterX, y=100, width=40, height=40)
            letterX += 45    
            self.passLabels.append(lbl)    

    def clear(self):
        self.errors = 0
        self.letters_ok = 0
        self.categoty = ""
        self.ploton.delete("all")
        for lbl in self.passLabels:
            lbl.destroy()
        self.passLabels = []
        self.password = self.randomText()
        self.createPassLetters()
        for letter in self.letters:
            letter["fg"] = "black"
            letter["bg"] = "white"            

    def checkLetter(self, event):
        if event.widget["fg"] != "black":
            return None

        litera_wybrana = event.widget["text"]
        czy_litera_ok = False
        for i, litera_hasla in enumerate(self.password):
            if litera_wybrana == litera_hasla:
                event.widget["fg"] = "white"
                event.widget["bg"] = "green"
                self.passLabels[i]["text"] = litera_wybrana
                czy_litera_ok = True
                self.rightLetter()
        if not czy_litera_ok:
            event.widget["fg"] = "red"
            event.widget["bg"] = "black"
            self.wrongLetter()

    def rightLetter(self):
        self.letters_ok += 1
        if self.letters_ok == len(self.password):
            over = ("¡WYGAŁEŚ!\n" +
                   "¿Chcesz grać dalej?")
            self.number += 15
            self.win += 1
            if messagebox.askyesno("GRATULACJE", over):
                lbl = Label(self.root, text = self.number, font=self.font, bg = "white", bd = 2, relief = "solid")
                lbl.place(x = 250, y = 500, width = 150, height = 40)
                self.clear()
            else:
                self.points()
                self.won()
                self.defeat()
                self.root.destroy()
                wisielec = WisielecExit()
                wisielec.run()
               

    def wrongLetter(self):
        self.errors += 1
        if self.errors == 1:
            self.ploton.create_line(20, 560 ,95 , 520, width = 10, fill = "#633A16")
        elif self.errors == 2:
            self.ploton.create_line(170, 560 ,95 , 520, width = 10, fill = "#633A16")
        elif self.errors == 3:
            self.ploton.create_line(95, 520 ,95 , 20, width = 10, fill = "#633A16")
        elif self.errors == 4:
            self.ploton.create_line(90, 20 ,305 , 20, width = 10, fill = "#633A16")
        elif self.errors == 5:
            self.ploton.create_line(245, 20 ,245 , 70, width = 5, fill = "#633A16")
        elif self.errors == 6:
            self.ploton.create_line(95, 150 ,170 , 20, width = 10, fill = "#633A16")
        elif self.errors == 7:
            self.ploton.create_oval(220, 70 ,270 , 120, width = 5)
        elif self.errors == 8:
            self.ploton.create_line(245, 120 ,245 , 230, width = 5, fill = "black")
        elif self.errors == 9:
            self.ploton.create_line(245, 150 ,205 , 190, width = 5, fill = "black")
        elif self.errors == 10:
            self.ploton.create_line(245, 150 ,285 , 190, width = 5, fill = "black")
        elif self.errors == 11:
            self.ploton.create_line(245, 230 ,205 , 270, width = 5, fill = "black")
        elif self.errors == 12:
            self.ploton.create_line(245, 230 ,285 , 270, width = 5, fill = "black")
        else:
            over = ("¡GRA SKOŃCZONA!\n" +
                   "Hasło to: " + self.password + "\n" +
                   "¿Chcesz grać dalej?")
            self.lost += 1
            self.number -= 10
            if messagebox.askyesno("GAME OVER", over):
                self.clear()
                lbl = Label(self.root, text = self.number, font=self.font, bg = "white", bd = 2, relief = "solid")
                lbl.place(x = 250, y = 500, width = 150, height = 40)
            else:
                self.won()
                self.defeat()
                self.points()
                self.root.destroy()
                wisielec = WisielecExit()
                wisielec.run()
        
    def randomCategory(self):
        randomCategory = random.randint(1, 4)
        self.category = linecache.getline('pliki/password/category.txt', randomCategory)
        self.category = self.category.rstrip()
        self.category1 = self.category
        self.category = ("pliki/password/" + self.category + ".txt")

    def randomText(self):
        self.randomCategory()
        category = self.category
        randomLiczba = random.randint(1, 20)
        wiersz = linecache.getline(category, randomLiczba)
        wiersz = wiersz.rstrip()
        #print(wiersz)
        return wiersz.upper()
    def run(self):
        self.root.mainloop()

    def reckord(self):
        plik = open('pliki\pliki\plik', 'r')
        try:
            self.liczba = plik.read()
            self.reckord = self.liczba
        finally:
             plik.close()

    def nowpoints(self):
        points = str(self.number)
        #print(points)
        plik = open('pliki\pliki\score', 'w')
        plik.write(points)
        plik.close()

    def won(self):
        win = str(self.win)
        plik = open('pliki\pliki\win', 'w')
        plik.write(win)
        plik.close()

    def defeat(self):
        lost = str(self.lost)
        plik = open('pliki\pliki\lost', 'w')
        plik.write(lost)
        plik.close()
    
    def points(self):
        self.nowpoints()
        self.liczba = int(self.liczba)
        self.number = int(self.number)
        if (self.number > self.liczba):
            self.licznik = self.liczba
            self.number = str(self.number)
            plik = open('pliki\pliki\plik', 'w')
            plik.write(self.number)
            plik.close()

    def exit(self,event):
        if messagebox.askyesno("Czy na pewno?","Czy na pewno chcesz wyjść z gry?"):
                self.points()
                self.won()
                self.defeat()
                self.root.destroy()
                wisielec = WisielecExit()
                wisielec.run()
                

if __name__ == '__main__':
    wisielec = Wisielec()
    wisielec.run()


