"""Размещение и функционал предметов/мебели"""

from abc import ABC, abstractmethod
from ..player.inventory import Inventory
from ..logging import HELogger
from ..player.player import Player
import pygame
import pygame.gfxdraw


pygame.init()


class GameObjects(ABC):
    """Этот класс является родителем для классов Item и Block"""
    screen: pygame.surface.Surface
    logger: HELogger
    
    @abstractmethod
    def placing(self, x: int, y: int, index: list[int, int], he_map: list[int, int], texture,
                player: Player) -> None:
        """
        Размещение предмета на карте
        
        Args:
            x (int): Позиция объекта по x,
            y (int): Позиция объекта по y,
            index (list[int, int]): Позиция игрока,
            he_map (list[int, int]): Карта дома,
            texture (object): Текстура объекта,
            player (Player): Объект игрока
        """
        if index == he_map:
            self.screen.blit(texture, (x, y))
        if ((player.x <= x <= player.x + texture.get_width() * 0.5) 
                and (player.y <= y <= player.y + texture.get_height() * 1.1)):
            texture.set_alpha(64)
        else:
            texture.set_alpha(500)
    
    @abstractmethod
    def functional(self, x: int, y: int, texture, go_type: str) -> int:
        """
        Функционал игрового объекта
        
        Args:
            x (int): Позиция объекта по x
            y (int): Позиция объекта по y
            texture (object): Текстура объекта
            go_type (str): GameObject_type. (либо item, либо block)
        Returns:
            int: 0 - ничего не произошло, 1 - воспроизведение звука #1, 2 - звук #2.
        """
        
        rect = texture.get_rect(topleft=(x, y))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        if rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if go_type == "item":
                    Inventory.inventory_list.append(texture)
                    return 1
                elif go_type == "block":
                    return 2
        return 0
    