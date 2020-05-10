from connect4.Board import Player
from connect4.Board import Cell
from connect4.Board import Board


class ConnectFourGame:

    board = Board()
    player_x = Player(Cell.X)
    player_o = Player(Cell.O)

    def __init__(self):
        pass

    def check_won(self, player, row, column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted

        Returns: boolean of whether the player won

        """
        if len(self.check_diagonal_decreasing(player, row, column, column)) >= 4:
            return True
        if len(self.check_diagonal_increasing(player, row, column, column)) >= 4:
            return True
        if len(self.check_horizontal(player, row, column)) >= 4:
            return True
        if len(self.check_vertical(player, row, column)) >= 4:
            return True
        return False

    def check_vertical(self, player, row, column):
        """

        Args:
            player: player who input the most recent piece
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted

        Returns: a list of the longest vertical chain formed with the most recent game piece

        """
        possible_victory = []
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            possible_connected_piece = self.check_vertical(player, row + 1, column)
            possible_victory.extend(possible_connected_piece)

        return possible_victory

    def check_horizontal(self, player, row, column, starting_column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted
            starting_column: the column at which the most recent game piece is inserted

        Returns: a list of the longest horizontal chain formed with the most recent game piece

        """
        possible_victory = []
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            if column < starting_column:
                possible_connected_piece_left = self.check_horizontal(player, row, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)
                return possible_victory
            possible_connected_piece_right = self.check_horizontal(player, row, column + 1, starting_column)
            possible_victory.extend(possible_connected_piece_right)
            if column <= starting_column:
                possible_connected_piece_left = self.check_horizontal(player, row, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)

        return possible_victory

    def check_diagonal_increasing(self, player, row, column, starting_column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted
            starting_column: the column at which the most recent game piece is inserted

        Returns: a list of the longest diagonal (increasing) chain formed with the most recent game piece

        """
        possible_victory = []
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            if column < starting_column:
                possible_connected_piece_left = self.check_diagonal_increasing(player, row + 1, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)
                return possible_victory
            possible_connected_piece_right = self.check_diagonal_increasing(player, row - 1, column + 1, starting_column)
            possible_victory.extend(possible_connected_piece_right)
            if column <= starting_column:
                possible_connected_piece_left = self.check_diagonal_increasing(player, row + 1, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)

        return possible_victory

    def check_diagonal_decreasing(self, player, row, column, starting_column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted
            starting_column: the column at which the most recent game piece is inserted

        Returns: a list of the longest diagonal (decreasing) chain formed with the most recent game piece

        """
        possible_victory = []
        if self.board.boardcells.get((row, column)) == player.sign:
            possible_victory.append((row, column))
            if column < starting_column:
                possible_connected_piece_left = self.check_diagonal_decreasing(player, row - 1, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)
                return possible_victory
            possible_connected_piece_right = self.check_diagonal_decreasing(player, row + 1, column + 1, starting_column)
            possible_victory.extend(possible_connected_piece_right)
            if column <= starting_column:
                possible_connected_piece_left = self.check_diagonal_decreasing(player, row - 1, column - 1, starting_column)
                possible_victory.extend(possible_connected_piece_left)

        return possible_victory


    # def start_game(self):



if __name__ == '__main__':
    game = ConnectFourGame()
    game.board.display_board()
    print("\n")
    game.board.input_piece(game.player_x, 2)
    game.board.input_piece(game.player_o, 3)
    game.board.input_piece(game.player_x, 3)
    game.board.input_piece(game.player_o, 4)
    game.board.input_piece(game.player_o, 4)
    game.board.input_piece(game.player_x, 4)
    game.board.input_piece(game.player_o, 5)
    game.board.input_piece(game.player_o, 5)
    game.board.input_piece(game.player_o, 5)
    game.board.input_piece(game.player_x, 5)
    game.board.input_piece(game.player_o, 6)
    game.board.input_piece(game.player_o, 6)
    game.board.input_piece(game.player_x, 6)
    game.board.input_piece(game.player_o, 7)
    game.board.input_piece(game.player_x, 7)
    game.board.input_piece(game.player_x, 4)
    game.board.input_piece(game.player_x, 4)
    game.board.display_board()
