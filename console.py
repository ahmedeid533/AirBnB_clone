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

    __get_class={
        "BaseModel":BaseModel,
        "User":User,
        "State":State,
        "City":City,
        "Place":Place,
        "Amenity":Amenity,
        "Review":Review
    }
    def default(self, arg):
        """continue the console when unknown command passed in"""
        pass

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
        opjects =[]
        args = split(arg)
        if arg in self.__get_class:
            for obj in storage.all().values():
                print(obj.__class__.__name__)
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    opjects.append(obj.__str__())
                elif len(args) == 0:
                    opjects.append(obj.__str__())
            print(opjects)
    

if __name__ == '__main__':

    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Bar"
    my_user.email = "airbnb@mail.com"
    my_user.password = "root"
    storage.save()
    HBNBCommand().cmdloop()
