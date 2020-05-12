from connect4.board import Player
from game import play


def main():
    # import player classes and create new players

    p1 = Player("red")
    p2 = Player("yellow")

    # start game
    result = play(p1, p2)
    print(result)


if __name__ == '__main__':
    main()




