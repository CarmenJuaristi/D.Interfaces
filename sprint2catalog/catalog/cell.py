import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, image_url, description):
        self.title = title
        self.image_url = image_url
        response = requests.get(self.image_url)
        imagen_rediseñada = Image.open(BytesIO(response.content))
        self.description = description
        imagen_rediseñada = (Image.open(self.path)).resize((100,100), Image.Resampling.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(imagen_rediseñada)
       


