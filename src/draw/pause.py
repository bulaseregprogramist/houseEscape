"""Меню паузы"""

import pygame
import sys
from ..game.logging import HELogger
from time import sleep
from ..entity.player import Player
from ..other.globals import font, load
from ..draw.mainmenu import MainMenu
from ..game.saving import Saving


pygame.init()


class Pause:
    """Пауза во время игры (в главном меню не работает)"""
    save = Saving()
    
    def __init__(self, screen: pygame.surface.Surface, logger: HELogger,
                index: list[int, int], player: Player, n: int) -> None:
        self.__logger = logger
        self.__screen: pygame.surface.Surface = screen
        self.__index: list[int, int] = index
        self.__player = player
        self.__n: int = n
        self.__text1 = font.render("ПАУЗА", 1, (255, 255, 255))
        self.__pause_menu = load("textures/pm.png", (300, 770), "convert")
        self.__crest = load("textures/crest.png", (90, 90), "convert")
        self.__mm = load("textures/mm.png", (100, 100), "convert")
        
    def __functional(self) -> int:
        """
        Функционал главного меню
        
        Returns:
            int: Выключает цикл или оставляет его включённым. (второй случай)
        """
        self.__screen.blit(self.__crest, (340, 600))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        rect = self.__crest.get_rect(topleft=(340, 600))
        rect2 = self.__mm.get_rect(topleft=(340, 440))
        # Остановка цикла меню паузы
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return 0, 0
        elif rect2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            return 0, 1
        return 1, 0
    
    def run(self) -> int:
        """
        Основной метод класса
        
        Returns:
            int: Выключение цикла или он останется неизменным.
        """
        self.__logger.info("Игра поставлена на паузу")
        pause_cycle = 1
        while pause_cycle:
            self.__screen.blit(self.__pause_menu, (240, 0))
            self.__screen.blit(self.__text1, (315, 45))
            self.__screen.blit(self.__mm, (340, 440))
            
            pause_cycle, button = self.__functional()
            if button:  # Если нажать на кнопку выход в главное меню
                mm = MainMenu()
                self.save.saving(self.__index, self.__player.x, 
                                self.__player.y, self.__n)
                return mm.to_menu()
                
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__logger.info("Выход из программы...")
                    self.save.saving(self.__index, self.__player.x,
                                self.__player.y, self.__n)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__logger.info("Выход из меню паузы")
                        pause_cycle = 0
                        sleep(0.412)
        return 1
    