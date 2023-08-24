import tkinter as tk
from tkinter import ttk

from .connection import *


def menu(root):
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar, width=300, height=300)
    
    menu_init = tk.Menu(menu_bar, tearoff=0)
    menu_check = tk.Menu(menu_bar, tearoff=0)
    menu_conf = tk.Menu(menu_bar, tearoff=0)
    menu_help = tk.Menu(menu_bar, tearoff=0)
    
    # Start Menu
    menu_bar.add_cascade(label='Start', menu=menu_init)
    
    menu_init.add_command(label='Create Table', command=create_table)
    menu_init.add_command(label='Delete Table', command=delete_table)
    menu_init.add_command(label='Exit', command=root.destroy)
    
    # Check Menu
    menu_bar.add_cascade(label='Check', menu=menu_check)
    
    # Config Menu
    menu_bar.add_cascade(label='Config', menu=menu_conf)
    
    # Help Menu
    menu_bar.add_cascade(label='Help', menu=menu_help)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=480, height=320, bg='#262626')
        
        self.nets_fields()
        self.disable_fields()
        self.table_nets()
    
    def nets_fields(self):
        # Name Label
        self.label_name = tk.Label(self, text='Name: ',
                                   fg='#d6d6d6', bg='#262626')
        self.label_name.config(font=('Arial', 12, 'bold'))
        self.label_name.grid(row=0, column=0, padx=10, pady=10, )
        
        # Input Label
        self.label_input = tk.Label(self, text='Number of Inputs: ',
                                    fg='#d6d6d6', bg='#262626')
        self.label_input.config(font=('Arial', 12, 'bold'))
        self.label_input.grid(row=1, column=0, padx=10, pady=10)
        
        # Hidden Label
        self.label_hidden = tk.Label(self, text='Number of Hidden: ',
                                     fg='#d6d6d6', bg='#262626')
        self.label_hidden.config(font=('Arial', 12, 'bold'))
        self.label_hidden.grid(row=2, column=0, padx=10, pady=10)
        
        # Output Label
        self.label_output = tk.Label(self, text='Number of outputs: ',
                                     fg='#d6d6d6', bg='#262626')
        self.label_output.config(font=('Arial', 12, 'bold'))
        self.label_output.grid(row=3, column=0, padx=10, pady=10)
        
        # Name Entry
        self.get_name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable=self.get_name)
        self.entry_name.config(width=25, font=('Arial', 12))
        self.entry_name.grid(row=0, column=1, columnspan=2)
        
        # Inputs Entry
        self.get_inputs = tk.StringVar()
        self.entry_inputs = tk.Entry(self, textvariable=self.get_inputs)
        self.entry_inputs.config(width=25, font=('Arial', 12))
        self.entry_inputs.grid(row=1, column=1, columnspan=2)
        
        # Hidden Entry
        self.get_hidden = tk.StringVar()
        self.entry_hidden = tk.Entry(self, textvariable=self.get_hidden)
        self.entry_hidden.config(width=25, font=('Arial', 12))
        self.entry_hidden.grid(row=2, column=1, columnspan=2)
        
        # Output Entry
        self.get_output = tk.StringVar()
        self.entry_output = tk.Entry(self, textvariable=self.get_output)
        self.entry_output.config(width=25, font=('Arial', 12))
        self.entry_output.grid(row=3, column=1, columnspan=2)
        
        # Button Create
        self.button_create = tk.Button(self, text="Create", command=self.start_fields)
        self.button_create.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='green', bg='#262626', cursor='hand2',
                                  activebackground='#202020')
        self.button_create.grid(row=4, column=0)
        
        # Button Save
        self.button_save = tk.Button(self, text="Save", command=self.save_data)
        self.button_save.config(width=20, font=('Arial', 12, 'bold'),
                                fg='blue', bg='#262626', cursor='hand2',
                                activebackground='#202020')
        self.button_save.grid(row=4, column=1)
        
        # Button Cancel
        self.button_cancel = tk.Button(self, text="Cancel", command=self.disable_fields)
        self.button_cancel.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='red', bg='#262626', cursor='hand2',
                                  activebackground='#202020')
        self.button_cancel.grid(row=4, column=2)
        
        # Button Edit
        self.button_edit = tk.Button(self, text="Edit")
        self.button_edit.config(width=20, font=('Arial', 12, 'bold'),
                                fg='blue', bg='#262626', cursor='hand2',
                                activebackground='#202020')
        self.button_edit.grid(row=6, column=0)
        
        # Button Delete
        self.button_delete = tk.Button(self, text="Delete")
        self.button_delete.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='red', bg='#262626', cursor='hand2',
                                  activebackground='#202020')
        self.button_delete.grid(row=6, column=1)
    
    def start_fields(self):
        # Entry
        self.entry_name.config(state='normal')
        self.entry_inputs.config(state='normal')
        self.entry_hidden.config(state='normal')
        self.entry_output.config(state='normal')
        
        # Buttons
        self.button_save.config(state='normal')
        self.button_cancel.config(state='normal')
    
    def disable_fields(self):
        self.get_name.set('')
        self.get_inputs.set('')
        self.get_hidden.set('')
        self.get_output.set('')
        
        # Entry
        self.entry_name.config(state='disabled')
        self.entry_inputs.config(state='disabled')
        self.entry_hidden.config(state='disabled')
        self.entry_output.config(state='disabled')
        
        # Buttons
        self.button_save.config(state='disabled')
        self.button_cancel.config(state='disabled')
    
    def save_data(self):
        neuronal_net = NeuronalNet(
            self.get_name.get(),
            self.get_inputs.get(),
            self.get_hidden.get(),
            self.get_output.get()
        )
        
        save(neuronal_net)
        
        self.table_nets()
        
        self.disable_fields()
    
    def table_nets(self):
        self.list_nets = insert()
        self.list_nets.reverse()
        
        self.table = ttk.Treeview(self, columns=('Name', 'Numbers of Input',
                                                 'Numbers of Hidden', 'Numbers of Output'))
        self.table.grid(row=5, column=0, columnspan=5)
        
        self.table.heading('#0', text='ID')
        self.table.heading('#1', text='Name')
        self.table.heading('#2', text='Numbers of Input')
        self.table.heading('#3', text='Numbers of Hidden')
        self.table.heading('#4', text='Numbers of Output')
        
        for nt in self.list_nets:
            self.table.insert('', 0, text=nt[0], values=(nt[1], nt[2], nt[3], nt[4]))
        
        self.table.insert('', 0, text='1', values=('Neuronal Network 1',
                                                   '2', '4, 6, 4', '2'))
