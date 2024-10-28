"""После использования предмета"""

from ..entity.endings import Endings
from ..game.saving import Saving
import pygame
import json
import logging

pygame.init()


class AfterUse:
    
    def __init__(self, texture_id: int, index: list[int, int],
                screen: pygame.surface.Surface, n: int) -> None:
        self.__index: list[int, int] = index
        self.__endings = Endings(screen)
        self.__save = Saving()
        self.__n: int = n
        self.__some_dict: dict = self.__save.load_save(n)
        self.__blocks: dict[int: list] = self.__some_dict["blocks"]
        self.__texture_id = str(texture_id)
        
    def change_exit(self) -> None:
        """Изменение внешнего вида решётки (сохранение)"""
        logging.info("Внешний вид выхода изменён!")
        with open(f"data/data{self.__n}.json", "w") as file:
            json.dump(self.__some_dict, file, indent=2)
        logging.info("Данные сохранены!")

    def functional(self, pos: tuple[int, int]) -> None:
        """
        Проверяет, находится ли курсор мыши над предметом и вызывает метод identify_ending.
        
        Args:
            pos (tuple[int, int]): Позиция курсора мыши.
        """
        if self.__texture_id == '9':
            if (self.__index == [3, 1]
                    and 50 <= pos[0] <= 230
                    and -41 <= pos[1] <= 101
                    and self.__blocks['7'][4] == 
                    'pygame.image.load(\'textures/exit2.png\')'):
                self.__blocks['7'][4] = 'pygame.image.load(\'textures/exit3.png\')'
                self.__some_dict["blocks"] = self.__blocks
                self.change_exit()
            elif (self.__index == [3, 1]
                    and 50 <= pos[0] <= 230
                    and -41 <= pos[1] <= 101
                    and self.__blocks['7'][4] ==
                    'pygame.image.load(\'textures/exit3.png\')'):
                self.__endings.pre_ending("Концовка Решётки")