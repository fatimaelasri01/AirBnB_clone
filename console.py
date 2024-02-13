import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex
import json


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
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance of a given id.
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = shlex.split(arg)
        if args and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        instances = []
        if args:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    instances.append(str(obj))
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[instance_key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = shlex.split(arg)
        if args and args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        instances = []
        if args:
            for key, obj in storage.all().items():
                if key.split('.')[0] == args[0]:
                    instances.append(str(obj))
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_count(self, arg):
        """Usage: <class name>.count()
        Count the number of instances of a class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        count = 0
        for key in storage.all():
            if key.startswith(class_name + "."):
                count += 1
        print(count)

    def do_show(self, arg):
        """Usage: <class name>.show(<id>)
        Show an instance based on its ID."""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[instance_key])

    def do_destroy(self, arg):
        """Usage: <class name>.destroy(<id>)
        Destroy an instance based on its ID."""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[instance_key]
        storage.save()

    def do_update(self, arg):
        """Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
        Update an instance based on its ID."""
        args = shlex.split(arg)
        if len(args) < 4:
            print("** value missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        obj = storage.all()[instance_key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_update_dict(self, arg):
        """Usage: <class name>.update(<id>, <dictionary representation>)
        Update an instance based on its ID with a dictionary."""
        args = shlex.split(arg)
        if len(args) < 3:
            print("** dictionary missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        instance_id = args[1]
        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        try:
            dictionary_str = args[2]
            dictionary = json.loads(dictionary_str)
        except ValueError:
            print("** invalid dictionary **")
            return
        obj = storage.all()[instance_key]
        for attr_name, attr_value in dictionary.items():
            setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
