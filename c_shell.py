from c_code import *

def main():
    c_code = CodeC()
    while True:
        command = input(">> ")
        c_code.add_line(command)
        c_code.run_c_code()


if __name__ == '__main__':
    main()