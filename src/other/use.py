"""Использование предметов"""

from ..other.globals import load, some_dict
from ..game.saving import Saving
import pygame
import logging
from time import sleep
import re


pygame.init()


class Use:
    """Кнопка использования"""
    save = Saving()
    
    def __init__(self, screen: pygame.surface.Surface, n: int,
                player: object) -> None:
        self.__screen = screen
        self.__player = player
        self.__visible = 0
        self.__keys = self.save.load_save(n)["items_id"]
        self.__some_list = []
        self.__rects_list = []
        self.__from_num_to_texture()
        self.__button = load("textures/act.png", (70, 70), "convert_alpha")
        self.__button2 = load('textures/act2.png', (70, 70), "convert_alpha")
        self.__slot = load("textures/menu.png", (21, 21), "convert")
        self.__slot2 = load("textures/menu2.png", (21, 21), "convert")
        self.__slot.set_alpha(96)
        
    def __from_num_to_texture(self) -> None:
        """
        От id к текстуре
        """
        logging.debug("Начало работы метода __from_num_to_texture")
        inv_list2 = []
        for i in self.__keys:
            pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

            match = re.search(pattern, some_dict["items"][int(i)][4])
            inv_list2.append(
                [load(match.group(1), (60, 60), "convert_alpha"), i])
        self.__some_list.extend(inv_list2)
        logging.debug("Конец работы метода __from_num_to_texture")
        
    def __draw_inventory_slots(self) -> None:
        """Отрисовка инвентаря"""
        x, y = 605, 75
        self.__rects_list.clear()
        for i in range(self.__player.MAX_CAPACITY):
            if i % 8 == 0 and i != 0:
                y += 21
                x = 605
            self.__screen.blit(self.__slot, (x, y))
            
            try:
                texture = pygame.transform.scale(self.__some_list[i][0],
                                                (20, 20))
                self.__screen.blit(texture, (x + 2, y))
                self.__rects_list.append(
                    [texture.get_rect(topleft=(x + 2, y)), texture])
            except IndexError:
                pass
            x += 21
        self.__after_click()
    
    def draw(self, pos: tuple[int, int]) -> None:
        """
        Отрисовка
        
        Args:
            pos (tuple[int, int]): Позиция мыши
        """
        self.__screen.blit(self.__button, (700, 0))
        rect = self.__button.get_rect(topleft=(700, 0))
        
        if rect.collidepoint(pos):
            self.__screen.blit(self.__button2, (700, 0))
            if pygame.mouse.get_pressed()[0]:
                sleep(0.12)
                if not self.__visible:
                    self.__visible = 1
                else:
                    self.__visible = 0
        if self.__visible:
            self.__draw_inventory_slots()
    
    def __after_click(self) -> None:
        """Функционал"""
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        for i in self.__rects_list:
            if i[0].collidepoint(mouse_pos):
                self.__screen.blit(self.__slot2, (i[0][0], i[0][1]))
                self.__screen.blit(i[1], (i[0][0], i[0][1]))
                if pygame.mouse.get_pressed()[0]:
                    pass
    
    