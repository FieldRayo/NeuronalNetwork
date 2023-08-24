import sqlite3
from tkinter import messagebox


class Connection:
    def __init__(self):
        self.database_nn = '/home/fieldrayo/Proyects/Github/NeuronalNetwork/NeuronalNetwork-Multilayer/Interface/database/neuralnets.db'
        self.connection = sqlite3.connect(self.database_nn)
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.connection.commit()
        self.connection.close()


class NeuronalNet:
    def __init__(self, name, n_inputs, n_hidden, n_outputs):
        self.id_neuronalnet = None
        self.name = name
        self.n_inputs = n_inputs
        self.n_hidden = n_hidden
        self.n_outputs = n_outputs
    
    def __str__(self):
        return f'Neuronal Network[{self.name}, {self.n_inputs}, {self.n_hidden}, {self.n_outputs}]'
    
def save(neuronalnet):
    connection = Connection()
        
    sql = f'''INSERT INTO neuronal_net (name, n_inputs, n_hidden, n_outputs)
    VALUES('{neuronalnet.name}', '{neuronalnet.n_inputs}', '{neuronalnet.n_hidden}', '{neuronalnet.n_outputs}')
    '''
    
    try:
        connection.cursor.execute(sql)
        connection.close()
    except:
        title = 'Register Connection'
        message = 'Table does not exist'
        messagebox.showwarning(title, message)
    

def insert():
    connection = Connection()
    list_nets = []
    
    sql = 'SELECT * FROM neuronal_net'
    
    try:
        connection.cursor.execute(sql)
        list_nets = connection.cursor.fetchall()
        connection.close()
    except:
        title = 'Register Connection'
        message = 'First you need to create a table'
        messagebox.showwarning(title, message)
        
    return list_nets

def create_table():
    connection = Connection()
    
    sql = '''
    CREATE TABLE neuronal_net(
        id_neuronalnet INTEGER,
        name VARCHAR(50),
        n_inputs VARCHAR(50),
        n_hidden VARCHAR(50),
        n_outputs VARCHAR(50),
        PRIMARY KEY(id_neuronalnet AUTOINCREMENT)
    )'''
    
    try:
        connection.cursor.execute(sql)
        connection.close()
        title = 'Register create'
        message = 'The table has been created successfully'
        
        messagebox.showinfo(title, message)
    except:
        title = 'Register create'
        message = 'The table already exists'
        
        messagebox.showwarning(title, message)

def delete_table():
    connection = Connection()
    
    sql = 'DROP TABLE neuronal_net'
    
    try:
        connection.cursor.execute(sql)
        connection.close()
        title = 'Register delete'
        message = 'The table has been successfully deleted'
        
        messagebox.showinfo(title, message)
    except:
        title = 'Register delete'
        message = 'table does not exist'
        
        messagebox.showwarning(title, message)