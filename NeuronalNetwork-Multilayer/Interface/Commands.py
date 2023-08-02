import matplotlib.pyplot as plt
import ast

import sys
import io
import os

# Agregar el directorio que contiene Multilayer.py al sys.path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from Multilayer import NeuronalNetwork

from Datatrain import *

data = {}


def test_command(command, vals, type):
    args = {}
    
    try:
        for i in range(vals + 1):
            args[f"v{i}"] = command.split()[i]

        if args["v1"] in data and type == 0:
            print("A neural network with that name has already been created")
            return 0

        if args["v1"] not in data and type == 1:
            print("The neural network is missing from the data")
            return 0
    except:
        help(command)
        return 0

    return args


def create_net(command):
    args = test_command(command, 1, 0)
    if args == 0: return 0
    name_nn = args["v1"]

    data[name_nn] = {}
    data[name_nn]["ID"] = cm_nn()
    print(f"{name_nn}: {data[name_nn]}\n- Has been created -")


def create_default_net(command):
    args = test_command(command, 1, 0)
    if args == 0: return 0
    name_nn = args["v1"]

    data[name_nn] = {}
    data[name_nn]["ID"] = cm_nn_default()
    print(f"{name_nn}: {data[name_nn]}\n- Has been created -")


def forward(command):
    args = test_command(command, 1, 1)
    if args == 0: return 0
    name_nn = args["v1"]

    data[name_nn]["forward"] = cm_nn_forward(data[name_nn]["ID"])
    print(f"- {name_nn}: The forward has been applied -")


def backpropagation(command):
    args = test_command(command, 1, 1)
    if args == 0: return 0
    name_nn = args["v1"]

    data[name_nn]["backpropagation"] = cm_nn_back(data[name_nn]["ID"])

    print(f"- {name_nn}: The backpropagation has been applied -")

def gradientdescent(command):
    args = test_command(command, 2, 1)
    if args == 0: return 0
    name_nn = args["v1"]
    lr = args["v2"]

    data[name_nn]["gradientdescent"] = cm_nn_grad(data[name_nn]["ID"], lr)
    print(f"- {name_nn}: The gradient decent has been applied -")

def get_value(command):
    args = test_command(command, 3, 1)
    if args == 0: return 0
    name_nn = args["v1"]
    value = args["v2"]
    n_data = args["v3"]

    if not hasattr(data[name_nn]["ID"], f"{value}"):
        print("The neural network is missing from the data")
        return

    s_data = getattr(data[name_nn]['ID'], f'{value}')
    try:
        if len(n_data) != 1:
            n_data = n_data.split("-")
            n_data = list(map(int, n_data))
            print(f"{value} = {s_data[n_data[0] - 1:n_data[1] - 1]}")
        elif n_data == "*":
            print(f"{value} = {s_data}")
        else:
            n_data = list(map(int, n_data))[0]
            print(f"{value} = {s_data[n_data - 1]}")
    except:
        print(f"{value} = {s_data}")


def set_value(command):
    if command.split()[2] == "n_hidden":
        name_nn = command.split()[1]
        value = "n_hidden"
        new_value = command.split("n_hidden ")[-1]
        new_value = ast.literal_eval(new_value)
    else:
        args = test_command(command, 3, 1)
        if args == 0: return 0
        name_nn = args["v1"]
        value = args["v2"]
        new_value = int(args["v3"])

    if name_nn not in data:
        print("The neural network is missing from the data")
        return

    if not hasattr(data[name_nn]["ID"], f"{value}"):
        print("The neural network is missing from the data")
        return

    setattr(data[name_nn]["ID"], value, new_value)
    update(data[name_nn]["ID"])
    print(f"{value} = {new_value}")


def show_nn(command):
    if len(data) == 0:
        print("First create a neural network with 'create_net (ID)'")
    else:
        show_nn()


