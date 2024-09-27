"""Запуск игры."""

from src.game import Game
from src.logging import HELogger
import logging


def main() -> None:
    logger = HELogger("HouseEscape", logging.INFO)
    Game(logger.getChild("Logger"))


if __name__ == "__main__":
    main()
