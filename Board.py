import enum


class Cell(enum.Enum):
    empty = "   "
    X = " X "
    O = " O "


class Player:
    def __init__(self, sign):
        self.sign = sign


class Board:
    def __init__(self):
        self.row = 7
        self.column = 6
        self.boardcells = {(1, 1): Cell.empty, (1, 2): Cell.empty, (1, 3): Cell.empty, (1, 4): Cell.empty,
                           (1, 5): Cell.empty, (1, 6): Cell.empty, (1, 7): Cell.empty,
                           (2, 1): Cell.empty, (2, 2): Cell.empty, (2, 3): Cell.empty, (2, 4): Cell.empty,
                           (2, 5): Cell.empty, (2, 6): Cell.empty, (2, 7): Cell.empty,
                           (3, 1): Cell.empty, (3, 2): Cell.empty, (3, 3): Cell.empty, (3, 4): Cell.empty,
                           (3, 5): Cell.empty, (3, 6): Cell.empty, (3, 7): Cell.empty,
                           (4, 1): Cell.empty, (4, 2): Cell.empty, (4, 3): Cell.empty, (4, 4): Cell.empty,
                           (4, 5): Cell.empty, (4, 6): Cell.empty, (4, 7): Cell.empty,
                           (5, 1): Cell.empty, (5, 2): Cell.empty, (5, 3): Cell.empty, (5, 4): Cell.empty,
                           (5, 5): Cell.empty, (5, 6): Cell.empty, (5, 7): Cell.empty,
                           (6, 1): Cell.empty, (6, 2): Cell.empty, (6, 3): Cell.empty, (6, 4): Cell.empty,
                           (6, 5): Cell.empty, (6, 6): Cell.empty, (6, 7): Cell.empty}

    def input_piece(self, player, column):
        """

        Args:
            player: Player instance
            column: the column at which the game piece is dropped

        Returns: (updates self.boardcells with the player's sign) and returns the row at which the piece is
                    added to

        """
        cell_keys = self.boardcells.keys()
        possible_rows = []
        for cell in cell_keys:
            if cell[1] == column:
                if self.boardcells.get(cell) == Cell.empty:
                    possible_rows.append(cell[0])
        row = max(possible_rows)
        self.boardcells[(row, column)] = player.sign
        return row

    def valid_moves(self):
        """

        Returns: list of valid moves of the columns that are not filled completely

        """
        valid_moves_lst = []
        cell_keys = self.boardcells.keys()
        for cell in cell_keys:
            if cell[0] == 1:
                if self.boardcells.get(cell) == Cell.empty:
                    valid_moves_lst.append(cell[1])
        return valid_moves_lst

    def display_board(self):
        """
        prints current game state
        """
        game_state = []
        for i in range(1, 7):
            inner_list = ["|"]
            for j in range(1, 8):
                cell_state = self.boardcells.get((i, j))
                inner_list.append(cell_state.value)
                inner_list.append("|")
            game_state.append(''.join(inner_list))

        for lst in game_state:
            print(lst)


