"""Торговая система"""

from ..trade.money_system import MoneySystem
from ..other.globals import font3, load
import json
from os import listdir
import pygame
from time import sleep


pygame.init()


class TradeSystem:
    """Торговая система у торговца"""
    
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen = screen
        with open(f"data/data{len(listdir("data/"))}.json") as file:
            self.__result: dict[int: list] = json.load(file)["npc_products"]
        self.__rects_list = []
    
    def draw_items(self) -> None:
        """Отрисовка предметов"""
        x, y = 170, 250
        self.__rects_list.clear()
        for i in self.__result:
            text = font3.render(f"Стоимость - {self.__result[i][0]}",
                            1, (0, 0, 0))
            self.__screen.blit(text, (x, y))
            texture = load(self.__result[i][1], (60, 60), "convert_alpha")
            self.__screen.blit(texture, (x + 250, y - 20))
            self.__rects_list.append(texture.get_rect(topleft=(x + 250,
                                                            y - 20)))
            y += 70
            self.buy_items(i)
    
    def buy_items(self, j: int) -> None:
        """
        Покупка предметов
        
        Args:
            j (int): Ключ из словаря npc_products.
        """
        mp: tuple[int, int] = pygame.mouse.get_pos()
        for i in self.__rects_list:
            if i.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                sleep(0.3)
                pygame.mixer.Sound("textures/collect.mp3").play()
                MoneySystem.change_money(self.__result[j][0])
