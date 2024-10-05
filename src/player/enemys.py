"""Враги в игре"""

from .character import Character
from ..game.logging import HELogger
import pygame


pygame.init()


class Enemy(Character):
    __x: int
    __y: int
    __enemy_type: str
    enemy_dict = {
        1: [450, 150, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [20, 320, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
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
            speed (int): Изменение статичного поля speed,
            fov (int): Поле зрения врага.
        """
        logger.debug("Идёт смена полей класса...")
        super().change_fields(speed)
        cls.field_of_view = fov
        logger.debug("Поля класса изменены!")
        
    def get_stats(self, logger: HELogger) -> None:
        """
        Получение информации о враге
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        logger.info("Получение информации об враге")
        result: dict = Character.filter_data()
        super().get_stats(self.__screen, [self.x, self.y], result)
        logger.info("Информация о враге получена!")
    
    @staticmethod
    def die() -> None:
        """Смерть врага"""
        super().die()
    
    def enemy_move(self) -> None:
        """Движение NPC (AI)"""
        pass
    