"""Транспорт игры HouseEscape"""

from ..gameobjects.gameobjects import GameObjects
from ..other.globals import load


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
    
    def functional(self) -> None:
        """Функционал транспорта"""
        pass
    