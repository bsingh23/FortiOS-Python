#!/usr/bin/python3
import sys
from datetime import datetime

#Function to Open Files, Read content and return a List
#def open_file(filename):
#    with open(filename) as f:
#        lines = f.read().splitlines()
#        return lines

def open_file(filename):
    try:
        with open (filename) as f:
            lines = f.read().splitlines()
            return lines
    except FileNotFoundError as e:
        print(e)
        sys.exit()

#Function to create a new file which contains the cli commands required
def execute():
    time_now = datetime.today().strftime('%Y%m%d-%H%M%S')  
    filename = "forti_cmd_output_" + time_now + ".txt"
    with open(filename, "w") as f:
        for id in policy_id:
            f.write(f'edit {id}\n')
            for cmds in config_lines:
                f.write(f'{cmds}\n')
            f.write("next\n")
        f.write("end")

if __name__ == "__main__":
    #Get all Policy id
    policy_id = open_file("policy_id.txt")
    #Get all commands
    config_lines = open_file("commands.txt")
    #Run main func
    execute()