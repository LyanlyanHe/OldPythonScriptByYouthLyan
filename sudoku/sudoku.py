import random

class Sudoku():
    def __init__(self, board=None):
        if board is None:
            board = []
        self.board = board


    def __str__(self):
        return formatter(self.board)

    def __repr__(self):
        return self.board

    def generate(self):
        self.board.clear()

        first_square = [x for x in range(1, 10)]
        random.shuffle(first_square)
        self.board.append(first_square)

        for _ in range(8):
            self.board.append([0 for _ in range(9)])

        self.board = sudoku_solver(self.board)

        coords = [(x, y) for x in range(9) for y in range(9)]
        answer = self.board.copy()
        amounts = random.randint(29, 53)

        for _ in range(amounts):
            remove_spot = random.choice(coords)
            coords.remove(remove_spot)

            self.board[remove_spot[0]][remove_spot[1]] = 0

        return answer


def formatter(board):
    output = ""
    border = "-" * 8 * 3 + "-\n"
    row = "| {} | {} | {} |\n"

    for x in range(3):

        output += border

        for y in range(3):
            output += row.format(
                " ".join([str(x) for x in board[x * 3][y * 3: y * 3 + 3]]),
                " ".join([str(x) for x in board[x * 3 + 1][y * 3: y * 3 + 3]]),
                " ".join([str(x) for x in board[x * 3 + 2][y * 3: y * 3 + 3]])
            )
    else:
        output += border

    return output.replace("0", " ")


def sudoku_valid(board):
    # square check
    for square in board:

        for num in range(1, 10):

            if square.count(num) > 1:
                return False

    # row check
    for index in range(0, 8, 3):

        for col in range(0, 8, 3):

            row = []

            for square in board[index: index + 3]:
                row.extend(square[col: col + 3])


            for x in range(1, 10):

                if row.count(x) > 1:

                    return False

    # col check
    for index in range(3):

        for row in range(3):

            col = []

            for square in board[index: index + 7: 3]:
                col.extend(square[row: row + 7: 3])

            for x in range(1, 10):
                if col.count(x) > 1:
                    return False

    return True

def sudoku_solver(board):

    first_missing = None

    for x in range(9):
        for y in range(9):

            if board[x][y] == 0:
                first_missing = (x, y)
                break

    if first_missing is None:
        return board

    for num in range(1, 10):
        board[first_missing[0]][first_missing[1]] = num

        if sudoku_valid(board) is False:
            continue

        result = sudoku_solver(board)

        if result is False:
            continue

        return result
    else:
        board[first_missing[0]][first_missing[1]] = 0
        return False




if "__main__" == __name__:
    board = [
        [7, 9, 0, 0, 0, 0, 0, 4, 3],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 2, 8, 7, 0, 4, 0, 9, 0],
        [0, 2, 9, 0, 0, 0, 0, 3, 1],
        [0, 5, 0, 2, 0, 4, 0, 9, 0],
        [0, 3, 6, 0, 0, 0, 0, 4, 7],
        [0, 6, 4, 0, 0, 0, 9, 8, 0],
        [0, 0, 8, 0, 0, 0, 3, 0, 0],
        [0, 5, 0, 6, 0, 2, 0, 7, 1]
    ]

    # U can make a board using UR board
    ur_board = Sudoku(board)
    print("Ur own board")
    print(ur_board)


    # Or generate it
    generate_board = Sudoku()
    generate_board.generate()
    print("\nGenerated board")
    print(generate_board)

    # U can make a board pretty if it is not "Sudoku" instance
    print("\nBefore")
    print(board)
    print("After formatting")
    print(formatter(board))

    # You can solve a board
    print("\nSolving ur own board")
    print(formatter(sudoku_solver(board)))
    print("Solving ur board instance")
    print(formatter(sudoku_solver(ur_board.board)))
    print("Solving generated board")
    print(formatter(sudoku_solver(generate_board.board)))

    # You can check if it is valid sudoku board
    print("\nOH mr python pls tell me is my board a VALID board")
    print(sudoku_valid(board))
