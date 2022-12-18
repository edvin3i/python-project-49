#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import game_progression


def main():
    engine.game_cycle(game_progression)


if __name__ == '__main__':
    main()
