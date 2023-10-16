import tkinter as tk 
from tkinter import ttk
class DetailWindow:
    def __init__ (self,root,title,image,description):
        self.root = root
        self.title = title
        self.image = image
        self.description = description
        self.window = tk.Toplevel(root)
        self.window.title(self.title)
    # Para la nueva pestaña que abriremos poniendo la foto, título y descripción primero ponemos al imagen, después el tipo de letra que querremos en el titulo y la descripcion
        image_label = ttk.Label(self.window, image = self.image)
        image_label.pack()
        title_label = ttk.Label(self.window, text = self.title, font = ("Times New Roman",16))
        title_label.pack()
        description_label = ttk.Label(self.window, text = self.description, wraplength= 300)
        description_label.pack()