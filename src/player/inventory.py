"""Инвентарь игрока"""

import pygame
import sys


pygame.init()


class Inventory:
    def __init__(self, inventory) -> None:
        self.__inventory = inventory
    
    def open(self) -> None:
        """Открытие инвентаря"""
        inv_cycle = 1
        while inv_cycle:
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
