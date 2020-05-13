from connect4.board import Board
import random
import time


class PlayerTesting:
    def __init__(self, colour):
        self.colour = colour
        self.board = Board()

    def update(self, player, column):
        self.board.input_piece(player, column)

    def action(self):
        time.sleep(1)
        available_moves = self.board.valid_moves()
        chosen_move = random.choice(available_moves)
        return chosen_move
