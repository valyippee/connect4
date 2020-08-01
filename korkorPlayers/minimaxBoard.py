class MinimaxBoard:

    BOARD_HEIGHT = 6
    BOARD_WIDTH = 7
    _RIGHT_DIAGONAL_COORD = [(6, 3), (6, 4), (6, 5), (5, 5), (4, 5), (5, 2)]
    _LEFT_DIAGONAL_COORD = [(0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)]
    _COLUMN_COORD = [0, 1, 2, 3, 4, 5, 6]
    _ROW_COORD = [0, 1, 2, 3, 4, 5]

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

    def vertical_length_count(self, length, column, colour):
        count = 0
        column_lst = []
        for xy in self.board_dict.keys():
            if xy[0] == column:
                column_lst.append(xy)
        column_lst.sort()
        curr_length = 0
        for xy in column_lst:
            if self.board_dict[xy] == colour:
                curr_length += 1
            else:
                if curr_length == length:
                    count += 1
                curr_length = 0
        if curr_length == length:
            count += 1

        return count

    def horizontal_length_count(self, length, row, colour):
        count = 0
        row_lst = []
        for xy in self.board_dict.keys():
            if xy[1] == row:
                row_lst.append(xy)
        row_lst.sort()
        curr_length = 0
        for xy in row_lst:
            if self.board_dict[xy] == colour:
                curr_length += 1
            else:
                if curr_length == length:
                    count += 1
                curr_length = 0
        if curr_length == length:
            count += 1

        return count

    def left_diagonal_length_count(self, length, start_coord, colour):
        count = 0
        diagonal_lst = []
        max_length = min(start_coord[1], 6 - start_coord[0])
        for i in range(max_length + 1):
            diagonal_lst.append((start_coord[0] + i, start_coord[1] - i))
        curr_length = 0
        for xy in diagonal_lst:
            if xy in self.board_dict.keys():
                if self.board_dict[xy] == colour:
                    curr_length += 1
                else:
                    if curr_length == length:
                        count += 1
                    curr_length = 0
            else:
                if curr_length == length:
                    count += 1
                curr_length = 0
        if curr_length == length:
            count += 1

        return count

    def right_diagonal_length_count(self, length, start_coord, colour):
        count = 0
        diagonal_lst = []
        max_length = min(start_coord[1], start_coord[0])
        for i in range(max_length + 1):
            diagonal_lst.append((start_coord[0] - i, start_coord[1] - i))
        curr_length = 0
        for xy in diagonal_lst:
            if xy in self.board_dict.keys():
                if self.board_dict[xy] == colour:
                    curr_length += 1
                else:
                    if curr_length == length:
                        count += 1
                    curr_length = 0
            else:
                if curr_length == length:
                    count += 1
                curr_length = 0
        if curr_length == length:
            count += 1

        return count

    def vertical_threat_length_count(self, length, column, colour):
        count = 0
        column_lst = []
        for xy in self.board_dict.keys():
            if xy[0] == column:
                column_lst.append(xy)
        column_lst.sort()
        curr_length = 0
        for xy in column_lst:
            if self.board_dict[xy] == colour:
                curr_length += 1
            else:
                curr_length = 0
        if curr_length == length and len(column_lst) < (6 - length):
            count += 1

        return count

    def horizontal_threat_length_count(self, length, row, colour):
        count = 0
        row_lst = []
        for xy in self.board_dict.keys():
            if xy[1] == row:
                row_lst.append(xy)
        row_lst.sort()
        curr_length = 0
        for xy in row_lst:
            if self.board_dict[xy] == colour:
                curr_length += 1
            else:
                if curr_length == length:
                    count += 1
                curr_length = 0
        if curr_length == length:
            count += 1

        return count

    def check_win(self, colour):
        for column in self._COLUMN_COORD:
            if self.vertical_length_count(4, column, colour) > 0:
                return True
        for row in self._ROW_COORD:
            if self.horizontal_length_count(4, row, colour) > 0:
                return True
        for left_diag_start in self._LEFT_DIAGONAL_COORD:
            if self.left_diagonal_length_count(4, left_diag_start, colour) > 0:
                return True
        for right_diag_start in self._RIGHT_DIAGONAL_COORD:
            if self.right_diagonal_length_count(4, right_diag_start, colour) > 0:
                return True
        return False

    def game_over(self):
        for column in self._COLUMN_COORD:
            if self.vertical_length_count(4, column, "red") > 0:
                return True
        for row in self._ROW_COORD:
            if self.horizontal_length_count(4, row, "red") > 0:
                return True
        for left_diag_start in self._LEFT_DIAGONAL_COORD:
            if self.left_diagonal_length_count(4, left_diag_start, "red") > 0:
                return True
        for right_diag_start in self._RIGHT_DIAGONAL_COORD:
            if self.right_diagonal_length_count(4, right_diag_start, "red") > 0:
                return True
        for column in self._COLUMN_COORD:
            if self.vertical_length_count(4, column, "yellow") > 0:
                return True
        for row in self._ROW_COORD:
            if self.horizontal_length_count(4, row, "yellow") > 0:
                return True
        for left_diag_start in self._LEFT_DIAGONAL_COORD:
            if self.left_diagonal_length_count(4, left_diag_start, "yellow") > 0:
                return True
        for right_diag_start in self._RIGHT_DIAGONAL_COORD:
            if self.right_diagonal_length_count(4, right_diag_start, "yellow") > 0:
                return True
        return False

    def heuristic(self, colour):
        score = 0
        if self.check_win(colour):
            return 10000
        if colour == "yellow":
            if self.check_win("red"):
                return -10000
        else:
            if self.check_win("yellow"):
                return -10000
        for column in self._COLUMN_COORD:
            score += self.vertical_length_count(2, column, colour)
            score += 100 * self.vertical_length_count(3, column, colour)
            score += 10000 * self.vertical_length_count(4, column, colour)
        for row in self._ROW_COORD:
            score += self.horizontal_length_count(2, row, colour)
            score += 100 * self.horizontal_length_count(3, row, colour)
            score += 10000 * self.horizontal_length_count(4, row, colour)
        for left_diag_start in self._LEFT_DIAGONAL_COORD:
            score += self.left_diagonal_length_count(2, left_diag_start, colour)
            score += 100 * self.left_diagonal_length_count(3, left_diag_start, colour)
            score += 10000 * self.left_diagonal_length_count(4, left_diag_start, colour)
        for right_diag_start in self._RIGHT_DIAGONAL_COORD:
            score += self.right_diagonal_length_count(2, right_diag_start, colour)
            score += 100 * self.right_diagonal_length_count(3, right_diag_start, colour)
            score += 10000 * self.right_diagonal_length_count(4, right_diag_start, colour)

        return score

    def smart_heuristic(self, colour):
        score = 0
        opp_colour = ""
        if self.check_win(colour):
            return 10000
        if colour == "yellow":
            opp_colour = "red"
            if self.check_win("red"):
                return -10000
        else:
            opp_colour = "yellow"
            if self.check_win("yellow"):
                return -10000
        for column in self._COLUMN_COORD:
            score += self.vertical_length_count(2, column, colour)
            score += 100 * self.vertical_length_count(3, column, colour)
            score += 10000 * self.vertical_length_count(4, column, colour)
            score -= self.vertical_length_count(2, column, opp_colour)
            score -= 100 * self.vertical_length_count(3, column, opp_colour)
            score -= 10000 * self.vertical_length_count(4, column, opp_colour)
        for row in self._ROW_COORD:
            score += self.horizontal_length_count(2, row, colour)
            score += 100 * self.horizontal_length_count(3, row, colour)
            score += 10000 * self.horizontal_length_count(4, row, colour)
            score -= self.horizontal_length_count(2, row, opp_colour)
            score -= 100 * self.horizontal_length_count(3, row, opp_colour)
            score -= 10000 * self.horizontal_length_count(4, row, opp_colour)
        for left_diag_start in self._LEFT_DIAGONAL_COORD:
            score += self.left_diagonal_length_count(2, left_diag_start, colour)
            score += 100 * self.left_diagonal_length_count(3, left_diag_start, colour)
            score += 10000 * self.left_diagonal_length_count(4, left_diag_start, colour)
            score -= self.left_diagonal_length_count(2, left_diag_start, opp_colour)
            score -= 100 * self.left_diagonal_length_count(3, left_diag_start, opp_colour)
            score -= 10000 * self.left_diagonal_length_count(4, left_diag_start, opp_colour)
        for right_diag_start in self._RIGHT_DIAGONAL_COORD:
            score += self.right_diagonal_length_count(2, right_diag_start, colour)
            score += 100 * self.right_diagonal_length_count(3, right_diag_start, colour)
            score += 10000 * self.right_diagonal_length_count(4, right_diag_start, colour)
            score -= self.right_diagonal_length_count(2, right_diag_start, opp_colour)
            score -= 100 * self.right_diagonal_length_count(3, right_diag_start, opp_colour)
            score -= 10000 * self.right_diagonal_length_count(4, right_diag_start, opp_colour)

        return score

    def print_board(self):
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


    def display_board(self):
        """

        prints current game_setup state

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