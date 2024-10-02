"""Этот файл включает в себя основной функционал игры"""

import pygame
from src.player.player import Player
from src.draw.draw import Draw
from src.draw.mainmenu import MainMenu
from .logging import HELogger
import logging
from src.gameobjects.blocks import Block
from src.gameobjects.item import Item
from src.gameobjects.gameobjects import GameObjects
from src.game.saving import Saving
from src.traps.traps import Traps
from src.api.api import HEAPI
from src.draw.pause import Pause
from keyboard import is_pressed
from ..player.inventory import Inventory


pygame.init()


class Game:
    """Основной игровой класс"""
    
    __lst = ["00100",  # Карта дома (1 - комнаты, 0 - комнаты, в которые нельзя попасть)
            "01110",
            "01110",
            "01110",
            "00000"]
    
    def __init__(self, logger: HELogger) -> None:
        logging.basicConfig(level=logging.DEBUG,
                            format="[%(name)s] - [%(levelname)s] - %(message)s",
                            encoding="utf-8")
        HELogger.better_info(logger)  # Цвета для логов (их можно включить указав BETTER в консоли)
        logger.info("Запуск программы")
        self.__screen = pygame.display.set_mode((770, 770))
        logger.debug("Создание переменной для экрана")
        logger.debug("Создание переменной карты")
        self.__clock = pygame.time.Clock()
        logger.debug("Создание объекта класса pygame.time.Clock")
        pygame.display.set_caption("House Escape")
        pygame.display.set_icon(pygame.image.load("textures/exit.png"))
        logger.debug("Установлено название и иконка")
        logger.info("Начата инициализация модов")
        HEAPI.load(logger)
        logger.info("Завершена инициализация модов")
        self.__player = Player(logger, self.__screen)
        logger.debug("Создание объекта класса Player")
        logger.info("Главное меню открыто!")
        MainMenu.render(self.__screen, logger)
        logger.info("Главное меню закрыто!")
        self.__start(logger)
        
    def __load(self, logger: HELogger) -> None:
        """
        Инициализация переменных
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        logger.info("Начата инициализация перед работой в цикле")
        self.__draw_location = Draw(logger)
        logger.debug("Создание объекта класса Draw")
        save = Saving()
        logger.debug("Создание объекта класса Saving")
        self.__index = save.load_save()["index"]  # Положение игрока на карте. 1 - по y, 2 - по x.
        logger.debug("Получен список index")
        self.__blocks = Block()  # Это не блоки, а мебель
        logger.debug("Создание объекта класса Block")
        self.__items = Item()  # Предметы игры (их можно подбирать и использовать)
        logger.debug("Создание объекта класса Item")
        GameObjects.screen = self.__screen
        logger.debug("Статичному полю GameObjects screen присвоено значение")
        GameObjects.logger = logger
        traps = Traps(self.__screen)
        logger.debug("Создание объекта класса Traps")
        Inventory.logger = logger
        logger.info("Закончена инициализация перед работой в цикле")
        
    def __start(self, logger: HELogger) -> None:
        """
        Запуск игры
        
        Args:
            logger (HELogger): Переменная для логов
        """
        self.__load(logger)
        cycle = 1
        logger.debug("Переменной cycle присвоен 1")
        
        while cycle:  # Основной игровой цикл
            self.__clock.tick(60)  # Вертикальная синхронизация
            self.__screen.fill((0, 0, 0))
            self.__draw_location.render_location(self.__index, self.__screen)
            result: pygame.surface.Surface = self.__player.blit()
            rect: pygame.surface.Surface = self.__player.player_interfaces(
                self.__screen, self.__player)
            self.__blocks.placing(self.__index, self.__player)
            self.__items.placing(self.__index, self.__player)
            pygame.display.flip()
            mp: tuple[int, int] = pygame.mouse.get_pos()
            
            self.__player.in_game(self.__player, self.__index, logger, rect)  # Движение игрока
            self.__check(logger)
            
            if result.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                self.__player.get_stats(logger)
            if is_pressed("esc"):  # При нажатии на ESCAPE игра поставится на паузу
                Pause(self.__screen, logger, self.__index, self.__player)
            
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
                logger.debug("Переменным x и y присвоены стандартные значения")
                self.__index[1] -= 1
        elif self.__player.y < 0:  # При выходе вверх
            if self.__lst[self.__index[0]][self.__index[0] - 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел вверх")
                self.__player.x = 385
                self.__player.y = 385
                logger.debug("Переменным x и y присвоены стандартные значения")
                self.__index[0] -= 1
        elif self.__player.x > 770:  # При выходе направо
            if self.__lst[self.__index[0]][self.__index[1] + 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел направо")
                self.__player.x = 385
                self.__player.y = 385
                logger.debug("Переменным x и y присвоены стандартные значения")
                self.__index[1] += 1
        elif self.__player.y > 770:  # При выходе вниз
            if self.__lst[self.__index[0]][self.__index[0] + 1] != "0":  # Проверка на выход за границу дома
                logger.info("Игрок вышел вниз")
                self.__player.x = 385
                self.__player.y = 385
                logger.debug("Переменным x и y присвоены стандартные значения")
                self.__index[0] += 1
