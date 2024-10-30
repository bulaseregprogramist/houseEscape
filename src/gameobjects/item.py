"""Предметы игры"""

from src.gameobjects.gameobjects import GameObjects
import pygame
from ..entity.player import Player, change
from ..game.saving import Saving
from ..game.logging import HELogger
import json


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""
    save = Saving()
    some_num = 1
    
    def __init__(self, logger: HELogger) -> None:
        self.__logger = logger
        self.__logger.debug("Завершена работа конструктора класса Item")
    
    def placing(self, he_map: list[int, int], player: Player, n: int) -> None:
        """
        Размещение предмета
        
        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Игрок,
            n (int): Номер выбранного сохранения.
        """
        if self.some_num:  # Позиции предметов и их текстуры
            self.__items: dict[int: list,
                            ...] = self.save.load_save(n)["items"]
        delete = 0
        for i in self.__items:
            texture = pygame.transform.scale(self._num_to_texture(
                self.__items[i][4]), (50, 50))
            super().placing(self.__items[i][0], self.__items[i][1],
                            [self.__items[i][2], self.__items[i][3]],
                            he_map,
                            texture, player)
            delete, key = self.functional(self.__items[i][0],
                            self.__items[i][1], texture, i, he_map,
                            [self.__items[i][2], self.__items[i][3]])
            if delete:  # Чтобы не было бага
                break
        if delete:  # Помещение предмета в инвентарь
            self.__items.pop(key)
            self.__save_item(n)
            self.some_num = 0  # Для предотвращения повторного срабатывания УО
    
    def functional(self, x: int, y: int, texture: pygame.surface.Surface, 
                i: int, he_map: list[int, int], index: list[int, int]) -> int:
        """
        Функционал предметов
        
        Args:
            x (int): Позиция предмета по x,
            y (int): Позиция предмета по y,
            texture (pygame.surface.Surface): Текстура предмета,
            i (int): Индекс предмета,
            he_map (list[int, int]): Позиция игрока,
            index (list[int, int]): Позиция предмета.
        Returns:
            int: Два числа. Первое число отвечает за удаление из словаря,
                            второе за удаляемый ключ
        """
        result: int = super().functional(x, y, texture, "item", he_map, index,
                                        i)
        if result == 1:  # Помещение предмета в инвентарь
            change()
            pygame.mixer.Sound("textures/press.mp3").play()
            self.__logger.debug("Данные успешно возвращены!")
            return 1, i  # Ключ будет удалён
        return 0, i  # Ключ не будет удалён
    
    def __save_item(self, n: int) -> None:
        """
        Сохранение предметов.
        
        Args:
            n (int): Номер выбранного сохранения.
        """
        some_dict: dict[str: int | dict | list] = self.save.load_save(n)
        some_dict["items"] = self.__items
        self.__logger.info("Предметы сохранены!")
        with open(f"data/data{n}.json", "w") as file:
            json.dump(some_dict, file, indent=2)
    