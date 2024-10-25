"""Функционал остальной мебели и техники"""

import json
import pygame
import sys
import logging
from ..game.saving import Saving
from ..other.globals import font
from ..entity.player import Player


pygame.init()


class OtherFunctional:
    
    def __init__(self, num: int, screen: pygame.surface.Surface,
                index: list[int, int], player: Player) -> None:
        self.__num = num
        self.__screen: pygame.surface.Surface = screen
        self.__index: list[int, int] = index
        self.__player = player
        self.__text = font.render("Шкаф", 1, (0, 0, 0))
        self.__save = Saving()
    
    def closet(self) -> None:
        """Шкаф"""
        with open(f"data/data{self.__num}.json") as file:
            result: dict[str: list | dict | int] = json.load(file)
        items: list[str, ...] = result["closet_items"]
        
        closet_cycle = 1
        while closet_cycle:
            pygame.draw.rect(self.__screen, (255, 255, 255),
                            (150, 150, 470, 470))
            self.__screen.blit(self.__text, (330, 170))
            
            for i in items:  # Отрисовка предметов шкафа
                pass
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Выход из игры...")
                    self.__save.saving(self.__index, 
                                self.__player.x, self.__player.y,
                                self.__num, True)
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    closet_cycle = 0
    
    def lamp(self) -> None:
        """Лампа в доме"""
        pass
    
    def bed(self) -> None:
        """Кровать в доме"""
        pass
