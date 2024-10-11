"""Враги в игре"""

from ..entity.character import Character
from ..game.logging import HELogger
from ..game.saving import Saving
from ..other.globals import n, load
import pygame
import re


pygame.init()


class Enemy(Character):
    """Враги игрока"""
    save = Saving()
    enemy_dict = save.load_save(n)["enemys"]
    field_of_view = save.load_save(n)["FOV"]  # FOV
    
    def __init__(self, x: int, y: int, enemy_type: str, screen) -> None:
        self.__screen = screen
        self.__x: int = x
        self.__y: int = y
        # В enemy_type может быть watcher, blinder, stalker
        self.__enemy_type: str = enemy_type
        self.enemy_draw_and_move()
        
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
        
    def __to_texture(self, command: str) -> pygame.surface.Surface:
        """
        От команды к текстуре в игре.
        
        Args:
            command (str): Команда для загрузки текстуры монстра.
        Returns:
            pygame.surface.Surface: Текстура монстра.
        """
        pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

        match = re.search(pattern, command)
        return load(match.group(1), (60, 60), "convert_alpha")
    
    @staticmethod
    def die(logger: HELogger) -> None:
        """
        Смерть врага
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        super().die()
        logger.info("Враг побеждён!")
    
    def enemy_draw_and_move(self) -> None:
        """
        Движение и отрисовка NPC (AI)
        """
        if self.__enemy_type == "watcher":
            self.__screen.blit(self.__to_texture(self.enemy_dict['1'][4]),
                            (self.enemy_dict['1'][0], self.enemy_dict['1'][1]))
        elif self.__enemy_type == "blinder":
            self.__screen.blit(self.__to_texture(self.enemy_dict['3'][4]),
                            (self.enemy_dict['3'][0], self.enemy_dict['3'][1]))
        elif self.__enemy_type == "stalker":
            self.__screen.blit(self.__to_texture(self.enemy_dict['2'][4]),
                            (self.enemy_dict['2'][0], self.enemy_dict['2'][1]))
    