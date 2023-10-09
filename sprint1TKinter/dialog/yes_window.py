import tkinter as tk
#Aquí definimos show_yes_window, donde si pulsamos la casilla de si, pondrá a mí me apetece un cigarro
def show_yes_window(self, yes_root):
    self.yes_root = yes_root
    yes_root.title("Casilla de sí")
    self.frame=tk.Frame(self.yes_root)
    self.frame.pack()

    self.label=tk.Label(self.frame, text="A mí me apetece un cigarro")
    self.label.pack()
    


   
  