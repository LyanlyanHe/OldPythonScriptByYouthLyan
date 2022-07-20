# from abc import ABC, abstractmethod
#
# """
# TOOLS for AI
# """
#
# def board_index(board: list):
#     output = []
#
#     for index, x in enumerate(board):
#         if x == "O" or x == "X":
#             output.append(x)
#             continue
#
#         output.append(index)
#
#     return output
#
# def formatter(board: list):
#     border = "-" * 9 + "\n"
#     row = "| {} {} {} |\n"
#
#     output = border
#
#     for x in range(0, 9, 3):
#          output += row.format(*board[x: x + 3])
#     else:
#         output += border
#
#     return output.replace("0", " ")
#
#
# """
# Classes for the Game
# """
# class Game:
#     def __init__(self, board=None):
#
#         if board is None:
#             board = [0 for _ in range(9)]
#
#         self.board = board
#
#     @staticmethod
#     def board_status(board):
#
#         # Row Check
#         pass
#
#     def making_move(self, index):
#         sym = "X" if self.board.count("X") == self.board.count("O") else "O"
#
#         self.board[index] = sym
#
#         return self.board_status(self.board)
#
#
#
# """
# Players
# """
# class Player(ABC):
#     def __init__(self, game: Game):
#         self.board = game.board
#
#     @abstractmethod
#     def make_move(self):
#         pass
#
#
# class RandomPlayer(Player):
#     def __init__(self, game: Game):
#         super().__init__(game)
#
#     def make_move(self):
#         pass
#
#
# class SmartPlayer(Player):
#     def __init__(self, game: Game):
#         super().__init__(game)
#
#     def make_move(self):
#         pass
#
# class HumanPlayer(Player):
#     def __init__(self, game: Game):
#         super().__init__(game)
#
#     def make_move(self):
#         pass
#
#
# """
# MAIN LOOPS
# """
# if "__main__" == __name__:
#     pass
