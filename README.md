# General Info:

This semester, the Computer Science Club is holding an AI poker tournament. Submitted bots will play Texas Hold'em in tables of up to six bots. As players are knocked out of the tournament, the tables will be consolidated until there is one player left standing.s Blind levels, the number of tables, and the starting stacks will be decided after we have a better idea of how many bots are going to be submitted.

The tournament is open to all members of the Hendrix Community, and we encourage people of all skill levels to play. All you need is a basic grasp of Python (or a teammate with a basic grasp of Python).

Submissions will be allowed until 11:59pm October 14th, through [this form](https://forms.office.com/Pages/ResponsePage.aspx?id=jMH2DNLQP0qD0GY9Ygpj0xyfNGkHdu5JkmagYtTIratUOVNOUFBHNkMzSVNSRjBTWlhWVjdVOUVXMy4u).

The Computer Science Club will be hosting two nights before the tournament where we will be available to answer questions and help with any problems you are having. The dates and times are still tbd.

The tournament will be held on October 16th. We plan to play the tournament live with a visualization. We are still working on getting a time and location.

# Rules:

- Teams are allowed.
- You are allowed to use code from online sources, as long as it is properly cited. If it is licensed, include a copy of the license notice in a comment in your file.
- Each player or team may submit up to three bots.
- Bots may not attempt to access resources outside of the game environment, such as webservers.
- Each bot must consist of a single Python file.
- The following Python libraries will be included. If you want a different library for your bot, please contact us **before** the tournament date.
  - numpy
  - scikit
  - pokerkit
  - tensorflow
  - all of Pythons standard libraries and any libraries required by any of the above
- Bots must be submitted by 11:59pm October 14th.

# Library Usage and Bot Specifications

The pokerkit library is the only Python library that is required to design a bot. The others listed above are all optional. pokerkit, however is required for the framework to emulate poker games. I installed it using [pip, Python's built in package manager, and a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) but you could also use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html). If you have any questions come to one of our Q&A nights or shoot one of us an email. See below for our contact info.

The bots for this tournament are to be written in Python. There is a file called `playertemplate.py` in the `unused_players` folder that lays out a template for how to design a bot. Each bot implements a `Player` class with two functions: `make_move()` and `update(message)`. It is important that you do not change the names of the `Player` class and the two functions, or your bot will not run.

The `make_move()` function is the core of your bot. Every time that it is your turn, this function will be called. You will need to implement the function so that it returns a valid move. You are allowed to write any helper functions that you need for your strategy.

The `update(message)` is responsible for updating your bot whenever something happens in the game. Anytime something happens in the game, each players `update` function will be called with a message describing what happened. The messages take the form of a tuple, with the first item being a short string indicating what happened, and the rest of the items being and additional information that is necessary. See the `protocol.txt` file for a detailed description of all of the possible messages. This function is not required to be implemented for your bot to function, but can be useful if you need to know anything about the game state.

Moves take the form of an enum called `Move`. It is defined in `move.py` and can be imported with `from move import Move`. Enums in Python work similarly to the way they work in Java: a particular member may be referenced with `Move.MEMBER`. So, to return a fold, you would say `return Move.FOLD`.

Cards are represented by a class called `Card`. It has two attributes: the rank and the suit. The rank is an integer from 2 to 14, with 11 through 14 being the face cards Jack through Ace. The suit is an enum called `Suit`. See `suit.py` for the names of the suits.

Several simple bots are provided for testing purposes. A bot called `userplayer.py` takes user input from to command line to allow a human user to play in order to test the bots. Several bots called `randomplayer.py` make random moves. These can be used to fill out a table for testing purposes.

To use the framework, just place the bots that you want to play in the folder called `players` and make sure there are no other files in the folder (besides a `__pycache__` folder, if there is one). Then run `poker_kit_game.py`. Currently, this will only print the name of the player that won the game, but you can add print statements where you need to see debugging information. The blind structure and starting stacks can also be edited in this file.

Each time `make_move()` or `update(message)` is called, a timer will be started for thirty seconds. If the timer is exceeded, the function will be stopped, and play will continue with the player being considered to have made an invalid move. This functionality is platform dependent and so will not be included in the version of the code provided to the players.

If a player returns an invalid move, the framework will either make them fold or check, depending on whether it is possible to fold at that time.

# Contact Us

### Ted Bjurlin

Wrote the framework to run the tournament.

Email: [bjurlintw@hendrix.edu](bjurlintw@hendrix.edu)

### Sarah Wright

Organized the tournament.

Email: [wrightse@hendrix.edu](wrightse@hendrix.edu)