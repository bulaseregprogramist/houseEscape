"""Торговая система"""

from ..trade.money_system import MoneySystem
from ..other.globals import font3, load
from ..entity.inventory import Inventory
import json
from os import listdir
import pygame
from time import sleep
from copy import copy
import logging


pygame.init()


class TradeSystem:
    """Торговая система у торговца"""
    
    def __init__(self, screen: pygame.surface.Surface, num: int) -> None:
        self.__screen = screen
        self.change_dict = 0
        self.__num = num
        with open(f"data/data{len(listdir("data/"))}.json") as file:
            self.__result: dict[int: list] = json.load(file)
        self.__rects_list = []
    
    def draw_items(self) -> None:
        """Отрисовка предметов"""
        x, y = 170, 250
        self.__rects_list.clear()
        i = 0
        for i in self.__result["npc_products"]:
            text = font3.render(f"Стоимость - {self.__result[
                "npc_products"][i][0]}",
                            1, (0, 0, 0))
            self.__screen.blit(text, (x, y))
            texture = load(self.__result["npc_products"][i][1], (60, 60), 
                        "convert_alpha")
            self.__screen.blit(texture, (x + 250, y - 20))
            self.__rects_list.append(texture.get_rect(topleft=(x + 250,
                                                            y - 20)))
            y += 70
            self.change_dict: int = self.buy_items(i)
            if self.change_dict:
                break
        if self.change_dict:  # Чтобы избежать ошибки Runtime
            try:
                self.__result.pop(i)
            except KeyError:
                pass
            self.change_keys()
            
    def change_keys(self) -> None:
        """
        Измение ключей, если предмет был куплен.
        """
        with open(f"data/data{self.__num}.json") as file:
            res: dict = json.load(file)
        res["npc_products"] = copy(self.__result["npc_products"])
        res["MON"] = MoneySystem.MONEY
        with open(f"data/data{self.__num}.json", "w") as file:
            json.dump(res, file)
    
    def buy_items(self, j: int) -> int:
        """
        Покупка предметов
        
        Args:
            j (int): Ключ из словаря npc_products.
        Returns:
            int: Удаление ключа из слоавря предметов магазина
        """
        mp: tuple[int, int] = pygame.mouse.get_pos()
        for i in self.__rects_list:  # 'Квадраты' предметов
            if i.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                logging.info("Предмет был куплен!")
                sleep(0.3)
                pygame.mixer.Sound("textures/collect.mp3").play()
                MoneySystem.change_money(self.__result["npc_products"][j][0])
                
                try:
                    Inventory.append(
                        load(self.__result["items"][str(int(j) + 6)][5],
                        (60, 60), "convert_alpha"), int(j) + 6)
                except IndexError:
                    pass
                return 1
        return 0
                
