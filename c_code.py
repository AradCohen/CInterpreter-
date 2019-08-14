from jinja2 import *
import subprocess

class CodeC:

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.template = self.env.get_template('main.c')
        self.user_code = []
        self.includes = []
        self.all_code = []

    def add_line(self, code_line):
        with open("user.c", "w") as file:
            if code_line.startswith("#include") or code_line.startswith("# include"):
                self.includes.append(code_line)
            else:
                self.user_code.append(code_line)
            file.write(self.template.render(user_code_lines= self.user_code, includes=self.includes))
            self.all_code.append(code_line)

    def run_c_code(self):
        
        result_gcc = subprocess.run(["gcc", "user.c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = result_gcc.stderr.decode()
        if stderr != "":
            del self.user_code[-1]
            return stderr

        result_binary = subprocess.run(["./a.out"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stderr = result_binary.stderr.decode()
        stdout = result_binary.stdout.decode()
        if stderr != "":
            del self.user_code[-1]
            return stderr
        if stdout != "":
            del self.user_code[-1]
            return stdout
        return ""




