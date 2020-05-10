from connect4.Board import Player
from connect4.Board import Cell
from connect4.Board import Board


class ConnectFourGame:

    board = Board()
    player_x = Player(Cell.X)
    player_o = Player(Cell.O)

    def __init__(self):
        pass

    # @property
    # def board(self):
    #     return Board()
    #
    # @property
    # def player_x(self):
    #     return Player(Cell.X)
    #
    # @property
    # def player_o(self):
    #     return Player(Cell.O)

    def check_won(self, player, row, column):
        """

        Args:
            row: the row at which the most recent game piece is inserted
            column: the column at which the piece is inserted

        Returns:

        """
        pass

    def check_vertical(self, player, row, column):
        possible_victory = []
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            possible_connected_piece = self.check_vertical(player, row + 1, column)
            possible_victory.extend(possible_connected_piece)

        return possible_victory

    def check_horizontal(self, player, row, column, starting_column):
        possible_victory = []
        print("row: " + str(row) + ", column: " + str(column))
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            print("inside if statement: ")
            print(possible_victory)
            if column < starting_column:
                possible_connected_piece_left = self.check_horizontal(player, row, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)
                return possible_victory
            possible_connected_piece_right = self.check_horizontal(player, row, column + 1, starting_column)
            possible_victory.extend(possible_connected_piece_right)
            if column <= starting_column:
                possible_connected_piece_left = self.check_horizontal(player, row, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)

        print(possible_victory)
        return possible_victory

    # def start_game(self):



if __name__ == '__main__':
    game = ConnectFourGame()
    game.board.display_board()
    print("\n")
    game.board.input_piece(game.player_x, 2)
    game.board.input_piece(game.player_x, 2)
    game.board.input_piece(game.player_x, 2)
    game.board.input_piece(game.player_x, 2)
    game.board.display_board()
    possible_victory = game.check_vertical(game.player_x, 3, 2)
    if len(possible_victory) >= 4:
        print("x won")
