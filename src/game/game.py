"""Этот файл включает в себя основной функционал игры"""

import pygame
from src.entity.player import Player
from src.draw.draw import Draw
from src.draw.mainmenu import MainMenu
from .logging import HELogger
import logging
from src.draw.crafting_table import CraftingTable
from src.gameobjects.blocks import Block
from src.gameobjects.item import Item
from src.gameobjects.gameobjects import GameObjects
from src.gameobjects.pictures import Pictures
from src.other.globals import traps_dict
from src.game.saving import Saving
from src.traps.traps import Traps
from src.api.api import HEAPI
from src.draw.pause import Pause
from keyboard import is_pressed
from ..entity.inventory import Inventory


pygame.init()


class Game:
    """Основной игровой класс"""
    # Карта дома (1 - комнаты, 0 - комнаты, в которые нельзя попасть)
    __lst = ["00100", "01110","01110", "01110", "00000"]
    
    def __init__(self, logger: HELogger) -> None:
        logging.basicConfig(level=logging.DEBUG,
            format="[%(name)s] - [%(levelname)s] [%(asctime)s] - %(message)s",
            encoding="utf-8")
        # Цвета для логов (их можно включить указав BETTER в консоли)
        # Или изменение уровня логов.
        HELogger.better_info(logger)
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
        logger.info("Главное меню открыто!")
        self.__numb: int = MainMenu.render(self.__screen, logger)
        logger.info("Главное меню закрыто!")
        self.__player = Player(logger, self.__screen, self.__numb)
        logger.debug("Создание объекта класса Player")
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
        Saving.inventory = Inventory
        logger.debug("Статичному полю Saving inventory присвоено значение")
        save = Saving()
        logger.debug("Создание объекта класса Saving")
        # Положение игрока на карте. 1 - по y, 2 - по x.
        self.__index: list[int, int] = save.load_save(
            self.__numb, logger)["index"]
        logger.debug("Получен список index")
        Block.screen = self.__screen
        logger.debug("Переменной screen класса Block присвоено значение")
        self.__blocks = Block()  # Это не блоки, а мебель
        logger.debug("Создание объекта класса Block")
        self.__items = Item()  # Предметы (их можно подбирать и использовать)
        logger.debug("Создание объекта класса Item")
        GameObjects.screen = self.__screen
        logger.debug("Статичному полю GameObjects screen присвоено значение")
        GameObjects.logger = logger
        logger.debug("Статичному полю GameObjects logger присвоено значение")
        CraftingTable.logger = logger
        logger.debug("Статичному полю CraftingTable logger присвоено значение")
        self.__traps = Traps(self.__screen)
        logger.debug("Создание объекта класса Traps")
        self.__pictures = Pictures()  # Картины с котами
        logger.debug("Создание объекта класса Pictures")
        Inventory.logger = logger
        logger.info("Закончена инициализация перед работой в цикле")
        
    def __start(self, logger: HELogger) -> None:
        """
        Запуск игры
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        self.__load(logger)
        cycle = 1
        logger.debug("Переменной cycle присвоен 1")
        
        while 1:
            while cycle:  # Основной игровой цикл
                self.__clock.tick(60)  # Вертикальная синхронизация
                self.__screen.fill((0, 0, 0))
                mp: tuple[int, int] = pygame.mouse.get_pos()
                self.__draw_location.render_location(self.__index, mp,
                                    self.__screen, self.__player)
                result: pygame.surface.Surface = self.__player.blit(mp)
                rect, rect2 = self.__player.player_interfaces(
                    self.__screen, self.__player, mp)
                self.__blocks.placing(self.__index, self.__player,
                                    self.__numb)
                self.__items.placing(self.__index, self.__player,
                                    self.__numb)
                self.__pictures.placing(self.__index, self.__player,
                                        self.__numb, self.__screen)
            
                for j in traps_dict:  # Отрисовка ловушек
                    if (traps_dict[j][2] == self.__index[0]
                            and traps_dict[j][3] == self.__index[1]):
                        trap_rect = self.__traps.draw_trap(traps_dict[j][0],
                                    traps_dict[j][1], traps_dict[j][4])
                        self.__traps.after(trap_rect, traps_dict[j][4], rect2)
            
                self.__player.in_game(self.__player,  # Движение игрока
                        self.__index, logger, rect, self.__numb, mp)
                self.__check(logger)  # Проверка на выход за границу
                pygame.display.flip()
                # Информация об игроке
                if result.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                    self.__player.get_stats(logger, self.__index, self.__numb)
                if is_pressed("esc"):
                    # При нажатии на ESCAPE игра поставится на паузу
                    pause = Pause(self.__screen, logger, self.__index,
                            self.__player, self.__numb)
                    cycle: int = pause.run()
            cycle = 1
            self.__numb: int = MainMenu.render(self.__screen, logger)
            
    def __check(self, logger: HELogger) -> None:
        """
        Проверка на выход за границу карты дома.
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        if self.__player.x < 0:  # При выходе налево
            self.__check2(logger, self.__index[0], self.__index[1] - 1, 1, 1)
        elif self.__player.y < 0:  # При выходе вверх
            self.__check2(logger, self.__index[0] - 1, self.__index[1], 0, 1)
        elif self.__player.x > 751:  # При выходе направо
            self.__check2(logger, self.__index[0], self.__index[1] + 1, 1, -1)
        elif self.__player.y > 770:  # При выходе вниз
            self.__check2(logger, self.__index[0] + 1, self.__index[1], 0, -1)
                
    def __check2(self, logger: HELogger, n1: int, n2: int,
                index: int, n: int) -> None:
        """Проверка на выход за границу карты дома (вторая часть)"""
        if self.__lst[n1][n2] != "0":
            logger.info("Игрок вышел налево")
            self.__player.x, self.__player.y = 385, 385
            logger.debug("Переменным x и y присвоены стандартные значения")
            self.__index[index] -= n
