from Board import Player
from Board import Board


class ConnectFourGame:

    board = Board()
    player_red = Player("red")
    player_yellow = Player("yellow")
    game_end = False
    player_red_turn = True

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
        if self.check_left_diagonal(player, row, column):
            return True
        if self.check_right_diagonal(player, row, column):
            return True
        if self.check_horizontal(player, row):
            return True
        if self.check_vertical(player, column):
            return True
        return False

    def check_vertical(self, player, column):
        """

        Args:
            player: player who input the most recent piece
            column: the column at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected vertically)

        """
        count_longest_chain = 0
        row = 0

        while self.board.board_dict.get((row, column)):
            if self.board.board_dict.get((row, column)) == player.colour:
                count_longest_chain += 1
            else:
                count_longest_chain = 0
            row += 1

        if count_longest_chain >= 4:
            return True
        return False

    def check_horizontal(self, player, row):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected horizontally)

        """

        count_longest_chain = 0
        column = 0

        while column <= game.board.BOARD_WIDTH:
            if self.board.board_dict.get((row, column)) == player.colour:
                count_longest_chain += 1
                if count_longest_chain >= 4:
                    return True
            else:
                count_longest_chain = 0
            column += 1

        return False

    def check_right_diagonal(self, player, row, column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected diagonally upwards to the right)

        """

        count_longest_chain = 0

        while row > 0 and column > 0:
            row -= 1
            column -= 1

        while column <= game.board.BOARD_WIDTH and row <= game.board.BOARD_HEIGHT:
            if self.board.board_dict.get((row, column)) == player.colour:
                count_longest_chain += 1
                if count_longest_chain == 4:
                    return True
            else:
                count_longest_chain = 0
            column += 1
            row += 1

        return False

    def check_left_diagonal(self, player, row, column):
        """

        Args:
            player:
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected diagonally upwards to the right)

        """
        count_longest_chain = 0

        while row > 0 and column < 6:
            row -= 1
            column += 1

        while column >= 0 and row >= 0:
            if self.board.board_dict.get((row, column)) == player.colour:
                count_longest_chain += 1
                if count_longest_chain >= 4:
                    return True
            else:
                count_longest_chain = 0
            column -= 1
            row += 1

        return False

    def start_game(self):
        while not game.game_end:
            game.board.display_board()
            print("Possible moves: " + str(game.board.valid_moves()))
            if game.player_red_turn:
                print("Red's turn.")
                input_column = int(input("Please input a number: "))
                if input_column not in game.board.valid_moves():
                    print("That is not a valid move. Please try again.")
                    continue
                input_row = game.board.input_piece(game.player_red, input_column)
                if game.check_won(game.player_red, input_row, input_column):
                    game.game_end = True
                    game.board.display_board()
                    print("Red won!")
                game.player_red_turn = False
            else:
                print("Yellow's turn.")
                input_column = int(input("Please input a number: "))
                if input_column not in game.board.valid_moves():
                    print("That is not a valid move. Please try again.")
                    continue
                input_row = game.board.input_piece(game.player_yellow, input_column)
                if game.check_won(game.player_red, input_row, input_column):
                    game.game_end = True
                    game.board.display_board()
                    print("Yellow won!")
                game.player_red_turn = True


if __name__ == '__main__':
    game = ConnectFourGame()
    game.start_game()
