from src.gameobjects.gameobjects import GameObjects
import pygame
from ..game.logging import HELogger
from ..player.player import Player
from ..other.globals import load


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""
    __items =  {  # Позиции предметов и их текстуры
        1: [150, 150, 3, 3, load("textures/boosty.png", (50, 50), "convert")],
        2: [320, 320, 3, 3, load("textures/boosty.png", (50, 50), "convert")]
        }
    
    def placing(self, he_map: list[int, int], player: Player) -> None:
        """
        Размещение предмета
        
        Args:
            he_map (list[int, int]): Карта дома,
            player (Player): игрок
        """
        delete = 0
        for i in self.__items:
            super().placing(self.__items[i][0], self.__items[i][1],
                            [self.__items[i][2], self.__items[i][3]],
                            he_map,
                            self.__items[i][4],
                            player)
            delete, key = self.functional(self.__items[i][0], self.__items[i][1],
                            self.__items[i][4], i)
        if delete == 1:  # Помещение предмета в инвентарь
            self.__items.pop(key)
    
    def functional(self, x: int, y: int, 
                texture: pygame.surface.Surface, i: int) -> int:
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
        result: int = super().functional(x, y, texture, "item")
        if result == 1:  # Помещение предмета в инвентарь
            pygame.mixer.Sound("textures/press.mp3").play()
            return 1, i
        return 0, i
    