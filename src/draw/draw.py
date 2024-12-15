"""Отрисовка комнат"""

import pygame
from ..other.globals import font, load
from ..entity.npc import NPC
from ..entity.player import Player
from ..game.logging import HELogger
from ..entity.enemys import Enemy
from ..game.saving import Saving
from ..draw.basement import Basement
from ..draw.cherdak import Cherdak
from ..entity.endings import Endings
from .other_functional.other_functional import OtherFunctional
from ..draw.crafting_table import CraftingTable


pygame.init()


class Draw:
    """Этот класс отвечает за отрисовку локаций и другого"""
    
    def __init__(self, screen, logger: HELogger) -> None:
        self.__logger = logger
        logger.info("Работа конструктора класса Draw начата!")
        self.__bg1 = load("textures/1.png", (770, 770), "convert")
        self.__bg2 = load("textures/2.png", (770, 770), "convert")
        self.__bg3 = load("textures/3.png", (770, 770), "convert")
        self.__bg4 = load("textures/4.png", (770, 770), "convert")
        self.__bg5 = load("textures/5.png", (770, 770), "convert")
        self.__bg6 = load("textures/6.png", (770, 770), "convert")
        self.__bg7 = load("textures/7.png", (770, 770), "convert")
        self.__bg8 = load("textures/8.png", (770, 770), "convert")
        self.__bg9 = load("textures/9.png", (770, 770), "convert")
        self.__bg10 = load("textures/house.png", (770, 770), "convert")
        self.__x = Enemy.enemy_dict['1'][0]
        self.__y = Enemy.enemy_dict['1'][1]
        
        self.__x2 = Enemy.enemy_dict['2'][0]
        self.__y2 = Enemy.enemy_dict['2'][1]
        
        self.__x3 = Enemy.enemy_dict['3'][0]
        self.__y3 = Enemy.enemy_dict['3'][1]
        logger.info("Работа конструктора класса Draw завершена!")
        
    @staticmethod
    def show_interfaces(*args) -> None:
        """
        Интерфейсы для мебели
        
        Args:
            *args (tuple): Параметры для интерфейса
        """
        text = font.render("СОЗДАНИЕ ПРЕДМЕТА", 1, (0, 0, 0))
        pygame.mixer.Sound("textures/collect.mp3").play()
        of = OtherFunctional(args[2], args[1], args[3], args[4], args[5])
        key = int(args[0])
        save = Saving()
        result: dict[int: list] = save.load_save(args[2])["blocks"]
        
        if key == 1:  # Верстак
            CraftingTable(args[1], text, args[2], args[3], args[4])
        elif key == 2:  # Лампа
            of.lamp(args[6])
        elif key == 3:  # Люк в подвал
            logger = HELogger("BASEMENT", "INFO")
            logger.getChild("HE")
            Basement(args[5], args[1], args[2])
        elif key == 4:  # Кровать
            of.bed(args[6])
        elif key == 5:  # Чердак (лестница)
            logger = HELogger("CHERDAK", "INFO")
            logger.getChild("HE")
            Cherdak(logger, args[1], args[2])
        elif key == 6:  # Шкаф
            of.closet(args[6])
        elif key == 7 and "exit3.png" in result['7'][4]:
            endings = Endings(args[1])
            endings.pre_ending("Концовка Решётки")
    
    def render_location(self, index: list[int, int], mp: tuple[int, int],
                    screen: pygame.surface.Surface, player: Player,
                    num: int, logger: HELogger) -> None:
        """
        Рендеринг комнаты дома

        Args:
            index (list[int, int]): Карта дома,
            mp (tuple[int, int]): Позиция мыши,
            screen (pygame.surface.Surface): Переменная экрана,
            player (Player): Объект игрока,
            num (int): Номер выбранного сохранения,
            logger (HELogger): Переменная для логов.
        """
        if index == [0, 2]:
            screen.blit(self.__bg10, (0, 0))
        elif index == [1, 1]:
            screen.blit(self.__bg2, (0, 0))
            enemy = Enemy(self.__x2, self.__y2, "stalker", logger, 
                        screen, player)
            self.__x2, self.__y2 = enemy.enemy_draw_and_move(player, mp, num)
        elif index == [1, 2]:
            screen.blit(self.__bg3, (0, 0))
            enemy = Enemy(self.__x3, self.__y3, "blinder", logger, screen)
            self.__x3, self.__y3 = enemy.enemy_draw_and_move(player, mp, num)
        elif index == [1, 3]:
            screen.blit(self.__bg4, (0, 0))
        elif index == [2, 1]:
            screen.blit(self.__bg5, (0, 0))
        elif index == [2, 2]:
            screen.blit(self.__bg6, (0, 0))
            npc = NPC(screen, self.__logger, index, num)
            npc.placing(mp, player, index, num)
        elif index == [2, 3]:
            screen.blit(self.__bg7, (0, 0))
        elif index == [3, 1]:
            screen.blit(self.__bg8, (0, 0))
        elif index == [3, 2]:
            screen.blit(self.__bg9, (0, 0))
        elif index == [3, 3]:  # Окрестности дома
            screen.blit(self.__bg1, (0, 0))
            enemy = Enemy(self.__x, self.__y, "watcher", logger, screen)
            self.__x, self.__y = enemy.enemy_draw_and_move(player, mp, num)
        