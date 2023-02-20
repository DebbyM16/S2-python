import tkinter as tk

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // 9
hauteur_case = HEIGHT // 9
largeur_cube = WIDTH // 3
hauteur_cube = HEIGHT // 3

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
canvas.grid(padx=10)

for i in range(9):
    for j in range(9):
        x1 = i
        y1 = j
        canvas.create_rectangle((x1*largeur_case, y1*hauteur_case),
                ((x1+1)*largeur_case, (y1+1)*hauteur_case), fill="grey80")
racine.mainloop() # Lancement de la boucle principale