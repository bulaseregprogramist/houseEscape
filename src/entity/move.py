"""Движение игрока"""

# Есть места в комнате, в которых не должен быть игрок
# Но они видимы. 
# Например: кровать в спальне.

from ..game.logging import HELogger
import pygame
from keyboard import is_pressed


pygame.init()


class Move:
    """Движение игрока"""
    
    @staticmethod
    def player_move(player: object, index: list[int, int], x: int, y: int,
                    speed: int) -> None:
        """
        Движение игрока
        
        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Карта дома,
            x (int): Позиция игрока по x
            y (int): Позиция игрока по y
            speed (int): Скорость игрока
        Returns:
            int: Позиция игрока по x и y.
        """
        if (is_pressed("w") and Move.move_in_location(player.x, 
                player.y, index) and y < 753):
            y -= 3 * speed
        elif (is_pressed("a") and Move.move_in_location(player.x,
                player.y, index) and x > -23):
            x -= 3 * speed
        elif (is_pressed("s") and Move.move_in_location(player.x,
                player.y, index) and y > -23):
            y += 3 * speed
        elif (is_pressed("d") and Move.move_in_location(player.x, 
                player.y, index) and x < 753):
            x += 3  * speed
        return x, y
    
    @staticmethod
    def press_keydown(logger: HELogger, event, cls, index: list[int, int],
                player: object, n: int, mouse_pos: tuple[int, int]) -> None:
        """
        Нажатие на клавишу
        
        Args:
            logger (HELogger): Переменная для логов,
            event (Any): Событие в pygame,
            cls (Inventory): Класс инвентаря,
            index (list[int, int]): Позиция игрока на карте дома,
            player (Player): Класс Player,
            n (int): Номер выбранного сохранения,
            mouse_pos (tuple[int, int]): Позиция мыши.
        """
        try:
            logger.info(f"Нажата клавиша - {chr(event.key)}")
        except ValueError:
            logger.error(
                "Нажата клавиша, которая не может быть обработана через chr")
        if event.key == pygame.K_e:
            cls.to_inventory(logger, index, player, n, mouse_pos)
    
    @staticmethod
    def move_in_location(x: int, y: int, index: list[int, int]) -> bool:
        """
        Даёт доступ только в определённые места

        Args:
            x (int): Позиция игрока по x,
            y (int): Позиция игрока по y,
            index (list[int, int]): Карта дома.
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
            if y > 120:
                return True
        return False
    