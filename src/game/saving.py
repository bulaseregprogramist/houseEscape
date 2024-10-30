"""Сохранения в игре"""

import json
import pygame
from ..other.globals import some_dict
from .logging import HELogger
import logging


pygame.init()


class Saving:
    inventory: object  # Хранит класс Inventory
    
    def load_save(self, numb: int, logger: HELogger = None) -> dict:
        """
        Загрузка сохранений
        
        Args:
            numb (int): Номер выбранного игроком сохранения,
            logger (HELogger | None): Параметр по умолчанию, для логов.
        Returns:
            dict[str: list | int | dict]: Сохранённые ранее данные игры.
        """
        try:
            # logger может быть None, в файлах blocks.py и items.py
            if logger is not None:
                logger.debug("Идёт загрузка данных")
            with open(f"data/data{numb}.json") as file:
                some_dict: dict[str: list | int | dict] = json.load(file)
            some_dict: dict[str: list | int | dict] = self.load_textures(numb)
        except FileNotFoundError:
            if logger is not None:
                logger.error("Ошибка. Файл data.json не найден")
            self.__not_found(numb, logger)
            some_dict: dict[str: list | int | dict] = self.load_textures(numb,
                                                                    logger)
        return some_dict
    
    def __not_found(self, numb: int, logger: HELogger = None) -> None:
        """
        Если файл data.json не найден
        
        Args:
            numb (int): Номер выбранного сохранения
            logger (HELogger | None): Параметр по умолчанию, для логов.
        """
        if logger is not None:
            logger.debug(f"Файл data{numb}.json не найден!")
            logger.debug("Устранение ошибки.")
            logger.debug("Ошибка исправлена!")
        with open(f"data/data{numb}.json", "w") as file:
            json.dump(some_dict, file, indent=2)
            
    def load_textures(self, numb: int, logger: HELogger = None) -> dict:
        """
        Загрузка текстур в словари
        
        Args:
            numb (int): Номер выбранного сохранения,
            logger (HELogger): Переменная для логов, по умолчанию None.
        Returns:
            dict: Словарь с данными игры.
        """
        with open(f"data/data{numb}.json", encoding='utf-8') as file:
            result: dict[str: list | int | dict] = json.load(file)
        if logger is not None:
            logger.debug("Текстуры получены!")
        return result
    
    def saving(self, index: list[int, int], x: int, y: int, n: int, 
            inventory_saving: bool = False) -> None:
        """
        Сохранение игры
        
        Args:
            index (list[int, int]): Позиция игрока на карте,
            x (int): Позиция игрока по x,
            y (int): Позиция игрока по y,
            n (int): Выбранное игроком сохранение,
            inventory_saving (bool): По умолчанию, сохранять ли инвентарь.
        """
        # Получение словаря из data.json
        result: dict[str: list | int | dict] = self.load_save(n)
        result["index"] = index  # Позиция игрока на карте.
        result["x"] = x
        result["y"] = y
        if inventory_saving:
            if result["items_id"] == []:
                items_id = []
            else:  # Если предметы есть
                items_id: list[str, ...] = result["items_id"]
            for b in self.inventory.inventory_list:  # Сохранение предметов
                items_id.append(b[1])
            result["items_id"] = items_id
        with open(f"data/data{n}.json", "w") as file:
            json.dump(result, file, indent=2)
            
    def save_closet_items(self, items: list[str, ...], num: int, 
                        some_dict: dict) -> None:
        """Сохраняет предметы шкафа"""
        logging.debug("Идёт сохранение предметов")
        some_dict["closet_items"] = items
        with open(f"data/data{num}.json", "w") as file:
            json.dump(some_dict, file, indent=2)
        logging.debug("Предметы шкафа сохранены!")
        
