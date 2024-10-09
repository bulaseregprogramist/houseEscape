"""Враги в игре"""

from ..entity.character import Character
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
        # В enemy_type может быть watcher, blinder, stalker
        self.__enemy_type = enemy_type
        
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
    def die(logger: HELogger) -> None:
        """
        Смерть врага
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        super().die()
        logger.info("Враг побеждён!")
    
    def enemy_move(self, enemy_type: str) -> None:
        """
        Движение NPC (AI)
        
        Args:
            enemy_type (str): Тип монстра (бывает watcher, blinder, stalker).
        """
        if enemy_type == "watcher":
            pass
        elif enemy_type == "blinder":
            pass
        elif enemy_type == "stalker":
            pass
    