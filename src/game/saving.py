"""Сохранения в игре"""

import json


class Saving:
    
    def load_save(self) -> dict:
        """Загрузка сохранений"""
        try:
            with open("data/data.json") as file:
                some_dict = json.load(file)
        except FileNotFoundError:
            self.__not_found()
            some_dict = {"index": [3, 3]}
        return some_dict
    
    def __not_found(self) -> None:
        """Если файл data.json не найден"""
        with open("data/data.json", "w") as file:
            some_dict = {
                "index": [3, 3]
            }
            json.dump(some_dict, file, indent=2, separators=(',', ': '))
    
    def saving(self) -> None:
        """Сохранение игры"""
        pass
