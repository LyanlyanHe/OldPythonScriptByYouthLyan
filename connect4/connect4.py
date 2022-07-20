from colorama import init, Fore, Back, Style

init()


class Connect4:
    def __init__(self):
        """
        For clearness

        [
            [ ... ] <- This is the last row in the board
            ...
            [ ... ] <- This is the fist row
        ]
        """
        self.board = [[0 for _ in range(6)] for _ in range(7)]

    def make_move(self, col):
        if col < 1 or col > 6:
            return "Wrong index"

        count_x = 0
        count_o = 0
        for row in self.board:
            count_x += row.count("X")
            count_o += row.count("O")

        if count_x > count_o:
            sym = "O"
        else:
            sym = "X"

        for index, row in enumerate(self.board):

            if row[col - 1] == 0:
                self.board[index][col - 1] = sym

                # Draw
                ava_spaces = 0
                for x in self.board:
                    ava_spaces += x.count(0)
                else:

                    if ava_spaces == 0:
                        return -1

                # Horizontal Scan
                if sym * 4 in "".join([str(x) for x in self.board[index]]):
                    return sym

                # Vertical Scan
                elif sym * 4 in "".join([str(x) for x in [self.board[y][col - 1] for y in range(0, 7)]]):

                    return sym

                # Diagonals
                else:

                    def left_dia():
                        r = index
                        c = col - 1

                        while True:

                            if c == 0 or r == 6:
                                break

                            r += 1
                            c -= 1

                        output = []

                        while True:

                            if r < 0 or c > 5:
                                return output

                            output.append(self.board[r][c])

                            r -= 1
                            c += 1

                    def right_dia():
                        r = index
                        c = col - 1

                        while True:

                            if c == 5 or r == 6:
                                break

                            r += 1
                            c += 1

                        output = []

                        while True:

                            if r < 0 or c < 0:
                                return output

                            output.append(self.board[r][c])

                            r -= 1
                            c -= 1

                    if sym * 4 in "".join([str(x) for x in left_dia()]) or sym * 4 in "".join(
                            [str(x) for x in right_dia()]):
                        return sym

                return
        else:

            return "This column is full"


def formatter(board, color=False):
    border = "-" * 25
    output = ""

    output += border + "\n"
    for row in reversed(board):
        output += "| " + " | ".join([str(x) for x in row]) + " |\n"
    else:
        output += border

    if color:
        return output.replace("0", " ").replace("X", Fore.RED + "X" + Style.RESET_ALL).replace("O",
                                                                                               Fore.YELLOW + "O" + Style.RESET_ALL)
    return output.replace("0", " ")


if "__main__" == __name__:
    connect4 = Connect4()

    while True:
        print(formatter(connect4.board, color=True))
        result = connect4.make_move(int(input(">>> ")))
        if result in ["X", "O", -1]:

            print(formatter(connect4.board, color=True))
            if result == -1:
                print("Draw")
            else:
                print(f"{result} won!")

            break
        elif result is not None:
            print(result)
