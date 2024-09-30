"""Запуск игры."""

from src.game.game import Game
from src.game.logging import HELogger
import logging


def main() -> None:
    logger = HELogger("HouseEscape", logging.DEBUG)
    Game(logger.getChild("Logger"))


if __name__ == "__main__":
    main()
