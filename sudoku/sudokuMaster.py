from sudoku import *

while True:

    command = input("$ ").lower()

    if command == "break":

        print("Bye have a good time")
        break

    if command == "start":
        board = []
        for x in range(1, 10):
            board.append([int(x) for x in input(f"{x} Square >> ")])

        if sudoku_valid(board) is False:
            print("This sudoku board isn't valid")
        else:
            print(formatter(sudoku_solver(board)))

