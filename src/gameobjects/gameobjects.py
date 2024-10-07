"""Размещение и функционал предметов/мебели"""

from abc import ABC, abstractmethod
from ..entity.inventory import Inventory
from ..game.logging import HELogger
from ..draw.draw import Draw
from ..entity.player import Player
from ..other.globals import font2
from time import sleep
import pygame
import pygame.gfxdraw


pygame.init()


class GameObjects(ABC):
    """Этот класс является родителем для классов Item и Block"""
    screen: pygame.surface.Surface
    logger: HELogger
    __text1 = font2.render("ЛКМ для взаимодействия", 1, (255, 255, 255))
    
    @abstractmethod
    def placing(self, x: int, y: int, index: list[int, int], he_map: list[int, int],
                stexture, player: Player) -> None:
        """
        Размещение предмета на карте
        
        Args:
            x (int): Позиция объекта по x,
            y (int): Позиция объекта по y,
            index (list[int, int]): Позиция игрока,
            he_map (list[int, int]): Карта дома,
            texture (pygame.surface.Surface): Текстура объекта,
            player (Player): Объект игрока.
        """
        if index == he_map:  # Если игрок находится в одной комнате с объектом
            self.screen.blit(stexture, (x, y))
        if ((player.x <= x <= player.x + stexture.get_width() * 0.5) 
                and (player.y <= y <= player.y + stexture.get_height() * 1.1)):
            stexture.set_alpha(64)  # Прозрачность
        else:  # Не прозрачность
            stexture.set_alpha(500)
            
    def __show_menu(self, go_type: str) -> None:
        """
        Показывает меню взаимодействия
        
        Args:
            go_type (str): Тип игрового объекта.
        """
        menu = pygame.transform.scale(pygame.image.load(
            "textures/menu.png").convert(), (200, 50))
        menu.set_alpha(64)
        
        self.screen.blit(menu, (30, 710))
        self.screen.blit(self.__text1, (40, 720))
        if go_type == "item":
            text2 = font2.render("item", 1, (255, 255, 255))
            self.screen.blit(text2, (40, 740))
        elif go_type == "block":
            text2 = font2.render("block", 1, (255, 255, 255))
            self.screen.blit(text2, (40, 740))
    
    @abstractmethod
    def functional(self, x: int, y: int, texture, go_type: str,
                he_map: list[int, int], pos: list, key: str = None) -> int:
        """
        Функционал игрового объекта
        
        Args:
            x (int): Позиция объекта по x,
            y (int): Позиция объекта по y,
            texture (pygame.surface.Surface): Текстура объекта,
            go_type (str): GameObject_type. (либо item, либо block),
            he_map (list[int, int]): Позиция игрока,
            pos (list[int, int]): Позиция объекта на карте.
            key (str | None): Ключи для сохранения.
        Returns:
            int: 0 - ничего не произошло, 1 - воспроизведение звука #1,
                2 - звук #2.
        """
        
        if isinstance(texture, str):
            return 0
        rect = texture.get_rect(topleft=(x, y))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        if rect.collidepoint(mouse_pos) and he_map == pos:
            self.__show_menu(go_type)
            if pygame.mouse.get_pressed()[0]:
                sleep(0.2)
                if go_type == "item":
                    Inventory.append(texture, key)
                    return 1
                elif go_type == "block":
                    return 2
        return 0
    