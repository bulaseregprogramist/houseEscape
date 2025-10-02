"""Запуск игры."""

from src.game.game import Game
from src.game.logging import HELogger


def main() -> None:
    """Этот метод запускает игру."""
    logger =  HELogger()
    Game(logger.change_name(logger))


if __name__ == "__main__":
    main()
