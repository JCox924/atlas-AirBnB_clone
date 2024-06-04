#!/usr/bin/python3
import cmd

"""
This module contains the entry point for the command interpreter
for the AirBnB clone project.
"""

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
