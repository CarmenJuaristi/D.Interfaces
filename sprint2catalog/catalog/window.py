from tkinter import ttk
import threading
import requests 
from PIL import Image, ImageTk 
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow
class MainWindow:
    cells = []
    # Primero haremos que cuando clickee una de las fotos le salte el mensaje de hiciste click en la celda de y el título de la celda que en este caso será el titulo del 
    # videojuego en el que hagas click
    def on_button_clicked(self,cell):
        DetailWindow(self.root, cell.title, cell.image_url, cell.description)
    def __init__(self, root, json_data):
        self.root = root
        self.cells = []
        for i in json_data:
            title = i.get("title")
            description = i.get("description")
            image_url = i.get("image_url")
            cell = Cell(title,description,image_url)
            self.cells.append(cell)
        # Aquí lo que hacemos es enumerar las celdas, es decir que estén ordenadas en vertical
        for i in range in enumerate(self.cells):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(pady=10)
            label = tk.Label(frame, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i,column=0)
            # En esta línea con el label bind estamos pendientes de si el usuarios clickea sobre una celda con el botón izquierdo del ratón
            #  y con el cell = cell ... lo que hacemos es que ejecute la función on_button_clicked pasando como parámetro la celda actual
            # y por eso si pulsas la celda de The Las Of Us 1 remake no te va a aparecer el titulo de Uncharted 4.
            #
            label.bind("<Button-1>",lambda event, cell = cell: self.on_button_clicked(cell))
        
