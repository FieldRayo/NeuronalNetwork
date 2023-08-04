import matplotlib.pyplot as plt
import ast

import sys
import os

# Agregar el directorio que contiene Multilayer.py al sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from Multilayer import NeuronalNetwork
import cmd_help
import Datatrain

data = {}


def get_args(command, parameters):
    words = command.split(" --")[1::]
    args = {}
    
    for x in words:
        p = x.split(" ", 1)

        if p[0] in parameters:
            args[p[0]] = ast.literal_eval(p[-1])
        else:
            print(f"The parameter '{p[0]}' is not in the parameter list. "
                  f"For more information consult 'help'.")
        
    return args


def read_file(command):
    args = get_args(command, ["file"])
    
    file_name = args["file"]
    
    file = (open(f"/home/fieldrayo/Proyects/"
                 f"Github/NeuronalNetwork/NeuronalNetwork-Multilayer/"
                 f"Interface/Commands_files/{file_name}.txt", "r")).read()
    
    print(file)
    file = file.split(" - ")
    
    for cmd in file:
        cmd_name = cmd.split()[0]
        
        if cmd_name in commands_mapping:
            commands_mapping[cmd_name](cmd)
        else:
            print(cmd_name)
        
    return ""


def create_file(command):
    args = get_args(command, ["file"])
    
    file_name = args["file"]
    
    import os
    file = open(f"/home/fieldrayo/Proyects/"
                f"Github/NeuronalNetwork/NeuronalNetwork-Multilayer/"
                f"Interface/Commands_files/{file_name}.txt", "w")
        
    text = input(f"- Archivo {file_name}.txt -\nWrite here: ")
    file.write(text + os.linesep)
    file.close()
    
    return ""
    

def create_net(command):
    parameters = ["name", "n_inputs", "n_hidden", "n_outputs"]
    default_values = ["NN1", 2, [4, 6, 4], 1]
    args = get_args(command, parameters)

    name = args.get("name", default_values[0])
    n_inputs = args.get("n_inputs", default_values[1])
    n_hidden = args.get("n_hidden", default_values[2])
    n_outputs = args.get("n_outputs", default_values[3])
    
    if name in data:
        return f"The name '{name}' has already been used to create a neural network"

    data[name] = {}
    data[name]["ID"] = cm_nn(n_inputs, n_hidden, n_outputs)
    
    return f"{name}: {data[name]}\n- Has been created -"


