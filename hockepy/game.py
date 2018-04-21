# vim: set fileencoding=utf-8 :

#  ____  ____    ____      ______  ___  ____   _________  ______    ____  ____
# |_   ||   _| .'    `.  .' ___  ||_  ||_  _| |_   ___  ||_   __ \ |_  _||_  _|
#   | |__| |  /  .--.  \/ .'   \_|  | |_/ /     | |_  \_|  | |__) |  \ \  / /
#   |  __  |  | |    | || |         |  __'.     |  _|  _   |  ___/    \ \/ /
#  _| |  | |_ \  `--'  /\ `.___.'\ _| |  \ \_  _| |___/ | _| |_       _|  |_
# |____||____| `.____.'  `._____.'|____||____||_________||_____|     |______|
#

"""
hockepy.game
------------

This module implements a league-agnostic Game representation.

These interfaces are implemented:
- Game named tuple
- GameStatus enum
- GameType enum
- has_started() - indicates whether the game has already started
"""

from collections import namedtuple
from enum import Enum, unique

Game = namedtuple(
    'Game',
    ['home',        # home team's name
     'away',        # away team's name
     'home_score',  # home team's score
     'away_score',  # away team's score
     'time',        # UTC time and date (datetime object)
     'type',        # GameType instance
     'status'       # GameStatus instance
     ])


def has_started(game):
    return (game.status.value > 1)


@unique
class GameStatus(Enum):
    SCHEDULED = 1
    LIVE = 2
    FINAL = 3


@unique
class GameType(Enum):
    PRESEASON = 1
    REGULAR = 2
    PLAYOFFS = 3