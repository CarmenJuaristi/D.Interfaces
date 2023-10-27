from tkinter import Tk
from loadingWindow import loadingWindow
if __name__ == "__main__":
    loadingWindow
    root = Tk()
    # Aquí vamos a centrar la imagen
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) /2 
    y = (root.winfo_screenheight() - root.winfo_reqheight()) /2
    root.geometry(f"+{int(x)}+{int(y)}") 
    app = loadingWindow(root)
    
    root.mainloop()