def forward(command):
    parameters = ["name", "input"]
    args = get_args(command, parameters)
    
    name = args["name"]
    input_ = args["input"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    return f"The current prediction is: {cm_nn_forward(data[name]['ID'], input_)[0]}"


def backpropagation(command):
    args = get_args(command, ["name"])
    
    name = args["name"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    data[name]["backpropagation"] = cm_nn_back(name)
    
    return f"- {name}: The backpropagation has been applied -"


def gradientdescent(command):
    parameters = ["name", "lr"]
    args = get_args(command, parameters)
 
    name = args["v1"]
    lr = args["v2"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    data[name]["gradientdescent"] = cm_nn_grad(data[name]["ID"], lr)
    return f"- {name}: The gradient decent has been applied -"


def get_value(command):
    parameters = ["name", "value", "index"]
    args = get_args(command, parameters)
    
    name = args["name"]
    value = args["value"]
    index = args.get("index", "*")
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    if not hasattr(data[name]["ID"], value):
        return "The neural network is missing from the data"
    
    s_data = getattr(data[name]['ID'], value)
    
    if len(index) != 1:
        n_data = index.split("-")
        n_data = list(map(int, n_data))
        return s_data[n_data[0] - 1:n_data[1] - 1]
    elif index == "*":
        return s_data
    else:
        n_data = list(map(int, index))[0]
        return s_data[n_data - 1]


def set_value(command):
    args = get_args(command, ["name", "value", "new_value"])
    if args == 0:
        return ""
    
    name = args["name"]
    value = args["value"]
    new_value = args["new_value"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    if not hasattr(data[name]["ID"], f"{value}"):
        return "The neural network is missing from the data"
    
    setattr(data[name]["ID"], value, new_value)
    update(data[name]["ID"])
    
    return f"{value} = {new_value}"


def show_nn(command):
    if len(data) == 0:
        return "First create a neural network with 'create_net (ID)'"
    
    if len(command.split()) != 1:
        return "the command takes no parameters"
    
    return "\n".join(cm_show_nn())


def show_data(command):
    args = get_args(command, ["name", "value", "index"])
    if args == 0:
        return ""
    
    name = args["name"]
    value = args["value"]
    index = args.get("index", "*")
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    s_data = data[name][value]
    
    if len(index) != 1:
        n_data = index.split("-")
        n_data = list(map(int, n_data))
        return s_data[n_data[0] - 1:n_data[1] - 1]
    elif index == "*":
        return s_data
    elif True:
        n_data = list(map(int, index))[0]
        return s_data[n_data - 1]


def len_data(command):
    args = get_args(command, ["name", "value"])
    
    name = args["name"]
    value = args["value"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    if isinstance(data[name], list):
        return f"len {value} = {len(data[name][value])}"
    
    return f"len {value} = 1"


def train_net(command):
    args = get_args(command, ["name", "lr", "err_max"])
    
    name = args["name"]
    lr = args["lr"]
    err_max = args["err_max"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    x, y = data[name]["datatrain"]
    
    data[name]["train"] = cm_nn_train(data[name]["ID"], lr, err_max, x, y)
    return f"\n- {name}: The train has been applied -"


def show_graphic(command):
    args = get_args(command, ["name", "graphic", "type"])
    
    name = args["name"]
    type_graphic = args["graphic"]
    plt_type = args["type"]
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    x, y = data[name][type_graphic]
    
    plt.clf()
    if plt_type == "plot":
        plt.plot(x, y)
    elif plt_type == "scatter":
        plt.scatter(x[:, 0], x[:, 1], c=y)
    
    plt.show()
    return ""


def set_datatrain(command):
    args = get_args(command, ["name", "datatrain", "size", "file_train"])
    if args == 0:
        return ""
    
    name = args["name"]
    data_s = args["datatrain"]
    size = args.get("size", 100)
    file_train = args.get("file_train", 0)
    
    file_train = open(f"/home/fieldrayo/Proyects/"
                      f"Github/NeuronalNetwork/NeuronalNetwork-Multilayer/"
                      f"Interface/Commands_files/{file_train}.txt", "r")
    file_train = file_train.read()
    
    if name not in data:
        return f"The name '{name}' is not found in data. Use 'create net' to create a neural network"
    
    x, y = Datatrain.get_datasets(data_s, size, file_train)
    
    data[name]["datatrain"] = [x, y]
    
    return f"\n- {name}: The dataset has been applied successfully -"


def get_help(command):
    commands_help = cmd_help.commands_help
    
    f_commands_help = "\n".join(commands_help)
    
    command_select = command.split()[1]
    
    if command_select not in commands_help and command != "get_help":
        return "Invalid command. Type 'get_help' to see the list of available commands."
    
    if command_select == "get_help":
        return f"Available commands:\n{f_commands_help}"
    else:
        return commands_help[command_select]


def cm_nn(n_inputs, n_hidden, n_outputs):
    return NeuronalNetwork(n_inputs, n_hidden, n_outputs)


def cm_nn_default():
    return NeuronalNetwork(2, [4, 6, 4], 1)


def cm_nn_forward(nn, input_):
    return nn.forward(input_)


def cm_nn_back(name_nn):
    x, y = data[name_nn]["datatrain"]
    nn = data[name_nn]["ID"]
    target = y
    output = cm_nn_forward(nn, x)
    error = output - target
    return nn.backprop(error)


def cm_nn_train(nn, lr, err_max, x, y):
    lr = int(lr) / 100
    err_max = int(err_max) / 100
    return nn.train(x, y, lr, err_max)


def cm_nn_grad(nn, lr):
    lr = int(lr) / 100
    return nn.gradient_descent(lr)


def cm_show_nn():
    return [f": {i}" for n, i in enumerate(data)]


def update(nn):
    nn.main()


commands_mapping = {
    "read_file": read_file,
    "create_file": create_file,
    "create_net": create_net,
    "forward": forward,
    "backpropagation": backpropagation,
    "gradientdescent": gradientdescent,
    "get_value": get_value,
    "set_value": set_value,
    "show_nn": show_nn,
    "show_data": show_data,
    "len_data": len_data,
    "train_net": train_net,
    "show_graphic": show_graphic,
    "set_datatrain": set_datatrain,
    "get_help": get_help
}

# Tareas :
# 1.- Funcion de reconocimiento de comandos escritos en documentos.txt *
# 2.- Ingreso de parametros *
# 3.- Mejorar "Get_help"
# 4.- Guardado de datos (Base de datos)
# 5.- Comunicacion online
