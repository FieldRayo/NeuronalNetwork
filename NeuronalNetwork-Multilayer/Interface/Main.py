from Commands import *
from Correct_command import correct_command
import random

# Diccionario de comandos con sus respectivas funciones
commands_mapping = {
    "create_net": create_net,
    "create_default_net": create_default_net,
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
    "help": help,
}
        

while True:
    cmd_user = input(">>> ")
    if cmd_user == "":
        continue
    
    probable_cm = correct_command(cmd_user, commands_mapping)
    
    cmd_name = cmd_user.split()[0]
    if cmd_name in commands_mapping:
        print(commands_mapping[cmd_name](cmd_user))
    elif probable_cm[1] > 48:
        print(f"Did you mean: '{probable_cm[0]}'?")
    else:
        print("Unknown command. Please enter a valid command.")
    
    print("\n")
