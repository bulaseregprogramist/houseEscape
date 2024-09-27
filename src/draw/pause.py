"""Меню паузы"""

import pygame
import sys
from ..logging import HELogger
from time import sleep


pygame.init()


class Pause:
    """Пауза во время игры"""
    
    def __init__(self, screen, logger: HELogger) -> None:
        self.__logger = logger
        self.__screen = screen
        font = pygame.font.Font("./textures/font.otf", 43)
        self.__text1 = font.render("ПАУЗА", 1, (255, 255, 255))
        self.__pause_menu = pygame.transform.scale(pygame.image.load("textures/pm.png").convert(), (300, 770))
        self.__run()
    
    def __run(self) -> None:
        """Основной метод класса"""
        self.__logger.info("Игра поставлена на паузу")
        pause_cycle = 1
        while pause_cycle:
            self.__screen.blit(self.__pause_menu, (240, 0))
            self.__screen.blit(self.__text1, (315, 45))
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__logger.info("Выход из программы")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_cycle = 0
                        sleep(0.412)
    