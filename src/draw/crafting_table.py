"""Стол для создания предметов"""

import pygame
from ..game.saving import Saving
from ..entity.inventory import Inventory
from time import sleep
from ..game.logging import HELogger
from ..entity.player import Player
from copy import copy
import sys


pygame.init()


class CraftingTable:
    save = Saving()
    logger: HELogger
    
    def __init__(self, screen, text, n: int, index: list[int, int],
                player: Player) -> None:
        self.__index: list[int, int] = index
        self.__player = player
        self.__screen = screen
        self.__text = text
        self.__keys: list[str, ...] = self.save.load_save(n)["items_id"]
        self.__some_list = copy(Inventory.inventory_list)
        self.__some_list.extend(Inventory.inventory_list2)
        self.__n = n
        self.__run()
        
    def __recipes(self) -> None:
        """Рецепты в верстаке"""
        if "1" in self.__keys:
            pass
        elif "2" in self.__keys:
            pass
        elif "3" in self.__keys:
            pass
        
    def __run(self) -> None:
        """Основной метод класса."""
        crafting_table_cycle = 1
        while crafting_table_cycle:
            pygame.draw.rect(self.__screen, 
                            (255, 255, 255), (100, 100, 570, 570))
            self.__screen.blit(self.__text, (139, 130))
            x, y = 170, 490
            
            # Отрисовка предметов в инвентаре
            for i in range(len(self.__some_list)):
                try:  # УО нужен для отрисовки хранимых в инвентаре предметов.
                    self.__screen.blit(self.__some_list[i], (x, y))
                except TypeError:
                    self.__screen.blit(self.__some_list[i][0], (x, y))
                    
                x += 70
                if (i + 1) % 6 == 0:  # Перенос предметов вниз.
                    x = 170
                    y += 70
            pygame.display.flip()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.logger.info("Выход из игры...")
                    self.save.saving(self.__index, self.__player.x,
                                    self.__player.y, self.__n)
                    sys.exit()
                elif (event.type == pygame.KEYDOWN
                        and event.key == pygame.K_ESCAPE):
                    sleep(0.15)
                    crafting_table_cycle = 0
