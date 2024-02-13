#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parses the arguments."""
    return arg.split()


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[instance_key]
                storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = parse(arg)
        if len(args) == 0:
            for obj in storage.all().values():
                print(obj)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if key.startswith(args[0]):
                    print(storage.all()[key])

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[instance_key]
                setattr(obj, args[2], args[3])
                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
