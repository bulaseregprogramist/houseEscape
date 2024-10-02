"""Сохранения в игре"""

import json


class Saving:
    
    def load_save(self) -> dict:
        """
        Загрузка сохранений
        
        Returns:
            Сохранённые ранее данные игры.
        """
        try:
            with open("data/data.json") as file:
                some_dict = json.load(file)
        except FileNotFoundError:
            self.__not_found()
            some_dict = {"index": [3, 3], "x": 385, "y": 385}
        return some_dict
    
    def __not_found(self) -> None:
        """Если файл data.json не найден"""
        with open("data/data.json", "w") as file:
            some_dict = {
                "index": [3, 3],
                "x": 385,
                "y": 385
            }
            json.dump(some_dict, file, indent=2)
    
    def saving(self, index: list[int, int], x: int, y: int) -> None:
        """
        Сохранение игры
        
        Args:
            index (list[int, int]): Позиция игрока на карте,
            x (int): Позиция игрока по x,
            y (int): Позиция игрока по y.
        """
        result: dict = self.load_save()  # Получение словаря из data.json
        result["index"] = index
        result["x"] = x
        result["y"] = y
        with open("data/data.json", "w") as file:
            json.dump(result, file, indent=2)
        
