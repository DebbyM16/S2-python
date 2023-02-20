import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code
x0 = 300
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
canvas.create_line(x0, y + 150, x0, y - 150)
canvas.create_oval(x0 - 50, CANVAS_HEIGHT, x0 + 50, y + 100)
canvas.create_oval(x0 - 50, 0, x0 + 50, y - 100)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
    
# Fin de votre code
canvas.grid()
root.mainloop()