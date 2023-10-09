import tkinter as tk
#definimos show_no_window y lo que haremos será que si pulsa No, después ponga respuesta errónea
def show_no_window(self,no_root):
    self.no_root = no_root
    no_root.title("No me apetece un cigarro")
    self.frame=tk.Frame(self.no_root)
    self.frame.pack()

    self.label=tk.Label(self.frame, text="Respuesta errónea")
    self.label.pack()
    
