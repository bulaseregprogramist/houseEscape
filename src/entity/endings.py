"""Концовки игры HouseEscape"""

import pygame
import sys  # Для sys.exit()
from ..other.globals import font
import logging


pygame.init()


class Endings:
    """Основной функционал концовок"""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen

    def pre_ending(self, name: str) -> None:
        """
        Перед концовкой
        
        Args:
            name (str): Название концовки.
        """
        logging.info("Игрок прошёл игру!")
        self.draw_ending(name)

    def draw_ending(self, name: str) -> None:
        """
        Отрисовка концовки

        Args:
            name (str): Название концовки.
        """
        cycle = 1
        text = font.render("ВЫ ПРОШЛИ ИГРУ", 1, (0, 211, 0))
        text2 = font.render(f"ВАША КОНЦОВКА - ", 1, (250, 0, 0))
        text3 = font.render(f"{name}.", 1, (250, 0, 0))
        while cycle:
            self.__screen.fill((0, 0, 0))
            self.__screen.blit(text, (240, 330))
            self.__screen.blit(text2, (70, 380))
            self.__screen.blit(text3, (70, 460))

            pygame.display.flip()

            {sys.exit() for i in pygame.event.get() if i.type == pygame.QUIT}
