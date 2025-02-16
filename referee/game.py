from referee.connectFourGame import ConnectFourGame

COLOURS = "red", "yellow"
NUM_PLAYERS = 2
GAME_NAME = "Connect Four"

def play(players):
    """
        Coordinate a game_setup, return a string describing the result.
    """
    game = Game()
    for player, colour in zip(players, COLOURS):
        player.init(colour)
    current_player, next_player = players
    while not game.connect_four_game.game_end:
        game.connect_four_game.board.display_board()
        print("Possible moves: " + str(game.connect_four_game.board.valid_moves()))
        print(current_player.colour + "'s turn")
        input_column = current_player.action()
        print("chosen column: " + str(input_column))
        if input_column not in game.connect_four_game.board.valid_moves():
            print("That is not a valid move. Please try again.")
            continue

        input_row = game.update(current_player.colour, input_column)

        for player in players:
            player.update(current_player.colour, input_column)

        if game.connect_four_game.check_won(current_player.colour, input_row, input_column):
            game.connect_four_game.board.display_board()
            if current_player.colour == "red":
                return "Red won!"
            return "Yellow won!"
        if game.connect_four_game.check_draw():
            return "Draw!"

        current_player, next_player = next_player, current_player


class Game:
    def __init__(self):
        self.connect_four_game = ConnectFourGame()

    def update(self, player, column):
        row = self.connect_four_game.board.input_piece(player, column)
        return row
