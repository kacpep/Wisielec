from tkinter import *
from tkinter import messagebox
import tkinter as tk
from wisielec import *


class WisielecStart(object):
    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Wisielec")
        self.root.geometry("800x600")
        self.font = ("Ariel" ,20,"bold")
        self.fontStart = ("Ariel" ,35,"bold")

        self.root.iconbitmap("pliki/img/panther.ico")

        C = Canvas(self.root, height=800, width=600)
        background = PhotoImage( file = "pliki/img/tlo.png")
        background_label = Label(self.root, image=background)
        background_label.image = background
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        B = Canvas(self.root, height=312, width=562)
        background = PhotoImage( file = "pliki/img/foto.png")
        background_label = Label(self.root, image=background)
        background_label.image = background
        background_label.place(x = 470, y = 15)
        
        
        lbl = Label(self.root, text = "START!",font = self.fontStart, fg = "white", bg = "red", bd = 2, relief = "solid", border = 0)
        lbl.place(x = 114, y = 200, width = 250, height = 80)
        lbl.bind("<Button-1>", self.exitStart)

        sb_textbox = tk.Scrollbar(self.root)

        textbox = tk.Text(self.root, width = 53, height = 10, yscrollcommand = sb_textbox.set)
        textbox.pack()
        sb_textbox.place(in_ = textbox, relx = 1., rely = 0, relheight = 1.) 
        textbox.place(x=10, y=415)
        textbox.insert(tk.END, "       Zasady gry", ("h1")) 
        textbox.insert(tk.END, """\n \n - Zgadujesz hasło i dostajesz 15 punktów.
        \n - Kategoria wyświetla się nad słowem.
        \n - Są to pojedyncze słowa.
        \n - Kategorie sąbardzo ogólne.
        \n - Aby odgadnąć słowo należy klikać w litery.
        \n - Słowa są losowane automatycznie.
        \n - Można popełnić tylko 13 błędów.
        \n - Jeden błąd to jedna litera której nie ma w słowie.
        \n - Jeden błąd to -10 punktów.
        \n - Nie otwieraj pliku z hasłami.
        \n - Aby zapisać grę musisz kliknąć przycisk "wyjdź"
        \n   lub kiedy program zapyta "Czy chcesz dalej grać?".
        \n   kliknij "Nie".
        \n - Program automatycznie zapisze twój wynik.
        \n - Aby zacząć grać kliknij "START!"
        \n - Życzę dobrej zabawy.  :-)
        \n - Gra autorstwa Kacper Ostrowski
        \n - Wszelkie prawa zastrzeżone (c)
        \n """) 
        textbox.tag_config("h1", font = self.fontStart)
        textbox.tag_config("p", foreground="#fff")

        sb_textbox.config(command = textbox.yview)

    def exitStart(self,event):
        self.root.destroy()
        wisielec = Wisielec()
        wisielec.run()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    wisielecStart = WisielecStart()
    wisielecStart.run()
