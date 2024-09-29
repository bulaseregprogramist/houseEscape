"""Отрисовка комнат"""

import pygame
from ..logging import HELogger


pygame.init()


class Draw:
    """Этот класс отвечает за отрисовку локаций"""
    
    def __init__(self, logger: HELogger) -> None:
        self.__bg1 = pygame.transform.scale(pygame.image.load("textures/1.png").convert(), (770, 770))
        self.__bg2 = pygame.transform.scale(pygame.image.load("textures/2.png").convert(), (770, 770))
        self.__bg3 = pygame.transform.scale(pygame.image.load("textures/3.png").convert(), (770, 770))
        self.__bg4 = pygame.transform.scale(pygame.image.load("textures/4.png").convert(), (770, 770))
        self.__bg5 = pygame.transform.scale(pygame.image.load("textures/5.png").convert(), (770, 770))
        self.__bg6 = pygame.transform.scale(pygame.image.load("textures/6.png").convert(), (770, 770))
        self.__bg7 = pygame.transform.scale(pygame.image.load("textures/7.png").convert(), (770, 770))
        self.__bg8 = pygame.transform.scale(pygame.image.load("textures/8.png").convert(), (770, 770))
        self.__bg9 = pygame.transform.scale(pygame.image.load("textures/9.png").convert(), (770, 770))
        self.__bg10 = pygame.transform.scale(pygame.image.load("textures/house.png").convert(), (770, 770))
        logger.info("Работа конструктора класса Draw завершена!")
    
    def render_location(self, index: list[int, int], screen: pygame.surface.Surface) -> None:
        """
        Рендеринг комнаты дома

        Args:
            index (list[int, int]): Карта дома,
            screen (pygame.surface.Surface): Переменная экрана
        """
        if index == [0, 2]:
            screen.blit(self.__bg1, (0, 0))
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
            screen.blit(self.__bg10, (0, 0))
        