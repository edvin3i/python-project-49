#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import game_even


def main():
    engine.game_cycle(game_even)


if __name__ == '__main__':
    main()
