"""Меню паузы"""

import pygame
import sys
from ..game.logging import HELogger
from time import sleep
from ..other.globals import font
from ..game.saving import Saving


pygame.init()


class Pause:
    """Пауза во время игры (в главном меню не работает)"""
    
    def __init__(self, screen: pygame.surface.Surface, logger: HELogger,
                index: list[int, int], player: object) -> None:
        self.__logger = logger
        self.__screen = screen
        self.__index = index
        self.__player = player
        self.__text1 = font.render("ПАУЗА", 1, (255, 255, 255))
        self.__pause_menu = pygame.transform.scale(pygame.image.load("textures/pm.png").convert(), (300, 770))
        self.__crest = pygame.transform.scale(pygame.image.load("textures/crest.png").convert(), (90, 90))
        self.__run()
        
    def __functional(self) -> int:
        """
        Функционал главного меню
        
        Returns:
            int: Выключает цикл или оставляет его включённым
        """
        self.__screen.blit(self.__crest, (340, 600))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        rect = self.__crest.get_rect(topleft=(340, 600))
        # Остановка цикла меню паузы
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return 0
        return 1
    
    def __run(self) -> None:
        """Основной метод класса"""
        self.__logger.info("Игра поставлена на паузу")
        pause_cycle = 1
        while pause_cycle:
            self.__screen.blit(self.__pause_menu, (240, 0))
            self.__screen.blit(self.__text1, (315, 45))
            pause_cycle = self.__functional()
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__logger.info("Выход из программы")
                    save = Saving()
                    save.saving(self.__index, self.__player.x, self.__player.y)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__logger.info("Выход из меню паузы")
                        pause_cycle = 0
                        sleep(0.412)
    