import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path, description):
        self.title = title
        self.path = path
        self.description = description
        imagen_rediseñada = (Image.open(self.path)).resize((100,100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(imagen_rediseñada)
