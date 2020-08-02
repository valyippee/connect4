class Board:
    BOARD_HEIGHT = 6
    BOARD_WIDTH = 7

    def __init__(self):
        self.board_dict = dict()

    def input_piece(self, player_colour, column):
        """

        Args:
            player_colour: player colour
            column: the column at which the game_setup piece is dropped

        Returns: (updates self.boardcells with the player's sign) and returns the row at which the piece is
                    added to

        """
        game_pieces = self.board_dict.keys()
        possible_rows = [0, 1, 2, 3, 4, 5]
        for game_piece in game_pieces:
            if game_piece[0] == column:
                possible_rows.remove(game_piece[1])
        row = min(possible_rows)
        self.board_dict[(column, row)] = player_colour
        return row

    def valid_moves(self):
        """

        Returns: list of valid moves of the columns that are not filled completely

        """
        valid_moves_lst = [0, 1, 2, 3, 4, 5, 6]
        game_pieces = self.board_dict.keys()
        for game_piece in game_pieces:
            if game_piece[1] == 5:
                valid_moves_lst.remove(game_piece[0])
        return valid_moves_lst

    def vertical_two_count(self, column):
        return

    def display_board(self):
        template = """ {}
            #    +---+---+---+---+---+---+---+
            #  5 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            #  4 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            #  3 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            #  2 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            #  1 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            #  0 |{:}|{:}|{:}|{:}|{:}|{:}|{:}|
            #    +---+---+---+---+---+---+---+
            # y/x  0   1   2   3   4   5   6  """
        coords = [(x, 5 - y) for y in range(6) for x in range(7)]
        cells = []
        for xy in coords:
            if xy not in self.board_dict:
                cells.append("   ")
            else:
                if self.board_dict[xy] == "red":
                    cells.append("\033[4m\033[91m X \033[0m")
                if self.board_dict[xy] == "yellow":
                    cells.append("\033[4m\033[93m O \033[0m")
        print(template.format("", *cells))

