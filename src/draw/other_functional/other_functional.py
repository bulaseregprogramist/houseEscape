"""Функционал остальной мебели и техники"""

import pygame
from ...game.saving import Saving
from ...entity.player import Player
from .closet import Closet
from .bed import Bed
from .lamp import Lamp
import sys  # Для sys.exit()


pygame.init()


class OtherFunctional:
    block = None
    item = None
    
    def __init__(self, num: int, screen: pygame.surface.Surface,
                index: list[int, int], player: Player, logger) -> None:
        self.__num = num
        self.__screen: pygame.surface.Surface = screen
        self.__index: list[int, int] = index
        self.__player: Player = player
        self.__clock = pygame.time.Clock()
        self.__save = Saving()
        
        self.block.screen = self.__screen
        logger.debug("Переменной screen класса Block присвоено значение")
        self.__blocks = self.block(logger)  # Это не блоки, а мебель
        self.__items = self.item(
            logger)  # Предметы (их можно подбирать и использовать)
        
    def __general(self) -> None:
        """
        Общий метод для остальных методов класса
        (анимация)
        """
        counter, general_cycle = 0, 1
        width = 0
        while general_cycle:
            self.__blocks.placing(self.__index, self.__player,self.__num, 0)
            self.__items.placing(self.__index, self.__player, self.__num, 0)
            
            self.__clock.tick(144)
            pygame.draw.circle(self.__screen, (255, 0, 0), (375, 375), width)
            counter += 2
            
            if counter > 1:
                counter = 0
                width += 3
            if width > 560:  # Круг дорисован.
                general_cycle = 0
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__save.saving(self.__index, self.__player.x,
                                    self.__player.y, self.__num, True)
                    sys.exit()
    
    def closet(self) -> None:
        """Шкаф"""
        self.__general()
        closet = Closet(self.__screen, self.__save, self.__num,
                        self.__player, self.__index)
        closet.run()
    
    def lamp(self) -> None:
        """Лампа в доме"""
        self.__general()
        lamp = Lamp()
        lamp.run()
    
    def bed(self) -> None:
        """Кровать в доме"""
        self.__general()
        bed = Bed()
        bed.run()
