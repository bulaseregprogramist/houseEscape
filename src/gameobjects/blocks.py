"""Мебель дома"""

from .gameobjects import GameObjects
from ..other.globals import font
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    __blocks = {
        1: [150, 150, 2, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [320, 320, 2, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
    
    def placing(self, he_map: list[int, int]) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Карта дома
        """
        for i in self.__blocks:
            super().placing(self.__blocks[i][0], self.__blocks[i][1],
                            [self.__blocks[i][2], self.__blocks[i][3]],
                            he_map,
                            self.__blocks[i][4])
            self.functional()
    
    def functional(self, x: int, y: int, texture) -> None:
        """
        Функционал мебели
        
        Args:
            x (int): Позиция мебели по x,
            y (int): Позиция мебели по y,
            texture (object): Текстура мебели
        """
        result: int = super().functional(x, y, texture, "block")
        if result == 2:
            pygame.mixer.Sound("textures/press2.mp3").play()
        
    @staticmethod
    def show_interface() -> None:
        """Интерфейс для мебели (при наведении на мебель)"""
        text = font.render("123", 1, (255, 255, 255))