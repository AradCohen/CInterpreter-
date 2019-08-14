from c_code import *
from curses import *

LINE_BREAK = 10


class CursesHandling:

    def __init__(self, codeCObject, stdscr):
        """
        :param codeCObject: A C code object in order to take the user's commands
        """
        self.stdscr = stdscr
        self.commands_history = []
        self.codeC = codeCObject
        self.current_command = ""
        self.current_idx = None
        self.up_counter = 0
        self.command = ""

    def handling_keys(self, key, current_command):
        """
        handling specials keys, such as KEY_UP, KEY_DOWN, etc, among with regular keys
        :param key: the key from the user
        :param current_command: the current user commands
        :return: true or false if
        """
        if key == KEY_UP:
            self.update_commands_history()
            self.up_counter += 1
            self.current_idx -= 1
            return self.commands_history[self.current_idx]

        elif key == KEY_DOWN:
            self.update_commands_history()
            if self.up_counter == 0:
                return current_command
            else:
                self.current_idx += 1
                self.up_counter -= 1
                return self.commands_history[self.current_idx]

        else:
            return current_command + chr(key)

    def get_user_command(self):
        self.update_commands_history()
        key = 0
        self.command = ""
        self.up_counter = 0

        while key != LINE_BREAK:
            key = self.stdscr.getch()
            self.command = self.handling_keys(key, self.command)

        return self.command

    def update_commands_history(self):
        self.current_idx = len( self.codeC.all_code)
        self.commands_history = self.codeC.all_code + [self.command]