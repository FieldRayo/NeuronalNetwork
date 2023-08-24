import tkinter as tk
from client.gui_app1 import Frame, menu


def main():
    root = tk.Tk()
    root.title('Neuronal Network Create')
    root.config(bg='#262626')
    menu(root)

    app = Frame(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()
    