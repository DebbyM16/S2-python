import tkinter as tk 
import random

# Fond noir

Height = Width = 500
marge = 500 // 4

# Commandes des boutons

def circle():
    x = random.randint(50, 400)
    y = random.randint(50, 400)
    fond.create_oval(x - 50, y - 50, x + 50, y + 50, outline= "blue2")

def square():
    x0 = random.randint(50, 400)
    y0 = random.randint(50, 400)
    fond.create_rectangle(x0 - 50, y0 - 50, x0 + 50, y0 + 50, outline= "red2")

def cross():
    x1 = random.randint(50, 400)
    y1 = random.randint(50, 400)
    fond.create_line(x1, y1, x1 + 100, y1, fill= "yellow")
    fond.create_line(x1 + 50, y1 - 50, x1 + 50, y1 + 50, fill= "yellow")

# Création de la fenêtre

fenetre = tk.Tk()
fenetre.title("Mon dessin")

couleur = tk.Button(fenetre, text= "Choisir une couleur")
couleur.grid(row= 0, column= 1)

cercle = tk.Button(fenetre, text= "Cercle", command= circle)
cercle.grid(row = 1, column= 0)

carre = tk.Button(fenetre, text= "Carré", command= square)
carre.grid(row= 2, column= 0)

croix = tk.Button(fenetre, text= "Croix", command= cross)
croix.grid(row= 3, column= 0)

fond = tk.Canvas(fenetre, height= Height, width= Width, bg= "grey1", bd= 5,
                relief= "raised")
fond.grid(row= 1, column= 1, rowspan= 3)

fenetre.mainloop()