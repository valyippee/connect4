from connect4.board import Player
from connect4.board import Board


class ConnectFourGame:

    board = Board()
    game_end = False
    player1_turn = True

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def check_won(self, player, row, column):
        """

        Args:
            player: player who input the most recent piece
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
            player: player who input the most recent piece
            row: the row at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected horizontally)

        """

        count_longest_chain = 0
        column = 0

        while column <= self.board.BOARD_WIDTH:
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
            player: player who input the most recent piece
            row: the row at which the most recent game piece is inserted
            column: the column at which the most recent game piece is inserted

        Returns: boolean of whether the player won (four pieces connected diagonally upwards to the right)

        """

        count_longest_chain = 0

        while row > 0 and column > 0:
            row -= 1
            column -= 1

        while column <= self.board.BOARD_WIDTH and row <= self.board.BOARD_HEIGHT:
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
            player: player who input the most recent piece
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

    def update(self, player, input_column):
        """

        updates board.board_dict by inputting the game piece according to the player's action

        """
        return self.board.input_piece(player, input_column)

# if __name__ == '__main__':
#     player1 = Player("red")
#     player2 = Player("yellow")
#     game = ConnectFourGame(player1, player2)
#     game.start_game()
