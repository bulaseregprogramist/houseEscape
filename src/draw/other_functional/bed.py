"""Кровать"""

import pygame
from src.other.globals import font
import logging
import sys


pygame.init()


class Bed:
    """Кровать дома"""
    
    def __init__(self, screen):
        self.__screen = screen
        self.__text = font.render("Кровать", 1, (0, 0, 0))

    def __draw_bed(self) -> None:
        """
        Отрисовка интерфейса кровати
        """
        pygame.draw.rect(self.__screen, (235, 255, 245), (150, 150, 470, 570))
        self.__screen.blit(self.__text, (290, 170))

    def run(self) -> None:
        """Основной метод класса"""
        
        bed_cycle = 1
        while bed_cycle:
            self.__draw_bed()
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
                    bed_cycle = 0

