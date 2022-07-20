from colorama import Fore, init, Style
import datetime

init()

class Bill:
    def __init__(self):
        self.table = []
        self.total_sum = 0
        self.exception = 0

    def clear(self):
        self.table = []

    def input(self, row: list):

        self.table.append([row, int(row[0] * row[1]) if int(row[0] * row[1]) - (row[0] * row[1]) else row[0] * row[1]])
        print(row, Fore.GREEN + str(int(row[0] * row[1]))+ Style.RESET_ALL)

    def initialize(self):
        row = " {} x {} = {} \n"
        output = ""

        sum = 0
        for x in self.table:
            output += row.format(x[0][0], x[0][1], Fore.YELLOW + str(x[1]) + Style.RESET_ALL)
            sum += x[1]

        output += f"SUM: {Fore.GREEN + str(sum) + Style.RESET_ALL}"

        return output, sum

    def edit(self, row: int, value: list):

        self.table[row] = [value, value[0] * value[1]]

    def loop(self):
        """
        MaIN
        """
        while True:

            input_ = input(">> ")

            if input_ == "clear":
                self.clear()
            elif input_ == "":
                result = self.initialize()
                self.exception = result[1]
                self.total_sum += result[1]
                print(result[0])

            elif input_.startswith("edit"):

                input_ = [float(x) for x in input_.replace("edit", "").strip().split()]

                self.edit(int(input_[0]), [input_[1], input_[2]])
                result = self.initialize()
                print(result[0])
                self.total_sum -= self.exception
                self.exception = result[1]
                self.total_sum += result[1]

            elif input_ == "end":
                print(Fore.RED + str(self.total_sum) + Style.RESET_ALL, "Bye")
                break
            else:
                self.input([float(x) for x in input_.split()])


if "__main__" == __name__:
    bill = Bill()
    bill.loop()