def show_data(command):
    args = test_command(command, 3, 1)
    if args == 0: return 0
    name_nn = args["v1"]
    value = args["v2"]
    n_data = args["v3"]

    s_data = data[name_nn][value]
    try:
        if len(n_data) != 1:
            n_data = n_data.split("-")
            n_data = list(map(int, n_data))
            print(s_data[n_data[0] - 1:n_data[1] - 1])
        elif n_data == "*":
            print(s_data)
        else:
            n_data = list(map(int, n_data))[0]
            print(s_data[n_data - 1])
    except:
        print(s_data)


def len_data(command):
    args = test_command(command, 2, 1)
    if args == 0: return 0
    name_nn = args["v1"]
    value = args["v2"]

    try:
        print(f"len {value} = {len(data[name_nn][value])}")
    except:
        print(f"len {value} = 1")


def train_net(command):
    args = test_command(command, 3, 1)
    if args == 0: return 0
    name_nn = args["v1"]
    lr = args["v2"]
    err_max = args["v3"]

    data[name_nn]["train"] = cm_nn_train(data[name_nn]["ID"], lr, err_max)
    print(f"\n- {name_nn}: The train has been applied -")


def show_graphic(command):
    args = test_command(command, 1, 1)
    if args == 0: return 0
    name_nn = args["v1"]

    x_axis = data[name_nn]["train"][0]
    errors = data[name_nn]["train"][1]

    plt.clf()
    plt.plot(x_axis, errors)
    plt.show()


def help(command):
    all_commands = {
        "create_net": "- create_net (ID): Create a new neural network with the given ID.",
        "create_default_net": "- create_default_net (ID): Create a new neural network with default parameters and the given ID.",
        "forward": "- forward (ID): Perform forward propagation on the neural network with the given ID.",
        "backpropagation": "- backpropagation (ID): Perform backpropagation on the neural network with the given ID.",
        "gradientdescent": "- gradientdecent (ID) (Learning Rate 1 - 100): Perform gradient descent on the neural network with the given ID.",
        "get_value": "- get_value (ID) (value) (n_data | *, 1, 2, 3.., 1-99): Get a specific value from the neural network with the given ID.",
        "set_value": "- set_value (ID) (value) (new_value): Set a specific value in the neural network with the given ID.",
        "show_nn": "- show_nn: Show the names of all created neural networks.",
        "show_data": "- show_data (ID) (data) (n_data | *, 1, 2, 3.., 1-99): Show specific data from the neural network with the given ID.",
        "len_data": "- len_data (ID) (data): Show the length of specific data from the neural network with the given ID.",
        "train_net": "- train_net (ID) (Learning Rate 1 - 100) (Tolerance 1 - 100): Train the neural network with the given ID.",
        "show_graphic": "- show_graphic (ID): Show a graph of the training errors for the neural network with the given ID.",
    }

    command_select = command.split()[0]

    if command_select not in all_commands and command != "help":
        print("Invalid command. Type 'help' to see the list of available commands.")
        return

    if command_select == "help":
        print("Available commands:")
        [print(f"{x}") for x in all_commands]
    else:
        print(all_commands[command_select])


def cm_nn():
    parameters = [int(input("- Set inputs layer -\n>>> ")),
                  input("- Set hidden layer -\n>>> ").split(),
                  int(input("- Set output layer -\n>>> "))]

    parameters[1] = list(map(int, parameters[1]))

    return NeuronalNetwork(parameters[0], parameters[1], parameters[2])


def cm_nn_default():
    return NeuronalNetwork(2, [4, 6, 4], 1)


def cm_nn_forward(nn):
    return nn.forward(inputs)


def cm_nn_back(nn):
    output = cm_nn_forward(nn)
    error = output - target
    return nn.backprop(error)


def cm_nn_train(nn, lr, err_max):
    X = inputs
    y = target
    lr = int(lr) / 100
    err_max = int(err_max) / 100
    return nn.train(X, y, lr, err_max)

def cm_nn_grad(nn, lr):
    lr = int(lr) / 100
    return nn.gradient_descent(lr)


def cm_show_nn():
    [print(f": {i}") for n, i in enumerate(data)]


def update(nn):
    nn.main()
