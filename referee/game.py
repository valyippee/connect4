from connect4.connectFourGame import ConnectFourGame


def play(player1, player2):
    """
        Coordinate a game, return a string describing the result.
    """
    game = ConnectFourGame(player1, player2)
    current_player = player1
    next_player = player2
    players = current_player, next_player
    while not game.game_end:
        game.board.display_board()
        print("Possible moves: " + str(game.board.valid_moves()))
        print(current_player.colour + "'s turn")
        # input_column = int(current_player.action())
        # print("chosen column: " + input_column)
        input_column = int(input("player's action: "))
        if input_column not in game.board.valid_moves():
            print("That is not a valid move. Please try again.")
            continue

        input_row = game.update(current_player, input_column)

        # for player in players:
        #     player.update(current_player, input_column)

        if game.check_won(current_player, input_row, input_column):
            game.game_end = True
            game.board.display_board()
        current_player, next_player = next_player, current_player

    if current_player == player1:
        return "Yellow won!"
    return "Red won!"
