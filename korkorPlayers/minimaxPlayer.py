from korkorPlayers.minimaxBoard import MinimaxBoard
import random
import math
import copy


class Player:
    def __init__(self, colour):
        self.colour = colour
        if colour == "red":
            self.opp_colour = "yellow"
        else:
            self.opp_colour = "red"
        self.board = MinimaxBoard()

    def update(self, player, column):
        self.board.input_piece(player, column)

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or board.game_over():
            score = board.heuristic(self.colour)
            return score

        if maximizingPlayer:
            max_eval = -math.inf
            for action in board.valid_moves():
                resulting_board = copy.deepcopy(board)
                resulting_board.input_piece(self.colour, action)
                eval = self.minimax(resulting_board, depth - 1, alpha, beta, False)
                max_eval = max(eval, max_eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval

        else:
            min_eval = math.inf
            for action in board.valid_moves():
                resulting_board = copy.deepcopy(board)
                resulting_board.input_piece(self.opp_colour, action)
                eval = self.minimax(resulting_board, depth - 1, alpha, beta, True)
                min_eval = min(eval, min_eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def action(self):
        available_moves = self.board.valid_moves()
        action_score = []
        alpha = -math.inf
        # alpha = (-math.inf, -math.inf)
        beta = math.inf
        # beta = (math.inf, math.inf)
        for action in available_moves:
            resulting_board = copy.deepcopy(self.board)
            resulting_board.input_piece(self.colour, action)
            score = self.minimax(resulting_board, 5, alpha, beta, False)
            action_score.append((score, action))
        sorted_action_score = sorted(action_score, reverse=True)

        best_action = sorted_action_score[0]
        best_action_list = []
        for i in action_score:
            if i[0] == best_action[0]:
                best_action_list.append(i)
        print(best_action_list)
        chosen_move = random.choice(best_action_list)

        return chosen_move[1]
