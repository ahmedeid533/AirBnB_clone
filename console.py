#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb) "

    __get_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def default(self, arg):
        """continue the console when unknown command passed in"""
        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count
        }
        args = arg.split('.')
        class_name = args[0]
        commandAndID = args[1].split('(')
        command = commandAndID[0]
        ID = commandAndID[1][:-2]
        AllArgs = []
        AllArgs.append(class_name)
        AllArgs.append(ID)
        if command in commands.keys():
            send = "{} {}".format(class_name, AllArgs)
            return commands[command](send)
        print("*** Unknown syntax: {}".format(arg))
        return False
    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_all(self, arg):
        """print opjects of one class or all classes"""
        opjects = []
        args = split(arg)
        if arg in self.__get_class or not arg:
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    opjects.append(obj.__str__())
                elif len(args) == 0:
                    opjects.append(obj.__str__())
            print(opjects)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = split(arg)
        objcts_storage = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__get_class.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objcts_storage:
            print("** no instance found **")
        else:
            print(objcts_storage["{}.{}".format(args[0], args[1])])

    def do_create(self, arg):
        """Create a new class instance"""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__get_class:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_destroy(self, arg):
        """Delete a class instance"""
        args = split(arg)
        objcts_storage = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__get_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objcts_storage.keys():
            print("** no instance found **")
        else:
            del objcts_storage["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, arg):
        """Update a class instance"""
        args = split(arg)
        objcts_storage = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.__get_class:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in objcts_storage.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False

        object = objcts_storage["{}.{}".format(args[0], args[1])]
        if args[2] in object.__class__.__dict__.keys():
            make_sure = type(object.__class__.__dict__[args[2]])
            object.__dict__[args[2]] = make_sure(args[3])
        else:
            object.__dict__[args[2]] = args[3]
        storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        args = split(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
