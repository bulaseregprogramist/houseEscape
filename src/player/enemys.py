"""Враги в игре"""

from .character import Character
from ..game.logging import HELogger


class Enemy(Character):
    __x: int
    __y: int
    __enemy_type: str
    field_of_view = 30  # FOV
    
    def __init__(self, x: int, y: int, enemy_type: str) -> None:
        self.__x = x
        self.__y = y
        self.__enemy_type = enemy_type  # В enemy_type может быть watcher, blinder, stalker
        
    @classmethod
    def change_fields(cls, logger: HELogger, speed: int, fov: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            logger (HELogger): Переменная для логов,
            speed (int): Изменение статичного поля speed
        """
        logger.debug("Идёт смена полей класса...")
        super().change_fields(speed)
        cls.field_of_view = fov
        logger.debug("Поля класса изменены!")
        
    def get_stats(self) -> None:
        """Получение информации о враге"""
        pass
    
    def die(self) -> None:
        """Смерть врага"""
        pass
    
    def enemy_move(self) -> None:
        """Движение NPC (AI)"""
        pass
    