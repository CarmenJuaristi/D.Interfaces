import tkinter as tk 
from tkinter import ttk
from cell import Cell

def mostrarDetalles(cell):
    root = tk.Toplevel()
    root.title(cell.nombre)
    mostrarl = ttk.Label(root, image = cell.image_tk)
    mostrarl.pack()
    mostrarl2 = ttk.Label(root, text = cell.descripcion)
    mostrarl2.pack()
    #Aquí vamos a centrar la imagen
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}")
    # Aquí lannzaremos la ventana detallada
    root.mainloop() 
    
