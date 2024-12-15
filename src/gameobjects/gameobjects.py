"""Размещение и функционал предметов/мебели"""

from abc import ABC, abstractmethod
from ..entity.inventory import Inventory
from ..game.logging import HELogger
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
    def placing(self, *args: tuple) -> None:
        """
        Размещение предмета на карте
        
        Args:
            *args (tuple): Список с данными (квадрат, объект игрока, текстура).
        """
        rect = args[4].get_rect(topleft=(args[0], args[1]))
        rect2 = args[5].player.get_rect(topleft=(args[5].x, args[5].y))
        if rect.colliderect(rect2):  # Прозрачный объект при вхождении в него
            args[4].set_alpha(64)
        else:  # Непрозрачный объект
            args[4].set_alpha(500)
        if args[2] == args[3]:  # Если игрок находится в одной комнате с объектом
            self.screen.blit(args[4], (args[0], args[1]))
            
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
    def functional(self, *args: tuple) -> int:
        """
        Функционал игрового объекта
        
        Args:
            *args (tuple): Параметры игрового объекта.
        Returns:
            int: 0 - ничего не произошло, 1 - воспроизведение звука #1,
                2 - звук #2, 3 - звук #3.
        """
        rect = args[2].get_rect(topleft=(args[0], args[1]))
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        
        # Небольшое чёрное окошко
        if (rect.collidepoint(mouse_pos)
                and args[4] == args[5]):
            self.__show_menu(args[3])
            if pygame.mouse.get_pressed()[0]:
                sleep(0.2)
                if args[3] == "item":  # args[6] - ключ словаря
                    Inventory.append(args[2], args[6])
                    return 1
                elif args[3] == "block":
                    return 2
                elif args[3] == "picture":
                    return 3
                elif args[3] == "vehicle":
                    return 4
        return 0
    