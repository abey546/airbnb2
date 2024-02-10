#!/usr/bin/python3 
import cmd
from models import storage
from models.base_model import BaseModel
import json
class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""
    prompt = "(hbnb) "
    classes = {"BaseModel"}
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
        else:
            print(eval(tokens[0])().id)
        #new_instance = HBNBCommand.classes[tokens[0]]()
        #storage.new(new_instance)
        storage.save()
        #print(new_instance.id)
    def do_show(self, args):
        tokens = args.split(" ")
        """Displays string representation of an instance"""
        if not args:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        class_name = tokens[0]
        obj_id = tokens[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        print(all_objs[key])
    def do_destroy(self, args):
        tokens = args.split(" ")
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(tokens) < 2:
            print("** instance id missing **")
            return
        class_name = tokens[0]
        obj_id = tokens[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]
        storage.save()
    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
    Display string representations of all instances of a given class.
    If no class is specified, displays all instantiated objects."""
        tokens = arg.split(" ")
        if len(tokens) > 0 and tokens[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(tokens) > 0 and tokens[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(tokens) == 0:
                    obj_list.append(obj.__str__())
            for obj_str in obj_list:
                print(obj_str)




if __name__ == '__main__' :
    HBNBCommand().cmdloop()