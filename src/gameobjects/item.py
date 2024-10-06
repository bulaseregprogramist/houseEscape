"""Предметы игры"""

from src.gameobjects.gameobjects import GameObjects
import pygame
from ..game.logging import HELogger
from ..player.player import Player
from ..game.saving import Saving
import json


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""
    save = Saving()
    some_num = 1
    
    def placing(self, he_map: list[int, int], player: Player, n: int) -> None:
        """
        Размещение предмета
        
        Args:
            he_map (list[int, int]): Карта дома,
            player (Player): игрок
        """
        if self.some_num:
            self.__items = self.save.load_save(n)["items"]  # Позиции предметов и их текстуры
        delete = 0
        for i in self.__items:
            texture = pygame.transform.scale(eval(self.__items[i][4]), (50, 50))
            super().placing(self.__items[i][0], self.__items[i][1],
                            [self.__items[i][2], self.__items[i][3]],
                            he_map,
                            texture,
                            player)
            delete, key = self.functional(self.__items[i][0], self.__items[i][1],
                            texture, i, self.__items)
        if delete == 1:  # Помещение предмета в инвентарь
            self.__items.pop(key)
            self.__save_item(n)
            self.some_num = 0
    
    def functional(self, x: int, y: int, 
                texture: pygame.surface.Surface, i: int, key: str) -> int:
        """
        Функционал предметов
        
        Args:
            x (int): Позиция предмета по x,
            y (int): Позиция предмета по y,
            texture (object): Текстура предмета
        Returns:
            int: Два числа. Первое число отвечает за удаление из словаря,
                            второе за удаляемый ключ
        """
        result: int = super().functional(x, y, texture, "item", i)
        if result == 1:  # Помещение предмета в инвентарь
            pygame.mixer.Sound("textures/press.mp3").play()
            return 1, i
        return 0, i
    
    def __save_item(self, n: int) -> None:
        """
        Сохранение предметов.
        
        Args:
            n (int): Номер выбранного сохранения.
        """
        some_dict = self.save.load_save(n)
        some_dict["items"] = self.__items
        with open(f"data/data{n}.json", "w") as file:
            json.dump(some_dict, file)
    