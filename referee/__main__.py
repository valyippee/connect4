from game import play
from player import PlayerWrapper


def main():
    # import player classes and create new players

    p1 = PlayerWrapper("red", "playerTesting", "PlayerTesting")
    p2 = PlayerWrapper("yellow", "playerTesting", "PlayerTesting")

    # start game
    result = play([p1, p2])
    print(result)


if __name__ == '__main__':
    main()



