"""Этот файл включает в себя основной функционал игры"""

import pygame
from src.player.player import Player
from src.draw.draw import Draw
from src.draw.mainmenu import MainMenu
from .logging import HELogger
import logging
from src.gameobjects.blocks import Block
from src.gameobjects.item import Item


pygame.init()


class Game:
    """Основной игровой класс"""
    
    __lst = ["00100",  # Карта дома
            "01110",
            "01110",
            "01110",
            "00000"]
    
    def __init__(self, logger: HELogger) -> None:
        logger.info("Запуск программы")
        self.__screen = pygame.display.set_mode((770, 770))
        self.__index = [3, 3]  # Положение игрока на карте. 1 - по y, 2 - по x.
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption("House Escape")
        pygame.display.set_icon(pygame.image.load("textures/exit.png"))
        self.__player = Player()
        
        logging.basicConfig(level=logging.INFO, format="[%(name)s] - [%(levelname)s] - %(message)s", encoding="utf-8")
        logger.info("Главное меню открыто!")
        MainMenu.render(self.__screen, logger)
        logger.info("Главное меню закрыто!")
        self.__start(logger)
        
    def __start(self, logger: HELogger) -> None:
        """
        Запуск игры
        
        Args:
            logger (HELogger): Переменная для логов
        """
        logger.info("Начата инициализация перед работой в цикле")
        cycle = 1
        draw_location = Draw(logger)
        blocks = Block()
        items = Item()
        logger.info("Закончена инициализация перед работой в цикле")
        
        while cycle:  # Основной игровой цикл
            self.__clock.tick(60)
            self.__screen.fill((0, 0, 0))
            draw_location.render_location(self.__index, self.__screen)
            self.__screen.blit(self.__player.player, (self.__player.x, self.__player.y))
            pygame.display.flip()
            
            self.__player.in_game(self.__player, self.__index, logger)    
            self.__check(logger)
            
    def __check(self, logger: HELogger) -> None:
        """
        Проверка на выход за границу
        
        Args:
            logger (HELogger): Переменная для логов
        """
        if self.__player.x < 0:  # При выходе налево
            if self.__lst[self.__index[0]][self.__index[1] - 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел налево")
                self.__player.x = 385
                self.__player.y = 385
                self.__index[1] -= 1
        elif self.__player.y < 0:  # При выходе вверх
            if self.__lst[self.__index[0]][self.__index[0] - 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел вверх")
                self.__player.x = 385
                self.__player.y = 385
                self.__index[0] -= 1
        elif self.__player.x > 770:  # При выходе направо
            if self.__lst[self.__index[0]][self.__index[1] + 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел направо")
                self.__player.x = 385
                self.__player.y = 385
                self.__index[1] += 1
        elif self.__player.y > 770:  # При выходе вниз
            if self.__lst[self.__index[0]][self.__index[0] + 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел вниз")
                self.__player.x = 385
                self.__player.y = 385
                self.__index[0] += 1    
