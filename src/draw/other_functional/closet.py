"""Шкаф"""

import pygame
import json
import logging
from ...entity.inventory import Inventory
from ...other.globals import font, some_dict, load
from copy import copy
import re
from ...other.use import Use
import sys  # Только для sys.exit()


pygame.init()


class Closet:
    """Функционал шкафа"""
    
    def __init__(self, screen: pygame.surface.Surface, save,
                num: int, player, index: list[int, int]) -> None:
        self.__num = num
        self.__text = font.render("Шкаф", 1, (0, 0, 0))
        self.__text2 = font.render("Инвентарь:", 1, (0, 0, 0))
        self.__sword2 = load("textures/sword2.png", (60, 60), "convert_alpha")
        self.__axe2 = load("textures/axe2.png", (60, 60), "convert_alpha")
        self.__save = save
        self.__x, self.__y = 230, 230
        self.__player = player
        self.__index: list[int, int] = index
        self.__items_rects_list = []
        self.__screen: pygame.surface.Surface = screen
        
    def to_texture(self, i: str) -> pygame.surface.Surface:
        """
        Возвращает текстуру из словаря items словаря some_dict.
        
        Args:
            i (str): Ключ словаря
        Returns:
            pygame.surface.Surface: Загруженная для шкафа текстура.
        """
        pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

        match = re.search(pattern, some_dict["items"][int(i)][4])
        texture = load(match.group(1), (60, 60), "convert_alpha")
        return texture
    
    def __draw_closet(self, items: list[str, ...]) -> None:
        """
        Отрисовка предметов в шкафе
        
        Args:
            items (list[str, ...]): Предметы шкафа.
        """
        lst = copy(Inventory.inventory_list)
        lst.extend(Inventory.inventory_list2)
        pygame.draw.rect(self.__screen, (235, 255, 245),
                            (150, 150, 470, 470))
        self.__screen.blit(self.__text, (330, 170))
            
        self.__items_rects_list.clear()

        for i in items:  # Отрисовка предметов шкафа
            texture = self.to_texture(i)
            self.__screen.blit(texture, 
                            (self.__x, self.__y))
            self.__items_rects_list.append([
                texture.get_rect(topleft=(self.__x, self.__y)),
                i])
            self.__x += 60
        self.__x, self.__y = 180, 490
        self.__screen.blit(self.__text2, (255, 450))
        for i in lst:
            try:
                self.__screen.blit(i[0], (self.__x, self.__y))
            except TypeError:  # Чтобы убрать баг
                self.__screen.blit(i, (self.__x, self.__y))
                
            self.__x += 60
        self.__x, self.__y = 230, 230
    
    def run(self, use) -> None:
        """Основной метод класса"""
        with open(f"data/data{self.__num}.json") as file:
            result: dict[str: list | dict | int] = json.load(file)
        items: list[str, ...] = result["closet_items"]
        
        closet_cycle = 1
        while closet_cycle:
            self.__draw_closet(items)
            mouse_position: tuple[int, int] = pygame.mouse.get_pos()
            
            for j in range(len(self.__items_rects_list)):  # Взятие предмета
                if ((self.__items_rects_list[j][0].collidepoint(
                        mouse_position))):
                    if self.__items_rects_list[j][1] == "12":  # Меч
                        self.__screen.blit(self.__sword2, (230, 230))
                    elif self.__items_rects_list[j][1] == "13":  # Топор
                        self.__screen.blit(self.__axe2, (290, 230))
                    
                    if pygame.mouse.get_pressed()[0]:
                        
                        Inventory.append(self.to_texture(items[int(j)]),
                                        str(int(j) + 12))
                        dict_id: str = str(int(j) + 12)
                        sl = [{dict_id: self.to_texture(items[int(j)])}]
                        use.append(sl)
                        items.pop(j)
                        self.__save.save_closet_items(items, self.__num,
                                                    result)
            
            pygame.display.flip()   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Выход из игры...")
                    self.__save.saving(self.__index, 
                                self.__player.x, self.__player.y,
                                self.__num, True)
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    closet_cycle = 0