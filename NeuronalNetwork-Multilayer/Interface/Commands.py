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


def test_command(command, size, type_op):
    words = command.split()
    
    if len(words) < size + 1:
        print('Invalid command, missing arguments.')
        return 0
    
    args = {f"v{i}": word for i, word in enumerate(words)}
    
    if type_op == 0 and args["v1"] in data:
        print("A neural network with that name has already been created.")
        return 0
    
    if type_op == 1 and args["v1"] not in data:
        print("The neural network is not present in the data.")
        return 0
    
    return args


def create_net(command):
    args = test_command(command, 1, 0)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    
    data[name_nn] = {}
    data[name_nn]["ID"] = cm_nn()
    
    return f"{name_nn}: {data[name_nn]}\n- Has been created -"


def create_default_net(command):
    args = test_command(command, 1, 0)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    
    data[name_nn] = {}
    data[name_nn]["ID"] = cm_nn_default()
    
    return f"{name_nn}: {data[name_nn]}\n- Has been created -"


def forward(command):
    args = test_command(command, 1, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    input_ = command.split(f"{name_nn} ")[-1]
    input_ = ast.literal_eval(input_)
    
    return f"The current prediction is: {cm_nn_forward(data[name_nn]['ID'], input_)[0]}"


def backpropagation(command):
    args = test_command(command, 1, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    
    data[name_nn]["backpropagation"] = cm_nn_back(name_nn)
    
    return f"- {name_nn}: The backpropagation has been applied -"


def gradientdescent(command):
    args = test_command(command, 2, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    lr = args["v2"]
    
    data[name_nn]["gradientdescent"] = cm_nn_grad(data[name_nn]["ID"], lr)
    return f"- {name_nn}: The gradient decent has been applied -"


def get_value(command):
    args = test_command(command, 3, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    value = args["v2"]
    n_data = args["v3"]
    
    if not hasattr(data[name_nn]["ID"], value):
        return "The neural network is missing from the data"
    
    s_data = getattr(data[name_nn]['ID'], value)
    
    if len(n_data) != 1:
        n_data = n_data.split("-")
        n_data = list(map(int, n_data))
        return s_data[n_data[0] - 1:n_data[1] - 1]
    elif n_data == "*":
        return s_data
    else:
        n_data = list(map(int, n_data))[0]
        return s_data[n_data - 1]


def set_value(command):
    args = test_command(command, 3, 1)
    if args == 0:
        return ""
    
    arg_value = get_value(f"get_value {args['v1']} {args['v2']} *")
    
    if isinstance(arg_value, list):
        name_nn = command.split()[1]
        value = args["v2"]
        new_value = command.split(f"{args['v2']} ")[-1]
        new_value = ast.literal_eval(new_value)
    else:
        name_nn = args["v1"]
        value = args["v2"]
        new_value = args["v3"]
    
    if not hasattr(data[name_nn]["ID"], f"{value}"):
        return "The neural network is missing from the data"
    
    setattr(data[name_nn]["ID"], value, new_value)
    update(data[name_nn]["ID"])
    
    return f"{value} = {new_value}"


def show_nn(command):
    if len(data) == 0:
        return "First create a neural network with 'create_net (ID)'"
    
    if len(command.split()) != 1:
        return "the command takes no parameters"
    
    return "\n".join(cm_show_nn())


def show_data(command):
    args = test_command(command, 3, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    value = args["v2"]
    n_data = args["v3"]
    
    s_data = data[name_nn][value]
    
    if len(n_data) != 1:
        n_data = n_data.split("-")
        n_data = list(map(int, n_data))
        return s_data[n_data[0] - 1:n_data[1] - 1]
    elif n_data == "*":
        return s_data
    elif True:
        n_data = list(map(int, n_data))[0]
        return s_data[n_data - 1]


def len_data(command):
    args = test_command(command, 2, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    value = args["v2"]
    
    if isinstance(data[name_nn], list):
        return f"len {value} = {len(data[name_nn][value])}"
    
    return f"len {value} = 1"


def train_net(command):
    args = test_command(command, 3, 1)
    if args == 0:
        return 0
    
    name_nn = args["v1"]
    lr = args["v2"]
    err_max = args["v3"]
    
    x, y = data[name_nn]["datatrain"]
    
    data[name_nn]["train"] = cm_nn_train(data[name_nn]["ID"], lr, err_max, x, y)
    return f"\n- {name_nn}: The train has been applied -"


def show_graphic(command):
    args = test_command(command, 3, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    type_graphic = args["v2"]
    plt_type = args["v3"]
    
    x, y = data[name_nn][type_graphic]
    
    plt.clf()
    if plt_type == "plot":
        plt.plot(x, y)
    elif plt_type == "scatter":
        plt.scatter(x[:, 0], x[:, 1], c=y)
    
    plt.show()
    return ""


def set_datatrain(command):
    args = test_command(command, 4, 1)
    if args == 0:
        return ""
    
    name_nn = args["v1"]
    data_s = args["v2"]
    size = int(args["v3"])
    type_dataset = int(args["v4"])
    
    x, y = Datatrain.get_datasets(data_s, size, type_dataset)
    
    data[name_nn]["datatrain"] = [x, y]
    
    return f"\n- {name_nn}: The dataset has been applied successfully -"


def get_help(command):
    commands_help = cmd_help.commands_help
    
    f_commands_help = "\n".join(commands_help)
    
    command_select = command.split()[0]
    
    if command_select not in commands_help and command != "help":
        return "Invalid command. Type 'help' to see the list of available commands."
    
    if command_select == "help":
        return f"Available commands:\n{f_commands_help}"
    else:
        return commands_help[command_select]


def cm_nn():
    parameters = [int(input("- Set inputs layer -\n>>> ")),
                  input("- Set hidden layer -\n>>> ").split(),
                  int(input("- Set output layer -\n>>> "))]
    
    parameters[1] = list(map(int, parameters[1]))
    
    return NeuronalNetwork(parameters[0], parameters[1], parameters[2])


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
