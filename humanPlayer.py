from board import Board


class Player:
    def __init__(self, colour):
        self.colour = colour
        self.board = Board()

    def update(self, player, column):
        self.board.input_piece(player, column)

    def action(self):
        available_moves = self.board.valid_moves()
        chosen_move = int(input("Please enter move: "))
        return chosen_move
