"""Сохранения в игре"""

import json
import pygame
from ..other.globals import some_dict
from .logging import HELogger


pygame.init()


class Saving:
    
    def load_save(self, numb: int, logger: HELogger = None) -> dict:
        """
        Загрузка сохранений
        
        Args:
            numb (int): Номер выбранного игроком сохранения,
            logger (HELogger | None): Параметр по умолчанию, для логов.
        Returns:
            dict: Сохранённые ранее данные игры.
        """
        try:
            if logger is not None:
                logger.debug("Идёт загрузка данных")
            with open(f"data/data{numb}.json") as file:
                some_dict: dict = json.load(file)
            some_dict: dict = self.load_textures(numb)
        except FileNotFoundError:
            if logger is not None:
                logger.error("Ошибка. Файл data.json не найден")
            self.__not_found(numb, logger)
            some_dict: dict = self.load_textures(numb)
        return some_dict
    
    def __not_found(self, numb: int, logger: HELogger = None) -> None:
        """
        Если файл data.json не найден
        
        Args:
            numb (int): Номер выбранного сохранения
            logger (HELogger | None): Переменная по умолчанию, для логов.
        """
        if logger is not None:
            logger.debug("Устранение ошибки.")
        with open(f"data/data{numb}.json", "w") as file:
            json.dump(some_dict, file, indent=3)
            
    def load_textures(self, numb: int) -> dict:
        """
        Загрузка текстур в словари
        
        Args:
            numb (int): Номер выбранного сохранения.
        Returns:
            dict: Словарь с данными игры
        """
        with open(f"data/data{numb}.json") as file:
            result: dict = json.load(file)
        return result
    
    def saving(self, index: list[int, int], x: int, y: int, n: int) -> None:
        """
        Сохранение игры
        
        Args:
            index (list[int, int]): Позиция игрока на карте,
            x (int): Позиция игрока по x,
            y (int): Позиция игрока по y,
            n (int): Выбранное игроком сохранение.
        """
        result: dict = self.load_save(n)  # Получение словаря из data.json
        result["index"] = index
        result["x"] = x
        result["y"] = y
        with open(f"data/data{n}.json", "w") as file:
            json.dump(result, file, indent=2)
        
