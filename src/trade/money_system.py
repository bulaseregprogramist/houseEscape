"""Денежная система"""

import json
from ..other.globals import load  # Загрузка текстур
from ..game.saving import Saving
from time import sleep
import pygame


pygame.init()


class MoneySystem:
    MONEY = 0
    
    def __init__(self, num: int, screen: pygame.surface.Surface) -> None:
        self.__num = num
        self.__change_dict = 0
        self.__screen: pygame.surface.Surface = screen
        save = Saving()
        self.change_money(-save.load_save(num)["MON"])
        self.__money: pygame.surface.Surface = load("textures/money.png", 
                                                (60, 60), "convert_alpha")
        with open(f"data/data{num}.json") as file:
            self.__res: dict[int: list[int, ...]] = json.load(file)["money"]
    
    @classmethod
    def change_money(cls, money: int) -> None:
        """
        Изменение кол-ва денег
        
        Args:
            money (int): Потраченные деньги
        """
        if cls.MONEY - money > 0:  # Если хватает денег
            cls.MONEY -= money  # Минус используется и так: -(-50) = +50
            
    def save_moneys(self) -> None:
        """Сохранение денег"""
        with open(f"data/data{self.__num}.json") as file:
            res2: dict[int: list[int, ...]] = json.load(file)
        res2["money"] = self.__res  # Расположение денег в комнатах
        res2["MON"] = self.MONEY  # Игровая валюта
        with open(f"data/data{self.__num}.json", "w") as file:
            json.dump(res2, file, indent=2)
            
    def placing_money(self, index: list[int, int], 
                    mouse_pos: tuple[int, int]) -> None:
        """
        Отрисовка денег на карте
        
        Args:
            index (list[int, int]): Позиция игрока на карте,
            mouse_pos (tuple[int, int]): Позиция курсора мыши
        """
        for i in self.__res:  # Список с расположением денег
            try:
                if (self.__res[i][2] == index[0]  # Если в комнате с деньгами
                        and self.__res[i][3] == index[1]):
                    self.__screen.blit(self.__money, (self.__res[i][0],
                                                self.__res[i][1]))
                    rect = self.__money.get_rect(topleft=(self.__res[i][0],
                                                    self.__res[i][1]))
                    if (rect.collidepoint(mouse_pos)  # Сбор при нажатии ЛКМ
                            and pygame.mouse.get_pressed()[0]):
                        sleep(0.135789043124)
                        pygame.mixer.Sound("textures/press.mp3").play()
                        self.change_money(-self.__res[i][4])
                        self.__change_dict = 1
                        break
            except KeyError:
                pass
        if self.__change_dict:  # Удаление, если деньги получены
            self.__change_dict = 0
            self.__res.pop(i)  # Удаление денег в том месте
            self.save_moneys()
                    
