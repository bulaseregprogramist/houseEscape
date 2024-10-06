"""Отрисовка комнат"""

import pygame
from ..other.globals import font, load
from ..game.logging import HELogger
from ..entity.enemys import Enemy
from keyboard import is_pressed
import sys
from time import sleep


pygame.init()


class Draw:
    """Этот класс отвечает за отрисовку локаций и другого"""
    
    def __init__(self, logger: HELogger) -> None:
        logger.info("Работа конструктора класса Draw начата!")
        self.__bg1 = load("textures/1.png", (770, 770), "convert")
        self.__bg2 = load("textures/2.png", (770, 770), "convert")
        self.__bg3 = load("textures/3.png", (770, 770), "convert")
        self.__bg4 = load("textures/4.png", (770, 770), "convert")
        self.__bg5 = load("textures/5.png", (770, 770), "convert")
        self.__bg6 = load("textures/6.png", (770, 770), "convert")
        self.__bg7 = load("textures/7.png", (770, 770), "convert")
        self.__bg8 = load("textures/8.png", (770, 770), "convert")
        self.__bg9 = load("textures/9.png", (770, 770), "convert")
        self.__bg10 = load("textures/house.png", (770, 770), "convert")
        logger.info("Работа конструктора класса Draw завершена!")
        
    @staticmethod
    def show_interfaces() -> None:
        """Интерфейсы для мебели"""
        text = font.render("123", 1, (255, 255, 255))
        interface_cycle = 1
        while interface_cycle:
            pygame.display.flip()
            
            {sys.exit() for i in pygame.event.get() if i.type == pygame.QUIT}
            if is_pressed("esc"):
                sleep(0.15)
                interface_cycle = 0
    
    def render_location(self, index: list[int, int],
                        screen: pygame.surface.Surface) -> None:
        """
        Рендеринг комнаты дома

        Args:
            index (list[int, int]): Карта дома,
            screen (pygame.surface.Surface): Переменная экрана
        """
        if index == [0, 2]:
            screen.blit(self.__bg10, (0, 0))
        elif index == [1, 1]:
            screen.blit(self.__bg2, (0, 0))
        elif index == [1, 2]:
            screen.blit(self.__bg3, (0, 0))
        elif index == [1, 3]:
            screen.blit(self.__bg4, (0, 0))
        elif index == [2, 1]:
            screen.blit(self.__bg5, (0, 0))
        elif index == [2, 2]:
            screen.blit(self.__bg6, (0, 0))
        elif index == [2, 3]:
            screen.blit(self.__bg7, (0, 0))
        elif index == [3, 1]:
            screen.blit(self.__bg8, (0, 0))
        elif index == [3, 2]:
            screen.blit(self.__bg9, (0, 0))
        elif index == [3, 3]:  # Окрестности дома
            self.__enemys = Enemy(Enemy.enemy_dict[1][0],
                                Enemy.enemy_dict[1][1], "watcher")
            screen.blit(self.__bg1, (0, 0))
        