from Board import Player
from Board import Cell
from Board import Board


class ConnectFourGame:

    board = Board()
    player_x = Player(Cell.X)
    player_o = Player(Cell.O)
    game_end = False
    player_x_turn = True

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
        if len(self.check_horizontal(player, row, column, column)) >= 4:
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

    def start_game(self):
        while not game.game_end:
            game.board.display_board()
            print("Possible moves: " + str(game.board.valid_moves()))
            if game.player_x_turn:
                print("Player X's turn.")
                player_move = int(input("Please input a number: "))
                input_row = game.board.input_piece(game.player_x, player_move)
                if game.check_won(game.player_x, input_row, player_move):
                    game.game_end = True
                    print("Player X won")
                game.player_x_turn = False
            else:
                print("Player O's turn.")
                player_move = int(input("Please input a number: "))
                input_row = game.board.input_piece(game.player_o, player_move)
                if game.check_won(game.player_x, input_row, player_move):
                    game.game_end = True
                    print("Player O won")
                game.player_x_turn = True


if __name__ == '__main__':
    game = ConnectFourGame()
    game.start_game()
