from src.gameobjects.gameobjects import GameObjects
import pygame
from ..logging import HELogger
from ..player.player import Player


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""
    __items =  {
        1: [150, 150, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [320, 320, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
    
    def placing(self, he_map: list[int, int], player: Player) -> None:
        """
        Размещение предмета
        
        Args:
            he_map (list[int, int]): Карта дома,
            player (Player): игрок
        """
        for i in self.__items:
            super().placing(self.__items[i][0], self.__items[i][1],
                            [self.__items[i][2], self.__items[i][3]],
                            he_map,
                            self.__items[i][4],
                            player)
            self.functional(self.__items[i][0], self.__items[i][1], self.__items[i][4])
    
    def functional(self, x: int, y: int, texture) -> None:
        """
        Функционал предметов
        
        Args:
            x (int): Позиция предмета по x,
            y (int): Позиция предмета по y,
            texture (object): Текстура предмета
        """
        result: int = super().functional(x, y, texture, "item")
        if result == 1:
            pygame.mixer.Sound("textures/press.mp3").play()
    