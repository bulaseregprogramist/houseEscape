"""Инвентарь игрока"""

import pygame
import sys
from ..other.globals import font3
from ..game.logging import HELogger
from ..game.saving import Saving


pygame.init()


class Inventory:
    inventory_list = []
    logger: HELogger
    Player = None
    
    def __init__(self, inventory: pygame.surface.Surface, 
                screen: pygame.surface.Surface) -> None:
        self.__inventory = inventory
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
    def draw_inventory(cls, screen: pygame.surface.Surface) -> None:
        """
        Отрисовка инвентаря
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана
        """
        text = font3.render("Enter для выхода из инвентаря", 1, (255, 255, 255))
        x, y = 100, 100
        screen.blit(text, (150, 30))
        for i in range(len(cls.inventory_list)):  # Отрисовка предметов
            if i % 4 == 0:
                x = 100
                y += 60
            screen.blit(cls.inventory_list[i][0], (x, y))
            x += 60
            
    def open(self, index: list[int, int], player: object, n: int) -> None:
        """
        Открытие инвентаря
        
        Args:
            index (list[int, int]): Позиция игрока на карте дома,
            player (Player): Переменная игрока,
            n (int): Номер выбранного сохранения.
        """
        inv_cycle = 1
        while inv_cycle:
            self.__screen.fill((70, 70, 70))
            self.__screen.blit(self.__inventory, (10, 10))
            Inventory.draw_inventory(self.__screen)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save = Saving()
                    save.saving(index, player.x, player.y, n, True)
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        inv_cycle = 0
