"""Использование предметов"""

from ..other.globals import load, some_dict
from ..game.saving import Saving
import pygame
import logging
from time import sleep
from ..entity.inventory import Inventory
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
        self.__keys: list[str, ...] = self.save.load_save(n)["items_id"]
        self.__some_list = []
        self.__rects_list = []
        self.__item_visible = 0
        self.to_dict()
        self.__button = load("textures/act.png", (70, 70), "convert_alpha")
        self.__button2 = load('textures/act2.png', (70, 70), "convert_alpha")
        self.__slot = load("textures/menu.png", (21, 21), "convert")
        self.__slot2 = load("textures/menu2.png", (21, 21), "convert")
        self.res = None
        self.__slot.set_alpha(96)
        
    def to_dict(self) -> None:
        """Из списка в словарь"""
        self.__from_num_to_texture()
        lst = []
        for i in self.__some_list:
            try:  # Для того, чтобы предметы не дублировались
                lst.append({i[1]: i[0]})
            except KeyError:
                pass
        self.__some_list = lst

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
        self.__some_list.extend(Inventory.inventory_list)
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
                texture = pygame.transform.scale(
                    list(self.__some_list[i].values())[0], (20, 20))
                self.__screen.blit(texture, (x + 2, y))
                self.__rects_list.append(
                    [texture.get_rect(topleft=(x + 2, y)), texture])
            except IndexError:
                pass
            x += 21
        self.__after_click()
    
    def draw(self, pos: tuple[int, int], player: object) -> None:
        """
        Отрисовка
        
        Args:
            pos (tuple[int, int]): Позиция мыши,
            player (Player): Объект игрока.
        """
        self.__screen.blit(self.__button, (700, 0))
        rect = self.__button.get_rect(topleft=(700, 0))
        rect2 = self.__player.player.get_rect(topleft=(self.__player.x,
                                            self.__player.y))
        
        if rect.collidepoint(pos):  # Кнопка действия
            self.__screen.blit(self.__button2, (700, 0))
            if pygame.mouse.get_pressed()[0]:
                sleep(0.10379)
                if not self.__visible:
                    self.__visible = 1
                else:
                    self.__visible = 0
        if rect.colliderect(rect2):
            self.__button.set_alpha(70)
        else:
            self.__button.set_alpha(800)
            
        if self.__visible:  # Для открытия/сворачивания
            self.__draw_inventory_slots()
            
    def item(self, mp: tuple[int, int],
            texture: pygame.surface.Surface) -> None:
        """
        Отрисовка применяемого предмета
        
        Args:
            mp (tuple[int, int]): Позиция курсора мыши,
            texture (pygame.surface.Surface): Текстура выбранного предмета.
        """
        texture = pygame.transform.scale(texture, (55, 55))
        self.__screen.blit(texture, (mp[0] - 15, mp[1] - 15))
    
    def __after_click(self) -> None:
        """Функционал"""
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        for i in self.__rects_list:
            if i[0].collidepoint(mouse_pos):
                self.__screen.blit(self.__slot2, (i[0][0], i[0][1]))
                self.__screen.blit(i[1], (i[0][0], i[0][1]))
                if pygame.mouse.get_pressed()[0]:  # Взятие предмета
                    if not self.__item_visible:
                        self.__item_visible = 1
                    else:
                        self.__item_visible = 0
                    self.res = i[1]
        if self.__item_visible:  # Предмет на курсоре мыши
            self.item(mouse_pos, self.res)
    
    