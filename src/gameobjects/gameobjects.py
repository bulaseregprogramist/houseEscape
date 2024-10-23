"""Размещение и функционал предметов/мебели"""

from abc import ABC, abstractmethod
from ..entity.inventory import Inventory
from ..game.logging import HELogger
from ..entity.player import Player
from ..other.globals import font2, load
from time import sleep
import pygame
import re


pygame.init()


class GameObjects(ABC):
    """Этот класс является родителем для классов Item и Block"""
    screen: pygame.surface.Surface
    logger: HELogger
    __text1 = font2.render("ЛКМ для взаимодействия", 1, (255, 255, 255))
    
    @abstractmethod
    def placing(self, x: int, y: int, index: list[int, int],
                he_map: list[int, int], stexture: pygame.surface.Surface,
                player: Player) -> None:
        """
        Размещение предмета на карте
        
        Args:
            x (int): Позиция объекта по x,
            y (int): Позиция объекта по y,
            index (list[int, int]): Позиция игрока,
            he_map (list[int, int]): Карта дома,
            stexture (pygame.surface.Surface): Текстура объекта,
            player (Player): Объект игрока.
        """
        rect = stexture.get_rect(topleft=(x, y))
        rect2 = player.player.get_rect(topleft=(player.x, player.y))
        if rect.colliderect(rect2):  # Прозрачный объект при вхождении в него
            stexture.set_alpha(64)
        else:
            stexture.set_alpha(500)
        if index == he_map:  # Если игрок находится в одной комнате с объектом
            self.screen.blit(stexture, (x, y))
            
    @staticmethod
    def _num_to_texture(command: str) -> pygame.surface.Surface:
        """
        От команды к текстуре в игре
        
        Args:
            command (str): Команда для загрузки изображения
        Returns:
            pygame.surface.Surface: Текстура игрового объекта.
        """
        pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

        match = re.search(pattern, command)
        return load(match.group(1), (60, 60), "convert_alpha")
            
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
            text2 = font2.render("предмет", 1, (255, 255, 255))
            self.screen.blit(text2, (40, 740))
        elif go_type == "block":
            text2 = font2.render("мебель/техника", 1, (255, 255, 255))
            self.screen.blit(text2, (40, 740))
        elif go_type == "vehicle":
            text2 = font2.render("транспорт", 1, (255, 255, 255))
            self.screen.blit(text2, (40, 740))
    
    @abstractmethod
    def functional(self, x: int, y: int, texture, go_type: str,
                he_map: list[int, int], pos: list[int, int],
                key: str = None) -> int:
        """
        Функционал игрового объекта
        
        Args:
            x (int): Позиция объекта по x,
            y (int): Позиция объекта по y,
            texture (pygame.surface.Surface): Текстура объекта,
            go_type (str): GameObject_type. (содержит имена наследников),
            he_map (list[int, int]): Позиция игрока,
            pos (list[int, int]): Позиция объекта на карте.
            key (str | None): Ключи для сохранения.
        Returns:
            int: 0 - ничего не произошло, 1 - воспроизведение звука #1,
                2 - звук #2, 3 - звук #3.
        """
        
        if isinstance(texture, str):
            return 0
        rect = texture.get_rect(topleft=(x, y))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        # Небольшое чёрное окошко
        if (rect.collidepoint(mouse_pos)
                and he_map == pos):
            self.__show_menu(go_type)
            if pygame.mouse.get_pressed()[0]:
                sleep(0.2)
                if go_type == "item":
                    Inventory.append(texture, key)
                    return 1
                elif go_type == "block":
                    return 2
                elif go_type == "vehicle":
                    return 3
        return 0
    