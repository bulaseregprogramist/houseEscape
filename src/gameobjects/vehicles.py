"""Транспорт игры HouseEscape"""

from ..gameobjects.gameobjects import GameObjects
from ..other.globals import load
from ..game.saving import Saving
from ..entity.player import Player
import pygame
import logging


pygame.init()


class Vehicles(GameObjects):
    """Транспортные средства. Наследник абстрактного класса GameObjects."""
    save = Saving()
    
    def __init__(self, vehicle_type: str) -> None:
        if vehicle_type == "1":
            self.vehicle = load("textures/car.png", (80, 60), "convert_alpha")
        else:
            self.vehicle = load("textures/boat.png", (80, 60), "convert_alpha")
    
    def placing(self, he_map: list[int, int], player: Player, n: int) -> None:
        """
        Размещение транспорта на карте
        
        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Объект игрока,
            n (int): Номер выбранного сохранения.
        """
        self.__vehicles = self.save.load_save(n)["vehicles"]
        for i in self.__vehicles:
            super().placing(self.__vehicles[i][0], self.__vehicles[i][1],
                        [self.__vehicles[i][2], self.__vehicles[i][3]],
                        he_map,
                        self.__vehicles[i][4], player)
    
    def functional(self, x: int, y: int, 
                texture: pygame.surface.Surface, i: int,
                he_map: list[int, int], index: list[int, int]) -> int:
        """
        Функционал транспорта
        
        Args:
            x (int): Позиция машины по x,
            y (int): Позиция машины по y,
            texture (pygame.surface.Surface): Текстура машины,
            i (int): Ключ словаря,
            he_map (list[int, int]): Позиция игрока,
            index (list[int, int]): Позиция объекта на карте
        Returns:
            int: Два числа. Первое число - истина на удаление из словаря,
                            второе за удаляемый ключ
        """
        result: int = super().functional(x, y, texture, "vehicle",
                                        he_map, index, i)
        if result == 3:  # Помещение предмета в инвентарь
            pygame.mixer.Sound("textures/open.mp3").play()
            logging.debug("Данные возвращены!")
            return 1, i
        return 0, i
    