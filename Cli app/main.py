import calculator

class CLI:
    def math(self, arg):
        args = [x.strip() for x in arg.split("-v")]

        variables = {}
        if len(args) > 1:
            for x in args[1].split():
                variables.update({x.split("=")[0].strip(): float(x.split("=")[1].strip())})

        print(calculator.calculate(args[0], variables=variables), end="\n\n")

    def help(self, arg=None):
        math = """Commands manual for math
        math [equation] [options]
With the math commands you can calculate easy math such as 12 + 85 - (5 + 4)
Options are also optional but you must include equation E.g math 12+85-(5+4)

Support Signs : + - * / % ^(Exponent) ( )

Options for math
-v ~ for declaring variables E.g 'math a+B -v a=15 b=48'
"""

        all_ = """Manual
math ~ for calculating basic math
"""

        if arg is None:
            print(all_)
        elif arg == "math":
            print(math)

    def main(self):
        while True:

            command = input("$ ")

            if command.startswith("math"):
                self.math(command.replace("math", "", 1).strip())
            elif command.startswith("help"):
                arg_for_help = command.replace("help", "", 1).strip()

                self.help(arg_for_help.lower() if arg_for_help else None)
            elif command == "exit":
                break
            else:
                print("Unknown command", end="\n\n")



if "__main__" == __name__:
    cli = CLI()
    cli.main()
