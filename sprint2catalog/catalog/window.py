from tkinter import ttk
import threading
import requests 
from PIL import Image, ImageTk 
import tkinter as tk
from cell import Cell
from tkinter import messagebox, Canvas, Frame, Label, Tk, ttk
from detail_window import mostrarDetalles
class MainWindow:
    cells = []
    # Primero haremos que cuando clickee una de las fotos le salte el mensaje de hiciste click en la celda de y el título de la celda que en este caso será el titulo del 
    # videojuego en el que hagas click
    def on_button_clicked(self,cell):
        mostrarDetalles(self.root, cell.title, cell.image_url, cell.description)
    def __init__(self, root, json_data):
        self.root = root
        self.cells = []
        for i in json_data:
            title = i.get("title")
            description = i.get("description")
            image_url = i.get("image_url")
            cell = Cell(title,description,image_url)
            self.cells.append(cell)
        #Crearemos aquí el scrollbar, que será verical y tambien el tamaño que queremos 
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview, width=15)
        # Crearemos el Frame del scrollbar
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        # Aqui lo configuraremos
        self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        for i, cell in enumerate(self.cells):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(pady=10)
            label = tk.Label(frame, image=cell.image_tk, text=cell.nombre, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, celda= cell:mostrarDetalles(celda))
        # Y por último lo posicionamos en la ventana
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1) 
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
            label.bind("<Button-1>",lambda event, cell = cell: self.mostrarDetalles(cell))
        
