from Commands import *
from Correct_command import correct_command
import random

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
