"""Лампа"""

import pygame
from src.other.globals import font
import logging
import sys


pygame.init()


class Lamp:
    """Лампа дома"""
    
    def __init__(self, screen):
        self.__screen = screen
        self.__text = font.render("Лампа", 1, (0, 0, 0))

    def __draw_lamp(self) -> None:
        """
        Отрисовка интерфейса лампы
        """
        pygame.draw.rect(self.__screen, (235, 255, 245), (150, 150, 470, 570))
        self.__screen.blit(self.__text, (310, 170))

    def run(self) -> None:
        """Основной метод класса"""
        
        lamp_cycle = 1
        while lamp_cycle:
            self.__draw_lamp()
            mouse_position: tuple[int, int] = pygame.mouse.get_pos()
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Выход из игры...")
                    self.__save.saving(
                        self.__index, self.__player.x,
                        self.__player.y, self.__num, True
                    )
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    lamp_cycle = 0

