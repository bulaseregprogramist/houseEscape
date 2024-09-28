"""Мебель дома"""

from .gameobjects import GameObjects
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    __blocks = {
        1: [150, 150, 2, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))],
        2: [320, 320, 2, 3, pygame.transform.scale(pygame.image.load("textures/boosty.png"), (50, 50))]
        }
    
    def placing(self, he_map: list[int, int]) -> None:
        for i in self.__blocks:
            super().placing(self.__blocks[i][0], self.__blocks[i][1],
                            [self.__blocks[i][2], self.__blocks[i][3]],
                            he_map,
                            self.__blocks[i][4])
            self.functional()
    
    def functional(self) -> None:
        pass