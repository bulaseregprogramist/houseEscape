"""Мебель дома"""

from .gameobjects import GameObjects
from ..draw.draw import Draw
from ..game.saving import Saving
from ..entity.player import Player
import pygame


pygame.init()


class Block(GameObjects):
    """Блоки (мебель) в доме"""
    save = Saving()
    screen: pygame.surface.Surface
    
    def placing(self, he_map: list[int, int], player: Player, n: int) -> None:
        """
        Размещение мебели
        
        Args:
            he_map (list[int, int]): Карта дома,
            player (Player): Игрок,
            n (int): Номер выбранного сохранения.
        """
        # Позиции мебели и их текстуры
        self.__blocks = self.save.load_save(n)["blocks"]
        for i in self.__blocks:
            texture = pygame.transform.scale(
                self._num_to_texture(self.__blocks[i][4]), (50, 50))
            some_list: list[int, int] = [self.__blocks[i][2],
                                        self.__blocks[i][3]]
            super().placing(int(self.__blocks[i][0]),
                int(self.__blocks[i][1]), some_list, he_map, texture, player)
            self.functional(self.__blocks[i][0], self.__blocks[i][1], texture,
                            he_map, some_list, i, n)
    
    def functional(self, x: int, y: int, texture: pygame.surface.Surface,
                he_map: list[int, int], some_list: list[int, int],
                i: int, n: int) -> None:
        """
        Функционал мебели
        
        Args:
            x (int): Позиция мебели по x,
            y (int): Позиция мебели по y,
            texture (pygame.surface.Surface): Текстура мебели,
            he_map (list[int, int]): Позиция игрока на карте,
            some_list (list[int, int]): Позиция мебели на карте,
            i (int): Ключи мебели,
            n (int): Номер выбранного сохранения.
        """
        result: int = super().functional(x, y, texture, "block", he_map, 
                                        some_list)
        if result == 2:  # Открытие меню мебели
            Draw.show_interfaces(i, self.screen, n)
            pygame.mixer.Sound("textures/press2.mp3").play()
    