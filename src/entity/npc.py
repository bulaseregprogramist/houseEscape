"""Неигровые персонажи (НПС)"""

from ..entity.character import Character
from ..other.globals import load, font3
from ..game.logging import HELogger
from ..trade.trade_system import TradeSystem
from ..game.saving import Saving
from ..trade.money_system import MoneySystem
from ..entity.player import Player
from os import listdir
from time import sleep
import pygame
import sys


pygame.init()


class NPC(Character):
    """Торговцы"""
    save = Saving()
    
    def __init__(self, screen: pygame.surface.Surface, logger: HELogger,
                index: list[int, int], num: int) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__logger: HELogger = logger
        self.__index: list[int, int] = index
        self.__num = num
        self.__npc = load("textures/npc.png", (65, 65), "convert_alpha")
    
    def placing(self, mouse_pos: tuple[int, int], player: Player,
                index: list[int, int], num: int) -> None:
        """
        Отрисовка торговца.
        
        Args:
            mouse_pos (tuple[int, int]): Позиция мыши,
            player (Player): Объект игрока,
            index (list[int, int]): Позиция игрока на карте,
            num (int): Номер выбранного сохранения
        """
        self.__screen.blit(self.__npc, (100, 100))
        rect = self.__npc.get_rect(topleft=(100, 100))
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.__menu(player, index, num)
        elif rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[2]:
            self.get_stats()
        
    def __menu(self, player: Player, index: list[int, int], num: int) -> None:
        """
        Меню торговли.
        
        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Позиция игрока на карте,
            num (int): Номер выбранного сохранения.
        """
        cycle = 1
        trade_system = TradeSystem(self.__screen, num, player, player.use)
        while cycle:
            text = font3.render(f"ВАШИ ДЕНЬГИ - {MoneySystem.MONEY}",
                            1, (0, 0, 0))
            pygame.draw.rect(self.__screen, 
                            (255, 255, 255), (100, 100, 570, 570))
            self.__screen.blit(text, (240, 150))
            trade_system.draw_items()
            pygame.display.flip()
            
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.__logger.info("Выход из игры...")
                    self.save.saving(index, player.x, player.y,
                                    len(listdir("data/")), True)
                    sys.exit()
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                    sleep(0.3)
                    cycle = 0
    
    @classmethod
    def change_fields(self) -> None:
        """Смена статических полей."""
        super().change_fields(2)
    
    def get_stats(self) -> None:
        """Получение информации об нпс."""
        super().get_stats(self.__screen, self.__index, self.__num,
                        [100, 100], self.__logger, {1: 2})
        self.__logger.info("Выход из меню...")
    
    @staticmethod
    def die(self) -> None:
        """Смерть нпс (торговца)."""
        super().die()
