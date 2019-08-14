from c_code import *
import curses
from curses import *


def main(stdscr):
    stdscr.clear()
    c_code = CodeC()
    curses.echo()

    while True:
        stdscr.addstr(">> ")
        command = stdscr.getstr().decode()

        c_code.add_line(command)
        result = c_code.run_c_code()
        stdscr.addstr(result + "\n")
        stdscr.refresh()

if __name__ == '__main__':
    wrapper(main)