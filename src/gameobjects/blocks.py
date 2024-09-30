"""Мебель дома"""

from .gameobjects import GameObjects
from ..draw.draw import Draw
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    __blocks = {  # Позиции мебели и их текстуры
        1: [450, 150, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [20, 320, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
    
    def placing(self, he_map: list[int, int], player: object) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Карта дома
            player (Player): Игрок
        """
        for i in self.__blocks:
            super().placing(self.__blocks[i][0], self.__blocks[i][1],
                            [self.__blocks[i][2], self.__blocks[i][3]],
                            he_map,
                            self.__blocks[i][4], player)
            self.functional(self.__blocks[i][0], self.__blocks[i][1], self.__blocks[i][4])
    
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
            Draw.show_interfaces()
            pygame.mixer.Sound("textures/press2.mp3").play()
    