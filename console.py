#!/usr/bin/python3
"""
This module contains the entry point for the command interpreter
for the AirBnB clone project.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, User, State, City, Place, Amenity, or Review, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        if arg:
            print([str(obj) for key, obj in objects.items() if key.startswith(arg)])
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        try:
            if attr_name in ('number_rooms', 'number_bathrooms', 'max_guest', 'price_by_night'):
                attr_value = int(attr_value)
            elif attr_name in ('latitude', 'longitude'):
                attr_value = float(attr_value)
        except ValueError:
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()

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
