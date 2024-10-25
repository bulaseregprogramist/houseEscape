"""Ловушки в доме"""

import pygame
from ..other.globals import load
from ..entity.player import Player
from ..traps.aftermath import AfterMath


pygame.init()


class Traps:
    """Ловушки"""
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__poison_trap = load("textures/pt.png", (60, 60), "convert_alpha")
        self.__trap = load("textures/trap.png", (60, 60), "convert_alpha")
        self.__ice = load("textures/ice.png", (60, 60), "convert_alpha")
        self.__aftermath = AfterMath()
        
    def draw_trap(self, x: int, y: int, trap_type: str) -> pygame.rect.Rect:
        """
        Отрисовка ловушек
        
        Args:
            x (int): Позиция ловушки по x,
            y (int): Позиция ловушки по y,
            trap_type (str): Тип ловушки.
        Returns:
            pygame.rect.Rect: 'Квадрат' ловушки.
        """
        if trap_type == "poison":
            self.__screen.blit(self.__poison_trap, (x, y))
            rect = self.__poison_trap.get_rect(topleft=(x, y))
        elif trap_type == "trap":
            self.__screen.blit(self.__trap, (x, y))
            rect = self.__trap.get_rect(topleft=(x, y))
        elif trap_type == "ice":
            self.__screen.blit(self.__ice, (x, y))
            rect = self.__ice.get_rect(topleft=(x, y))
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
        if rect.colliderect(player_rect):  # Попадание в ловушку
            if trap_type == "poison":
                self.__aftermath.poison_aftermath()
            elif trap_type == "trap":
                self.__aftermath.common_aftermath()
            elif trap_type == "ice":
                self.__aftermath.ice_aftermath()
            Player.die(self.__screen)
