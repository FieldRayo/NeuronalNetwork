commands_help = {
    "read_file": "- read_file --file 'file_name': "
                 "Run commands from a text file",
    "create_file": "- create_file --file 'file_name': "
                   "Creates a text file in which commands can be executed",
    "create_net": "- create_net --name 'name' (default='NN1') --n_inputs 'value' (default=2)"
                  " --n_hidden 'value' (default=[4, 6, 4]) --n_outputs 'value' (default=1): "
                  "Create a new neural network with the given ID.",
    "forward": "- forward --name 'name' --input list: "
               "Perform forward propagation using the specified input on the neural network with the given name.",
    "backpropagation": "- backpropagation --name 'name': "
                       "Perform backpropagation on the neural network with the given name.",
    "gradientdescent": "- gradientdescent --name 'name' --lr float: "
                       "Perform gradient descent on the neural"
                       " network with the given name using the specified learning rate.",
    "get_value": "- get_value --name 'name' --value 'value' --index 'index': "
                 "Get a specific value from the neural network with the given name. "
                 "The index can be a number, a range (start-end), or '*' for all values.",
    "set_value": "- set_value --name 'name' --value 'value' --new_value 'new_value': "
                 "Set a specific value in the neural network with the given name.",
    "show_nn": "- show_nn: "
               "Show the names of all created neural networks.",
    "show_data": "- show_data --name 'name' --value 'value' --index 'index': "
                 "Show specific data from the neural network with the given name. "
                 "The index can be a number, a range (start-end), or '*' for all values.",
    "len_data": "- len_data --name 'name' --value 'value': "
                "Show the length of specific data from the neural network with the given name.",
    "train_net.txt": "- train_net.txt --name 'name' --lr float --err_max float: "
                 "Train the neural network with the given name using the specified learning rate and error tolerance.",
    "show_graphic": "- show_graphic --name 'name' --graphic 'graphic' --type 'type': "
                    "Show a graph of the training errors for the neural network with the given name. "
                    "The type of graphic can be 'plot' or 'scatter'.",
}
