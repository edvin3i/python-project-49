#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import game_gcd


def main():
    engine.game_cycle(game_gcd)


if __name__ == '__main__':
    main()
