"""Инвентарь игрока"""

import pygame
import sys
from typing import Self
from ..other.globals import font3, some_dict, load
from ..game.logging import HELogger
from ..game.saving import Saving
from ..trade.money_system import MoneySystem
import re  # Регулярные выражения нужны, чтобы сделать из id текстуру.


pygame.init()


class Inventory:
    inventory_list = []  # Не сохранённые предметы
    logger: HELogger
    Player = None
    inventory_list2 = []  # Сохранённые предметы
    
    def __init__(self, inventory: pygame.surface.Surface, 
                screen: pygame.surface.Surface) -> None:
        self.__inventory = inventory  # Текстура рюкзака.
        self.__screen = screen
        
    @classmethod
    def append(cls, texture: pygame.surface.Surface, key: str) -> None:
        """
        Добавление в инвентарь предметов
        
        Args:
            texture (pygame.surface.Surface): Текстура предмета,
            key (str): Ключ словаря предмета.
        """
        try:
            if cls.Player.MAX_CAPACITY > len(cls.inventory_list):
                cls.inventory_list.append([texture, key])
                cls.logger.debug("Предмет успешно добавлен!")
            else:
                cls.logger.error("В инвентаре нет места!")
        except AttributeError:
            cls.logger.critical("Инвентарь не инициализирован!!")

    @classmethod   
    def draw_inventory(cls, screen: pygame.surface.Surface) -> None:
        """
        Отрисовка инвентаря
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана
        """
        text = font3.render("Enter для выхода из инвентаря", 1, 
                            (255, 255, 255))
        x, y = 100, 100
        screen.blit(text, (150, 30))
        if len(cls.inventory_list) > 0:  # Сохранённые предметы
            for i in range(len(cls.inventory_list)):  # Отрисовка предметов
                if i % 8 == 0 and i != 0:
                    x = 100
                    y += 60
                    
                try:
                    screen.blit(cls.inventory_list[i], (x, y))
                except TypeError:
                    screen.blit(cls.inventory_list[i][0], (x, y))
                x += 60
        if len(cls.inventory_list2) > 0:  # Отрисовка не сохранённых предметов
            for j in range(len(cls.inventory_list2)):  # Отрисовка предметов
                if j % 8 == 0 and j != 0:
                    x = 100
                    y += 60
                screen.blit(cls.inventory_list2[j], (x, y))
                x += 60

    @classmethod  
    def __num_to_texture(cls, inv_list: list[str, ...]) -> None:
        """
        От id к текстуре
        
        Args:
            inv_list (list[str, ...]): Список с id.
        """
        inv_list2 = []
        for i in inv_list:
            pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

            match = re.search(pattern, some_dict["items"][int(i)][4])
            inv_list2.append(load(match.group(1), (60, 60), "convert_alpha"))
        cls.inventory_list2 = inv_list2
            
    def open(self, index: list[int, int], player: Self, n: int,
            logger: HELogger) -> None:
        """
        Открытие инвентаря
        
        Args:
            index (list[int, int]): Позиция игрока на карте дома,
            player (Player): Переменная игрока,
            n (int): Номер выбранного сохранения,
            logger (HELogger): Переменная для логов.
        """
        inv_cycle = 1
        save = Saving()
        inventory_list2: list[str, ...] = save.load_save(n)["items_id"]
        self.__num_to_texture(inventory_list2)
        text = font3.render(f"Деньги - {MoneySystem.MONEY}", 1,
                            (0, 0, 0))
        while inv_cycle:
            self.__screen.fill((70, 70, 70))
            self.__screen.blit(self.__inventory, (10, 10))
            self.__screen.blit(text, (110, 7))
            Inventory.draw_inventory(self.__screen)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save = Saving()
                    save.saving(index, player.x, player.y, n, True)
                    logger.info("Выход из игры...")
                    sys.exit()
                elif (event.type == pygame.KEYDOWN
                        and event.key == pygame.K_RETURN):
                    inv_cycle = 0
