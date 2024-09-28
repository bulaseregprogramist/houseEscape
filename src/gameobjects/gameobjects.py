"""Размещение и функционал предметов/мебели"""

from abc import ABC, abstractmethod
from ..logging import HELogger
import pygame


pygame.init()


class GameObjects(ABC):
    """Этот класс является родителем для классов Item и Block"""
    screen: pygame.surface.Surface
    logger: HELogger
    
    @abstractmethod
    def placing(self, x: int, y: int, index: list[int, int], he_map: list[int, int], texture) -> None:
        """Размещение предмета на карте"""
        if index == he_map:
            self.screen.blit(texture, (x, y))
    
    @abstractmethod
    def functional(self) -> None:
        """Функционал игрового объекта"""
        pass