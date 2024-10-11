"""Отрисовка комнат"""

import pygame
from ..other.globals import font, load
from ..game.logging import HELogger
from ..entity.enemys import Enemy
from ..draw.basement import Basement
from ..draw.crafting_table import CraftingTable


pygame.init()


class Draw:
    """Этот класс отвечает за отрисовку локаций и другого"""
    
    def __init__(self, logger: HELogger) -> None:
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
        logger.info("Работа конструктора класса Draw завершена!")
        
    @staticmethod
    def show_interfaces(key: int, screen: pygame.surface.Surface, 
                        n: int) -> None:
        """
        Интерфейсы для мебели
        
        Args:
            key (int): id мебели,
            screen (pygame.surface.Surface): Переменная для экрана,
            n (int): Номер выбранного сохранения.
        """
        text = font.render("СОЗДАНИЕ ПРЕДМЕТА", 1, (0, 0, 0))
        pygame.mixer.Sound("textures/collect.mp3").play()
        key = int(key)
        if key == 1:  # Верстак
            CraftingTable(screen, text, n)
        elif key == 2:  # Лампа
            pass
        elif key == 3:  # Люк в подвал
            Basement()
        elif key == 4:  # Кровать
            pass
    
    def render_location(self, index: list[int, int],
                        screen: pygame.surface.Surface) -> None:
        """
        Рендеринг комнаты дома

        Args:
            index (list[int, int]): Карта дома,
            screen (pygame.surface.Surface): Переменная экрана
        """
        if index == [0, 2]:
            screen.blit(self.__bg10, (0, 0))
        elif index == [1, 1]:
            screen.blit(self.__bg2, (0, 0))
        elif index == [1, 2]:
            screen.blit(self.__bg3, (0, 0))
        elif index == [1, 3]:
            screen.blit(self.__bg4, (0, 0))
        elif index == [2, 1]:
            screen.blit(self.__bg5, (0, 0))
        elif index == [2, 2]:
            screen.blit(self.__bg6, (0, 0))
        elif index == [2, 3]:
            screen.blit(self.__bg7, (0, 0))
        elif index == [3, 1]:
            screen.blit(self.__bg8, (0, 0))
        elif index == [3, 2]:
            screen.blit(self.__bg9, (0, 0))
        elif index == [3, 3]:  # Окрестности дома
            screen.blit(self.__bg1, (0, 0))
            Enemy(Enemy.enemy_dict['1'][0],
                    Enemy.enemy_dict['1'][1], "watcher", screen)
        