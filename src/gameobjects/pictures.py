"""Картины"""

from ..gameobjects.gameobjects import GameObjects
from ..entity.player import Player
from ..game.saving import Saving
from ..other.globals import load
import logging
import requests  # Для того, чтобы воспользоваться API cataas.
import pygame
import io  # Для загрузки картинки с котиками (из байтов в код)


pygame.init()


class Pictures(GameObjects):
    """Картины с котиками"""
    save = Saving()
    load_picture = 1
    
    def __init__(self) -> None:
        self.__frame = load("textures/frame.png", (125, 125), "convert_alpha")
        logging.debug("Завершена работа конструктора класса Pictures")
    
    @classmethod
    def __load_picture_from_site(cls) -> None:
        """Загрузка картинки"""
        method_cycle = 1
        while method_cycle:
            try:
                result: requests.models.Response = requests.get(
                    "https://cataas.com/cat")
                cls.image: pygame.surface.Surface = pygame.image.load(
                    io.BytesIO(result.content))
                cls.image = pygame.transform.scale(cls.image.convert(),
                                                (68, 110))
                cls.load_picture = 0
                method_cycle = 0
            except pygame.error:
                pass
            except requests.exceptions.ConnectionError:
                logging.error("У пользователя нет интернета!")

    def placing(self, he_map: list[int, int], player: Player, n: int,
                screen: pygame.surface.Surface) -> None:
        """
        Размещение картин.
        
        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Объект игрока,
            n (int): Номер выбранного сохранения,
            screen (pygame.surface.Surface): Переменная дисплея.
        """
        self.__pict: dict[int: list, ...] = self.save.load_save(n)["pictures"]
        
        if self.load_picture:  # Оптимизация
            self.__load_picture_from_site()
        for i in self.__pict:  # Отрисовка картин
            if [self.__pict[i][2], self.__pict[i][3]] == he_map:
                screen.blit(self.__frame, (self.__pict[i][0] + 5,
                                    self.__pict[i][1] - 5))
                rect = self.__frame.get_rect(topleft=(self.__pict[i][0] + 7,
                                                    self.__pict[i][1]))
                if rect.colliderect(player.player.get_rect(  # Прозрачность
                        topleft=(player.x, player.y))):
                    self.__frame.set_alpha(64)
                else:  # Не прозрачность
                    self.__frame.set_alpha(500)
            super().placing(self.__pict[i][0] + 37, self.__pict[i][1] + 3,
                    [self.__pict[i][2], self.__pict[i][3]],
                    he_map, self.image, player)
    
    def functional(self) -> None:
        """Функционал картины"""
        pass