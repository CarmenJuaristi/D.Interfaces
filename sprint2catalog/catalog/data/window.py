from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow
class MainWindow:
    # Primero haremos que cuando clickee una de las fotos le salte el mensaje de hiciste click en la celda de y el título de la celda que en este caso será el titulo del 
    # videojuego en el que hagas click
    def on_button_clicked(self,cell):
        DetailWindow(self.root, cell.title, cell.image_tk, cell.description)
    def __init__(self, root):
        root.title("Videojuegos")
        self.root = root
        self.cells = [
            # A cada celda le asignamos un título (que será el que se muestre cuando clickees en la celda, y una ruta de acceso para poner la foto)
            Cell("The Last Of Us 1 remake","C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\TLOU 1.jpg","En un mundo postapocalíptico en el que los infectados, antiguos humanos extremadamente agresivos y convertidos en criaturas salvajes por un hongo mutante, vagan por el mundo, el curtido superviviente Joel deberá guiar a Ellie, una adolescente, fuera de la zona de cuarentena militar. La misión se convierte en un angustioso viaje a través de unos Estados Unidos devastados, mientras Joel hace todo lo que puede para mantenerla con vida. "),
            Cell("The Last Of Us 2","C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\TLOU2.jpg","Cinco años después de su peligroso viaje a través de unos Estados Unidos pospandemia, Ellie y Joel logran establecerse en Jackson, Wyoming. Vivir entre una próspera comunidad de sobrevivientes les ha concedido paz y estabilidad, a pesar de la amenaza constante de los infectados y de otros sobrevivientes más desesperados. Cuando un evento traumático interrumpe esa paz, Ellie se embarca en un viaje incesante para obtener justicia y llegar a un cierre. A medida que caza a los responsables uno por uno, deberá enfrentarse a las devastadoras repercusiones físicas y emocionales de sus acciones."),
            Cell("Resident Evil 4 remake", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\RE 4.jpg","Seis años después de los eventos de Resident Evil 2, el sobreviviente de Raccoon City, Leon Kennedy, se encuentra apostado en un recóndito pueblo de Europa para investigar la desaparición de la hija del presidente de los Estados Unidos. Lo que descubre allí no se parece a nada que haya enfrentado antes."),
            Cell ("Uncharted 4", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\Uncharted4.jpg","res años después de los eventos de  UNCHARTED 3: La traición de Drake, se supone que Nathan Drake se retiró del mundo de los cazafortunas. Sin embargo, el destino no tarda en golpear su puerta cuando su hermano Sam reaparece en busca de ayuda para salvar su propia vida, una aventura demasiado tentadora e irresistible para Drake.  "),
            Cell ("Call of Dutty Black Ops 2", "C:\\msys64\\home\\carme\\D.Interfaces\\sprint1Tkinter\\catalog\\data\\edited\\CD BO 2.jpg","El argumento inicia en los años 80 durante la Guerra Fría, esto con el fin de centrarse en el origen de la historia del principal antagonista de Black Ops II, Raúl Menéndez; que, en 2025, es él quien provoca la guerra entre China y EE. UU. En la línea temporal de 1980, el protagonista es Alex Mason, quien también lo era en Black Ops. Frank Woods, otro de los personajes de Black Ops, vuelve a este argumento y es además el narrador de la línea temporal de 1980. En la sección de este año el protagonista será David Mason")
        ]
        # Aquí lo que hacemos es enumerar las celdas, es decir que estén ordenadas en vertical
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title,compound=tk.BOTTOM)
            label.grid(row=i,column=0)
            # En esta línea con el label bind estamos pendientes de si el usuarios clickea sobre una celda con el botón izquierdo del ratón
            #  y con el cell = cell ... lo que hacemos es que ejecute la función on_button_clicked pasando como parámetro la celda actual
            # y por eso si pulsas la celda de The Las Of Us 1 remake no te va a aparecer el titulo de Uncharted 4.
            #
            label.bind("<Button-1>",lambda event, cell = cell: self.on_button_clicked(cell))