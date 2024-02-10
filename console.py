#!/usr/bin/python3 
import cmd
from models import storage
from models.base_model import BaseModel
import json
class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True
    def emptyline(self):
        """Empty line"""
        pass
    def do_create(self, args):
        tokens = args.split(" ")
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[tokens[0]]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

if __name__ == '__main__' :
    HBNBCommand().cmdloop()