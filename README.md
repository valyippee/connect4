# connect4

A connect 4 game with game rules explained in details here: https://www.ludoteka.com/clasika/connect-4.html 

## How to run the game

**Download Connect4**

Clone this project to create a local copy on your computer.

**Run the game**

Navigate to the directory of this project on your terminal. 
Run `__main__.py <player_type> <player_type>` to start the game.
`<player_type>` allows you choose a type of player to play with.
Note that you have to enter the path to the player python file. There are three
types of players that you can choose from.
Input `players/humanPlayer.py` to select a human player which 
enables you to choose the moves, `players/randomPlayer.py` to select 
a random player who choose moves randomly, and `players/valeriePlayer.py`, `players/korkorPlayers/minimaxPlayer.py`, or `players/korkorPlayers/smartMinimaxPlayer.py`
to select an AI bot that uses minimax algorithm to choose the moves. 

Note that the order at which you input `<player_type>` determines the order
at which the players will play by.

You can also run `__main__.py -h` for help.

**How to select moves during the game 
(if you are using `humanPlayer.py` as a player)**

The board has coordinates 0 to 6 (x-axis). Choose one to select the column.
