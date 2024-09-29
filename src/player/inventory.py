"""Инвентарь игрока"""

import pygame
import sys


pygame.init()


class Inventory:
    inventory_list = []
    
    def __init__(self, inventory, screen) -> None:
        self.__inventory = inventory
        self.__screen = screen
    
    def open(self) -> None:
        """Открытие инвентаря"""
        inv_cycle = 1
        while inv_cycle:
            self.__screen.fill((0, 0, 0))
            self.__screen.blit(self.__inventory, (10, 10))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
