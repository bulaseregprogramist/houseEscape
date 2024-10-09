"""Движение игрока"""

# Есть места в комнате, в которых не должен быть игрок
# Но они видимы. 
# Например: кровать в спальне.

from ..game.logging import HELogger
import pygame


pygame.init()


class Move:
    """Движение игрока"""
    
    @staticmethod
    def press_keydown(logger: HELogger, event, cls, index, player, n) -> None:
        """Нажатие на клавишу"""
        try:
            logger.info(f"Нажата клавиша - {chr(event.key)}")
        except ValueError:
            logger.error(
                "Нажата клавиша, которая не может быть обработана через chr")
        if event.key == pygame.K_e:
            cls.to_inventory(logger, index, player, n)
    
    @staticmethod
    def move_in_location(x: int, y: int, index: list[int, int]) -> bool:
        """
        Даёт доступ только в определённые места

        Args:
            x (int): позиция игрока по x,
            y (int): позиция игрока по y,
            index (list[int, int]): карта дома

        Returns:
            bool: Можно ли идти в этой зоне дома (True или False)
        """
        if index == [3, 3]:
            return True
        elif index == [3, 2]:
            return True
        elif index == [3, 1]:
            return True
        elif index == [2, 3]:
            return True
        elif index == [2, 2]:
            return True
        elif index == [2, 1]:
            return True
        elif index == [1, 3]:
            return True
        elif index == [1, 2]:
            return True
        elif index == [1, 1]:
            return True
        elif index == [0, 2]:
            return True
        return False
    