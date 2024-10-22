"""Концовки игры HouseEscape"""

import pygame
import sys
from ..other.globals import font


pygame.init()


class Endings:
    """Основной функционал концовок"""
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
    
    def identify_ending(self) -> None:
        """Определение на какую концовку прошёл игрок"""
        pass
    
    def draw_ending(self, name: str) -> None:
        """
        Отрисовка концовки
        
        Args:
            name (str): Название концовки.
        """
        cycle = 1
        text = font.render("ВЫ ПРОШЛИ ИГРУ", 1, (0, 211, 0))
        text2 = font.render(f"ВАША КОНЦОВКА - {name}", 1, (250, 0, 0))
        while cycle:
            self.__screen.blit(text, (330, 330))
            self.__screen.blit(text2, (330, 380))
            
            pygame.display.flip()
            
            {sys.exit() for i in pygame.event.get if i.type == pygame.QUIT}
