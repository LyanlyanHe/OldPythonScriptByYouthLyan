from colorama import Fore, Style, init
import math

init()


class TicTacToe:
    def __init__(self, board=None):
        self.board = board if board is not None else [0 for _ in range(9)]

    def make_move(self, index):

        if index < 0 or index > 8:
            return "Invalid value"
        elif self.board[index] != 0:
            return "This place is taken"

        sym = "X" if self.board.count("X") == self.board.count("O") else "O"
        self.board[index] = sym

        if self.board.count(0) == 0:
            return -1

        # Horizontal scan
        if [self.board[x] for x in range(math.floor(index / 3) * 3, math.floor(index / 3) * 3 + 3)].count(sym) == 3:
            return sym

        # Vertical scan
        if [self.board[x] for x in range(index % 3, index % 3 + 9, 3)].count(sym) == 3:
            return sym

        # Diagonals
        if index not in [x for x in range(1, 8, 2)]:

            if [self.board[x] for x in range(0, 9, 4)].count(sym) == 3 or [self.board[x] for x in range(2, 7, 2)].count(sym) == 3:
                return sym

        return


def formatter(board: list, color=False):
    border = "-" * 9
    row = "\n| {} |"
    output = ""

    output += border
    for i in range(0, 9, 3):
        output += row.format(" ".join([str(x) for x in [board[y] for y in range(i, i + 3)]]))
    else:
        output += "\n" + border

    return output.replace("0", " ") if not color else output.replace("0", " ").replace("X", Fore.RED + "X" + Style.RESET_ALL).replace("O", Fore.BLUE + "O" + Style.RESET_ALL)


if "__main__" == __name__:
    game = TicTacToe()

    while True:
        print(formatter(game.board, color=True))
        result = game.make_move(int(input(">> ")) - 1)

        if result in ["X", "O", -1]:
            print(formatter(game.board, color=True))
            if result == -1:
                print("Draw")
                break

            print(f"{result} won!")
            break

        elif result is not None:
            print(result)