from board import Board
from game import COLOURS
import random

class Player:
    def __init__(self, colour):
        self.colour = colour
        if colour == COLOURS[0]:
            self.opponent_colour = COLOURS[1]
        else:
            self.opponent_colour = COLOURS[0]
        self.board = Board()
        self.scores = {self.colour: 1, self.opponent_colour: -1, 'tie': 0}

    def update(self, player_colour, column):
        return self.board.input_piece(player_colour, column)

    def action(self):
        recursion_depth = 8
        available_moves = self.board.valid_moves()
        chosen_move = available_moves[0]
        best_score = float('-inf')
        for i in range(len(available_moves)):
            row = self.update(self.colour, available_moves[i])
            # self.board.display_board()
            # score = self.minimax(False, recursion_depth - 1)
            score = self.minimax(False, recursion_depth - 1, float('-inf'), float('inf'))
            del self.board.board_dict[(row, available_moves[i])]
            if score > best_score:
                best_score = score
                chosen_move = available_moves[i]
        return chosen_move

    def minimax(self, is_max, depth, alpha, beta):
        # recursion depth hit or game ended, return static evaluation of the game state
        if depth == 0 or self.check_game_end():
            return random.randint(0, 50)

        available_moves = self.board.valid_moves()
        if is_max:
            best_score = float('-inf')
            for move in available_moves:
                row = self.update(self.colour, move)
                # self.board.display_board()
                # score = self.minimax(False, depth - 1)
                score = self.minimax(False, depth - 1, alpha, beta)
                # print("score: " + str(score))
                if score > best_score:
                    best_score = score
                del self.board.board_dict[(row, move)]
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
        else:
            best_score = float('inf')
            for move in available_moves:
                row = self.update(self.opponent_colour, move)
                # self.board.display_board()
                # score = self.minimax(True, depth - 1)
                score = self.minimax(True, depth - 1, alpha, beta)
                # print("score: " + str(score))
                if score < best_score:
                    best_score = score
                del self.board.board_dict[(row, move)]
                beta = min(beta, score)
                if alpha >= beta:
                    break

        return best_score

    def check_game_end(self):
        if len(self.board.board_dict) == self.board.BOARD_HEIGHT * self.board.BOARD_WIDTH:
            return True
        return False

    def check_won(self):
        # check rows
        for column in range(self.board.BOARD_WIDTH):
            opponent_chain = 0
            my_chain = 0
            for row in range(self.board.BOARD_HEIGHT):
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
            # print("my chain: " + str(my_chain))
            # print("opponent chain" + str(opponent_chain))
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour

        # check columns
        for row in range(self.board.BOARD_HEIGHT):
            opponent_chain = 0
            my_chain = 0
            for column in range(self.board.BOARD_HEIGHT):
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour

        # check increasing diagonals (6 possible starting points)
        for row in range(0, 3):
            column = 0
            my_chain = 0
            opponent_chain = 0
            while column <= self.board.BOARD_WIDTH and row <= self.board.BOARD_HEIGHT:
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
                column += 1
                row += 1
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour
        for column in range(1, 4):
            row = 0
            my_chain = 0
            opponent_chain = 0
            while column <= self.board.BOARD_WIDTH and row <= self.board.BOARD_HEIGHT:
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
                column += 1
                row += 1
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour

        # check increasing diagonals (6 possible starting points)
        for row in range(0, 3):
            column = 0
            my_chain = 0
            opponent_chain = 0
            while column >= 0 and row <= self.board.BOARD_HEIGHT:
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
                column -= 1
                row += 1
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour
        for column in range(3, 6):
            row = 0
            my_chain = 0
            opponent_chain = 0
            while column >= 0 and row <= self.board.BOARD_HEIGHT:
                my_chain, opponent_chain = self.check_consecutive(my_chain, opponent_chain, row, column)
                column += 1
                row += 1
            if opponent_chain >= 4:
                return self.opponent_colour
            elif my_chain >= 4:
                return self.colour
        return "tie"

    def check_consecutive(self, my_chain, opponent_chain, row, column):
        if self.board.board_dict.get((row, column)) == self.colour:
            my_chain += 1
            opponent_chain = 0
        elif self.board.board_dict.get((row, column)) == self.opponent_colour:
            opponent_chain += 1
            my_chain = 0
        else:
            my_chain = 0
            opponent_chain = 0
        return my_chain, opponent_chain





