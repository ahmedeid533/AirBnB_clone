#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = "(hbnb) "

    def emptL(self):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == '__main__':

    HBNBCommand().cmdloop()
