"""Транспорт игры HouseEscape"""

from ..gameobjects.gameobjects import GameObjects
from ..other.globals import load
import pygame


pygame.init()


class Vehicles(GameObjects):
    """Транспортные средства. Наследник абстрактного класса GameObjects."""
    
    def __init__(self, vehicle_type: str) -> None:
        if vehicle_type == "1":
            self.vehicle = load("textures/car.png", (80, 60), "convert_alpha")
        else:
            self.vehicle = load("textures/boat.png", (80, 60), "convert_alpha")
    
    def placing(self) -> None:
        """Размещение транспорта на карте"""
        pass
    
    def functional(self, x: int, y: int, 
                texture: pygame.surface.Surface, i: int,
                he_map: list[int, int], index: list[int, int]) -> int:
        """
        Функционал транспорта
        
        Args:
            x (int): Позиция машины по x,
            y (int): Позиция машины по y,
            texture (pygame.surface.Surface): Текстура машины,
            i (int):
            he_map (list[int, int]):
            index (list[int, int]):
        Returns:
            int:
        """
        result: int = super().functional(x, y, texture, "vehicle",
                                        he_map, index, i)
        if result == 3:  # Помещение предмета в инвентарь
            pygame.mixer.Sound("textures/open.mp3").play()
            return 1, i
        return 0, i
    