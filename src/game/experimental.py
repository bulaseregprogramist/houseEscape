"""Экспериментальные функции"""

import pygame
import sys
from ..other.globals import font3


pygame.init()


class Experimental:
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__sound1 = pygame.mixer.Sound("textures/collect.mp3")
        self.__text1 = font3.render("Экспериментальные возможности", 1, (0, 0, 0))
        self.__sound1.set_volume(0.41)
    
    def run(self) -> None:
        """Основной метод класса"""
        self.__sound1.play()
        cycle = 1
        while cycle:
            self.__screen.fill((255, 255, 255))
            self.__screen.blit(self.__text1, (150, 50))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    cycle = 0
