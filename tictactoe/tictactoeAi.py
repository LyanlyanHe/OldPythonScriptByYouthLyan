from tictactoe import TicTacToe, formatter
from abc import ABC, abstractmethod
import random


class Player(ABC):
    @abstractmethod
    def make_move(self):
        pass


class ComputerPlayer(Player):
    def __init__(self, symbol, game: TicTacToe):
        self.symbol = symbol
        self.game = game

    def make_move(self):
        return random.randint(0, 9) if self.game.board.count(0) == 9 else self.mini_max().get("index")

    def mini_max(self):
        ava_spaces = [index for index, x in enumerate(self.game.board) if x == 0]

        moves = []    # this will store what will each index result lead too ... i guess
        for x in ava_spaces:

            result = self.game.make_move(x)

            if result is not None:

                if result == self.symbol:
                    return {"score": 10}
                elif result == "XO".strip(self.symbol):
                    return {"score": -10}
                elif result == -1:
                    return {"score": 0}
                else:
                    continue

            self.game.board[x] = 0

            moves.append({"index": x, "score": self.mini_max().get("score")})

        output = {"index": 0, "score": 0}

        for move in moves:

            if (self.game.board.count("X") == self.game.board.count("O") and self.symbol == "X") or\
                    (self.game.board.count("X") > self.game.board.count("O") and self.symbol == "O"):

                if output["score"] < move["score"]:

                    output = move
            else:

                if output["score"] > move["score"]:

                    output = move

        return output



class HumanPlayer(Player):
    def make_move(self):
        return int(input("Enter your index: ")) - 1


class PlayerControl:
    def __init__(self, player_1: Player, player_2: Player, game: TicTacToe):
        self.player_1 = player_1
        self.player_2 = player_2
        self.game = game

    @staticmethod
    def terminate_state(output):
        if output in ["X", "O", -1]:

            if output == -1:
                print("Draw")
            else:
                print(f"{output} wins!")

            return 0
        elif output is not None:
            print(output)
            return
        else:
            return 1

    def correct_move(self, player: Player):
        while True:

            result = self.game.make_move(player.make_move())

            inspect_ = self.terminate_state(result)
            if inspect_ == 0:
                return 0
            elif inspect_ == 1:
                break
            else:
                continue

    def game_flow(self):
        while True:
            print(formatter(self.game.board, color=True))
            output = self.correct_move(self.player_1)
            if output == 0:
                break
            print(formatter(self.game.board, color=True))
            output = self.correct_move(self.player_2)
            if output == 0:
                break

if "__main__" == __name__:
    game = TicTacToe()
    game_play = PlayerControl(ComputerPlayer("X", game), HumanPlayer(), game)
    game_play.game_flow()