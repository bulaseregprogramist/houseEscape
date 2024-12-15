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
    
    def placing(self, he_map: list[int, int], player: Player, n: int, use,
                have_functional=1) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Объект игрока,
            n (int): Номер выбранного сохранения,
            use (Use): Объект класса Use,
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
                            he_map, some_list, i, n, player, use)
    
    def functional(self, *args) -> None:
        """
        Функционал мебели
        
        Args:
            *args (tuple[int, int, pygame.surface.Surface, Player, Use]):
            Ключ словаря, текстура, объекты игрока и Use, ...
        """
        result: int = super().functional(args[0], args[1], args[2], "block",
                                        args[3], args[4], None)
        if result == 2:  # Открытие меню мебели
            Draw.show_interfaces(args[5], self.screen, args[6], args[3],
                                args[7], self.__logger, args[8])
            pygame.mixer.Sound("textures/press2.mp3").play()
            self.__logger.debug(
                "Завершена работа УО метода functional класса Block")
    