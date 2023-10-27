from tkinter import Tk
from loadingWindow import loadingWindow
if __name__ == "__main__":
    loadingWindow
    root = Tk()
    app = loadingWindow(root)
    root.mainloop()
