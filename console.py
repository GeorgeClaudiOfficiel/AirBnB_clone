#!/usr/bin/python3
"""
Command interpreter module
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            print(obj_dict[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            del obj_dict[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances
        based or not on the class name
        """
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in obj_dict.values() if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all()
            key = "{}.{}".format(args[0], args[1])
            obj = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])
        storage.save()

    def do_quit(self, arg):
        """
        Quits the command interpreter
        """
        return True

    def do_EOF(self, arg):
        """
        Handles the EOF signal to quit the command interpreter
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

