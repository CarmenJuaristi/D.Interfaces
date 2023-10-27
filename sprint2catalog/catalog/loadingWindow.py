import threading
import requests
import tkinter as tk
from window import MainWindow
from tkinter import messagebox

class loadingWindow:
    
    def __init__(self, root):
        self.finished = False
        self.json_data = []
        self.root = root
         # Esto es el título de la ventana de carga
        self.root.title("CARGANDO...")
        # Aquí indicamos el ancho y alto de dicha ventana 
        self.root.geometry("170x120") 
        # Aquí lo que indicamos es que no se pueda aumentar el tamaño de la ventana ni en horizontal ni en vertical
        self.root.resizable(False, False) 
        # Esto es el texto que hay dentro de la ventana
        self.label = tk.Label(self.root, text="Cargando datos...", font=("arial", 14)) 
        self.label.pack(side=tk.TOP, pady=10)
        # A partir de aquí creamos el círculo de carga
        label_bg_color = self.label.cget("bg") #Esto es para obtener el color de fondo 
        
        #Aquí dibujamos la circunferencia
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        self.progress = 0 
        
        self.draw_progress_circle(self.progress)
        
        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        if self.thread.is_alive():
            self.check_thread()
    # Aquí lo mostramos 
    def draw_progress_circle(self, progress): 
        self.canvas.delete("progress")
        angle = int(360 * (progress/100))
        self.canvas.create_arc(10, 10, 35, 35, start = 0, extent=angle, tags="progress", outline='green', width=5, style=tk.ARC)
    
    # Aquí hacemos que gire el círculo de carga 
    def update_progress_circle(self): 
        if self.progress < 100:
            self.progress+=10
        else:
            self.progress=0
        
        self.draw_progress_circle(self.progress)
        self.root.after(200, self.update_progress_circle)
    
    #Aquí será donde en el siguiente ejercicio descarguemos el json
    def fetch_json_data(self): 
        response = requests.get("https://raw.githubusercontent.com/CarmenJuaristi/D.Interfaces/main/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished=True
    
    # Aquí comprobamos que la descarga esté bien
    def check_thread(self): 
        if self.finished:
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

# Aquí lanzamos el main
def launch_main_window(json_data, root):
    root = tk.Tk()
    # Y aquí lanzamos la principal
    root.app = MainWindow(root, json_data) 
    root.mainloop()
    # Aquí vamos a centrar la imagen
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}") 