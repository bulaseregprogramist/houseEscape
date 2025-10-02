"""Функционал остальной мебели и техники"""

import pygame
from ...game.saving import Saving
from ...entity.player import Player
from .closet import Closet
from .bed import Bed
from ...other.globals import traps_dict
from .lamp import Lamp
import sys  # Для sys.exit()


pygame.init()


class OtherFunctional:
    # Эти переменные хранят одноимённые классы
    block = None
    item = None
    traps = None

    def __init__(
        self, num: int,
        screen: pygame.surface.Surface,
        index: list[int, int], player: Player,
        logger) -> None:
        self.__num = num
        self.__screen: pygame.surface.Surface = screen
        self.__index: list[int, int] = index
        self.__player: Player = player
        self.__clock = pygame.time.Clock()
        self.__save = Saving()

        self.block.screen = self.__screen
        logger.debug("Переменной screen класса Block присвоено значение")
        self.__blocks = self.block(logger)  # Это не блоки, а мебель
        # Предметы (их можно подбирать и использовать)
        self.__items = self.item(logger)
        self.__traps = self.traps(self.__screen)

    def __general(self, use) -> None:
        """
        Общий метод для остальных методов класса
        (анимация)
        """
        counter, general_cycle = 0, 1
        width = 0
        while general_cycle:
            self.__blocks.placing(self.__index,
                                self.__player, self.__num, use, 0)
            self.__items.placing(self.__index, self.__player, self.__num, 0)
            for j in traps_dict:  # Отрисовка ловушек
                if (traps_dict[j][2] == self.__index[0]
                    and traps_dict[j][3] == self.__index[1]):
                    self.__traps.draw_trap(
                        traps_dict[j][0], traps_dict[j][1], traps_dict[j][4]
                    )

            self.__clock.tick(144)
            pygame.draw.circle(self.__screen, (255, 0, 0), (375, 375), width)
            counter += 2

            if counter > 1:
                counter = 0
                width += 3
            if width > 560:  # Круг дорисован.
                general_cycle = 0
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__save.saving(
                        self.__index, self.__player.x, 
                        self.__player.y, self.__num, True
                    )
                    sys.exit()

    def closet(self, use) -> None:
        """Шкаф"""
        self.__general(use)
        closet = Closet(
            self.__screen, self.__save, self.__num, 
            self.__player, self.__index
        )
        closet.run(use)

    def lamp(self, use: object) -> None:
        """Лампа в доме"""
        self.__general(use)
        lamp = Lamp()
        lamp.run()

    def bed(self, use: object) -> None:
        """Кровать в доме"""
        self.__general(use)
        bed = Bed()
        bed.run()
