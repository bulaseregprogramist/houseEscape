"""Мебель дома"""

from .gameobjects import GameObjects
from ..draw.draw import Draw
from ..game.saving import Saving
from ..entity.player import Player
from ..game.logging import HELogger
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    save = Saving()
    screen: pygame.surface.Surface
    
    def __init__(self, logger: HELogger) -> None:
        self.__logger: HELogger = logger
        self.__logger.debug("Завершена работа конструктора класса Block")
    
    def placing(self, he_map: list[int, int], player: Player, n: int,
                have_functional=1) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Объект игрока,
            n (int): Номер выбранного сохранения,
            have_functional (int): Выключается для анимации.
        """
        # Позиции мебели и их текстуры
        self.__blocks: dict[int: list, ...] = self.save.load_save(n)["blocks"]
        for i in self.__blocks:
            texture = pygame.transform.scale(
                self._num_to_texture(self.__blocks[i][4]), (50, 50))
            some_list: list[int, int] = [self.__blocks[i][2],
                                        self.__blocks[i][3]]
            super().placing(int(self.__blocks[i][0]),
                int(self.__blocks[i][1]), some_list, he_map, texture, player)
            if have_functional:
                self.functional(self.__blocks[i][0], self.__blocks[i][1], texture,
                            he_map, some_list, i, n, player)
    
    def functional(self, x: int, y: int, texture: pygame.surface.Surface,
                he_map: list[int, int], some_list: list[int, int],
                i: int, n: int, player: Player) -> None:
        """
        Функционал мебели
        
        Args:
            x (int): Позиция мебели по x,
            y (int): Позиция мебели по y,
            texture (pygame.surface.Surface): Текстура мебели,
            he_map (list[int, int]): Позиция игрока на карте,
            some_list (list[int, int]): Позиция мебели на карте,
            i (int): Ключи мебели,
            n (int): Номер выбранного сохранения,
            player (Player): Объект игрока
        """
        result: int = super().functional(x, y, texture, "block", he_map, 
                                        some_list)
        if result == 2:  # Открытие меню мебели
            Draw.show_interfaces(i, self.screen, n, he_map, player, self.__logger)
            pygame.mixer.Sound("textures/press2.mp3").play()
            self.__logger.debug(
                "Завершена работа УО метода functional класса Block")
    