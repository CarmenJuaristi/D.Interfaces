import threading
import requests
import tkinter as tk
from window import MainWindow
from tkinter import messagebox

class loadingWindow:
    
    def __init__(self, root):
        self.root = root
        self.root.title("CARGANDO...") # Aqui le damos el titulo a la ventana de carga
        self.root.geometry("170x120") # Aqui le damos el tamaño a la ventana de carga
        self.root.resizable(False, False) # Aqui indicamos que no se puede estirar ni ampliar la ventana de carga
        
        self.label = tk.Label(self.root, text="Cargando datos...", font=("arial", 14)) # Aqui mostramos un texto dentro de la ventana
        self.label.pack(side=tk.TOP, pady=10)
# De aqui para aabajo hacemos el circulo de carga
        label_bg_color = self.label.cget("bg")

        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0 
        
        self.draw_progress_circle(self.progress)
        
        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        
    def draw_progress_circle(self, progress): # Aqui mostramos el circulo de carga
        self.canvas.delete("progress")
        angle = int(360 * (progress/100))

        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=5, style=tk.ARC)
    
    def update_progress_circle(self): # Aqui hacemos que el circulo de carga gire
        if self.progress < 100:
            self.progress+=10
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(200, self.update_progress_circle)
    
    def launch_main_window(json_data, root): # Aqui lanzamos la ventana main
        root = tk.Tk()
        app = MainWindow(root, json_data) #Aqui lanzamos la ventana principal
        root.mainloop()

    def fetch_json_data(self, json_data): # Aqui descargamos el json
        response = requests.get("https://github.com/CarmenJuaristi/D.Interfaces/blob/main/catalog.json")
        if response.status_code == 200:
            json_data = response.json()
            self.root.quit()
            self.launch_main_window(json_data)   

    