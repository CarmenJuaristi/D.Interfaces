from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
class MainWindow:
    # Primero haremos que cuando clickee una de las fotos le salte el mensaje de hiciste click en la celda de y el título de la celda que en este caso será el titulo del 
    # videojuego en el que hagas click
    def on_button_clicked(self,cell):
        message = "Hiciste click en la celda "+cell.title
        messagebox.showinfo("Información", message)
    def __init__(self, root):
        root.title("MainWindow")
        self.cells = [
            # A cada celda le asignamos un título (que será el que se muestre cuando clickees en la celda, y una ruta de acceso para poner la foto)
            Cell("The Last Of Us 1 remake","C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\TLOU 1.jpg"),
            Cell("The Last Of Us 2","C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\TLOU2.jpg"),
            Cell("Resident Evil 4 remake", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\RE 4.jpg"),
            Cell ("Uncharted 4", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\Uncharted4.jpg"),
            Cell ("Call of Dutty Black Ops 2", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\CD BO 2.jpg")
        ]
        # Aquí lo que hacemos es enumerar las celdas, es decir que estén ordenadas en vertical
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title,compound=tk.BOTTOM)
            label.grid(row=i,column=0)
            # En esta línea con el label bind estamos pendientes de si el usuarios clickea sobre una celda con el botón izquierdo del ratón
            #  y con el cell = cell ... lo que hacemos es que ejecute la función on_button_clicked pasando como parámetro la celda actual
            # y por eso si pulsas la celda de The Las Of Us 1 remake no te va a aparecer el titulo de Uncharted 4.
            label.bind("<Button-1>",lambda event, cell = cell: self.on_button_clicked(cell))