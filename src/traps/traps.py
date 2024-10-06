"""Ловушки в доме"""

import pygame
from ..other.globals import load
from ..player.player import Player


pygame.init()


class Traps:
    """Ловушки"""
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen = screen
        self.__poison_trap = load("textures/pt.png", (60, 60), "convert_alpha")
        self.__trap = load("textures/trap.png", (60, 60), "convert_alpha")
        
    def draw_trap(self, x: int, y: int, trap_type: str) -> pygame.rect.Rect:
        """
        Отрисовка ловушек
        
        Args:
            x (int): Позиция ловушки по x,
            y (int): Позиция ловушки по y,
            trap_type (str): Тип ловушки.
        Returns:
            pygame.rect.Rect: 'Квдрат' ловушки.
        """
        if trap_type == "poison":
            self.__screen.blit(self.__poison_trap, (x, y))
            rect = self.__poison_trap.get_rect(topleft=(x, y))
        elif trap_type == "trap":
            self.__screen.blit(self.__trap, (x, y))
            rect = self.__trap.get_rect(topleft=(x, y))
        return rect
            
    def after(self, rect: pygame.rect.Rect, trap_type: str,
            player_rect: pygame.rect.Rect) -> None:
        """
        Последствия попадания в ловушку
        
        Args:
            rect (pygame.rect.Rect): 'Квадрат' ловушки,
            trap_type (str): Тип ловушки,
            player_rect (pygame.rect.Rect): 'Квадрат' игрока.
        """
        if rect.colliderect(player_rect):
            if trap_type == "poison":
                Player.die(self.__screen)
            elif trap_type == "trap":
                pass
