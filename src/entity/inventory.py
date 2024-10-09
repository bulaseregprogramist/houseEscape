"""Инвентарь игрока"""

import pygame
import sys
from ..other.globals import font3, some_dict, load
from ..game.logging import HELogger
from ..game.saving import Saving
import re  # Регулярные выражения нужны, чтобы сделать из id текстуру.


pygame.init()


class Inventory:
    inventory_list = []
    logger: HELogger
    Player = None
    inventory_list2 = []
    
    def __init__(self, inventory: pygame.surface.Surface, 
                screen: pygame.surface.Surface) -> None:
        self.__inventory = inventory  # Текстура рюкзака.
        Saving.inventory = self
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
    def draw_inventory(cls, screen: pygame.surface.Surface, il: list) -> None:
        """
        Отрисовка инвентаря
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            il (list): Сохранённые предметы.
        """
        text = font3.render("Enter для выхода из инвентаря", 1, (255, 255, 255))
        x, y = 100, 100
        screen.blit(text, (150, 30))
        if len(cls.inventory_list) > 0:
            for i in range(len(cls.inventory_list)):  # Отрисовка предметов
                if i % 4 == 0 and i != 0:
                    x = 100
                    y += 60
                    
                try:
                    screen.blit(cls.inventory_list[i], (x, y))
                except TypeError:
                    screen.blit(cls.inventory_list[i][0], (x, y))
                x += 60
        if len(il) > 0:
            for j in range(len(il)):  # Отрисовка предметов
                if j % 4 == 0 and j != 0:
                    x = 100
                    y += 60
                screen.blit(il[j], (x, y))
                x += 60

    @classmethod  
    def __num_to_texture(cls, inv_list: list) -> None:
        """
        От id к текстуре
        
        Args:
            inv_list (list): Список с id.
        """
        inv_list2 = []
        for i in inv_list:
            pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

            match = re.search(pattern, some_dict["items"][int(i)][4])
            inv_list2.append(load(match.group(1), (60, 60), "convert_alpha"))
        cls.inventory_list2 = inv_list2
            
    def open(self, index: list[int, int], player: object, n: int) -> None:
        """
        Открытие инвентаря
        
        Args:
            index (list[int, int]): Позиция игрока на карте дома,
            player (Player): Переменная игрока,
            n (int): Номер выбранного сохранения.
        """
        inv_cycle = 1
        save = Saving()
        inventory_list2 = save.load_save(n)["items_id"]
        self.__num_to_texture(inventory_list2)
        while inv_cycle:
            self.__screen.fill((70, 70, 70))
            self.__screen.blit(self.__inventory, (10, 10))
            Inventory.draw_inventory(self.__screen, self.inventory_list2)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save = Saving()
                    save.saving(index, player.x, player.y, n, True)
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    inv_cycle = 0
