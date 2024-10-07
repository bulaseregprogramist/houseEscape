"""Транспорт игры HouseEscape"""

from ..gameobjects.gameobjects import GameObjects


class Vehicles(GameObjects):
    """Транспортные средства. Наследник абстрактного класса GameObjects."""
    
    def placing(self) -> None:
        """Размещение транспорта на карте"""
        pass
    
    def functional(self) -> None:
        """Функционал транспорта"""
        pass
    