from src.gameobjects.gameobjects import GameObjects
import pygame
from ..logging import HELogger


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""
    __items =  {
        1: [150, 150, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [320, 320, 3, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
    
    def placing(self, he_map: list[int, int]) -> None:
        for i in self.__items:
            super().placing(self.__items[i][0], self.__items[i][1],
                            [self.__items[i][2], self.__items[i][3]],
                            he_map,
                            self.__items[i][4])
            self.functional()
    
    def functional(self) -> None:
        pass
    