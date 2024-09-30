"""Ловушки в доме"""

import pygame
from ..other.globals import load


pygame.init()


class Traps:
    """Ловушки"""
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen = screen
        self.__poison_trap = load("textures/pt.png", (60, 60), "convert_alpha")
        
    def draw_trap(self, x: int, y: int) -> None:
        """
        Отрисовка ловушек
        
        Args:
            x (int): Позиция ловушки по x,
            y (int): Позиция ловушки по y
        """
        self.__screen.blit(self.__poison_trap, (x, y))
