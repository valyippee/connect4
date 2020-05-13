class Board:

    BOARD_HEIGHT = 6
    BOARD_WIDTH = 7

    def __init__(self):
        self.board_dict = dict()

    def input_piece(self, player, column):
        """

        Args:
            player: Player instance
            column: the column at which the game piece is dropped

        Returns: (updates self.boardcells with the player's sign) and returns the row at which the piece is
                    added to

        """
        game_pieces = self.board_dict.keys()
        possible_rows = [0, 1, 2, 3, 4, 5]
        for game_piece in game_pieces:
            if game_piece[1] == column:
                possible_rows.remove(game_piece[0])
        row = min(possible_rows)
        self.board_dict[(row, column)] = player.colour
        return row

    def valid_moves(self):
        """

        Returns: list of valid moves of the columns that are not filled completely

        """
        valid_moves_lst = [0, 1, 2, 3, 4, 5, 6]
        game_pieces = self.board_dict.keys()
        for game_piece in game_pieces:
            if game_piece[0] == 5:
                valid_moves_lst.remove(game_piece[1])
        return valid_moves_lst

    def display_board(self):
        """

        prints current game state

        """
        for i in range(self.BOARD_HEIGHT):
            i = self.BOARD_HEIGHT - i - 1
            print(str(i) + " |", end="")
            for j in range(self.BOARD_WIDTH):
                game_piece = self.board_dict.get((i, j))
                if game_piece is None:
                    print("\033[4m   \033[0m", end="")
                elif game_piece == "yellow":
                    print("\033[4m\033[93m O \033[0m", end="")
                elif game_piece == "red":
                    print("\033[4m\033[91m X \033[0m", end="")
                if j != self.BOARD_WIDTH - 1:
                    print("|", end="")
                else:
                    print("|")
        print("    0   1   2   3   4   5   6  ")
