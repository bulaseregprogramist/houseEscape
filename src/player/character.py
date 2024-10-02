"""Персонаж"""

from abc import abstractmethod, ABC
import sys
import pygame
from ..other.globals import load, font4
from time import sleep
from copy import copy


pygame.init()


class Character(ABC):
    speed = 1
    
    @classmethod
    @abstractmethod
    def change_fields(cls, speed: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            speed (int): Скорость персонажа
        """
        cls.speed = speed
        
    @abstractmethod
    def get_stats(self, screen: pygame.surface.Surface, ch: list[int, int], *args) -> None:
        """
        Получение информации об персонаже
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            ch (list[int, int]): Координаты игрока,
            *args (Any): Статичные поля класса
        """
        data_menu_cycle, y = 1, ch[1] - 30
        y2 = copy(y)
        menu = load("textures/menu.png", (152, 150), "convert")
        texts_list = [font4.render(str(i), 1, (255, 255, 255)) for i in args[0].values()]
        while data_menu_cycle:
            screen.blit(menu, (ch[0] - 30, ch[1] - 30))
            #print(texts_list)
            
            for j in texts_list:
                screen.blit(j, (ch[0] - 30, y))
                y += 25
            y = copy(y2)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sleep(0.15)
                    data_menu_cycle = 0
    
    @staticmethod
    def filter_data(dct: dict) -> dict:
        """Для получения статичных полей"""
        class_attributes = {key: value for key, value in dct.__dict__.items() 
                    if not callable(value) and not key.startswith('__') and not isinstance(value, classmethod)
                    and not key.startswith('_') or key.isupper()}

        # Вывод атрибутов класса
        for attr, value in class_attributes.items():
            print(f"{attr}: {value}")
        return class_attributes
    
    @abstractmethod
    def die(self) -> None:
        """Смерть персонажа"""
        pass
    