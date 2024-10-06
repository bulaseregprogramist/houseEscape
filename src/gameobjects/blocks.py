"""Мебель дома"""

from .gameobjects import GameObjects
from ..draw.draw import Draw
from ..game.saving import Saving
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    save = Saving()
    
    def placing(self, he_map: list[int, int], player: object, n: int) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Карта дома,
            player (Player): Игрок,
            n (int): Номер выбранного сохранения.
        """
        self.__blocks = self.save.load_save(n)["blocks"]  # Позиции мебели и их текстуры
        for i in self.__blocks:
            texture = pygame.transform.scale(eval(self.__blocks[i][4]), (50, 50))
            super().placing(int(self.__blocks[i][0]), int(self.__blocks[i][1]),
                            [self.__blocks[i][2], self.__blocks[i][3]],
                            he_map,
                            texture, player)
            self.functional(self.__blocks[i][0], self.__blocks[i][1], texture)
    
    def functional(self, x: int, y: int, 
                texture: pygame.surface.Surface) -> None:
        """
        Функционал мебели
        
        Args:
            x (int): Позиция мебели по x,
            y (int): Позиция мебели по y,
            texture (pygame.surface.Surface): Текстура мебели.
        """
        result: int = super().functional(x, y, texture, "block")
        if result == 2:  # Открытие меню мебели
            Draw.show_interfaces()
            pygame.mixer.Sound("textures/press2.mp3").play()
    