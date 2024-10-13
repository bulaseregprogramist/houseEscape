"""Неигровые персонажи (НПС)"""

from ..entity.character import Character
from ..other.globals import load, font3
from ..game.logging import HELogger
from ..trade.trade_system import TradeSystem
from ..game.saving import Saving
from ..trade.money_system import MoneySystem
from ..entity.player import Player
from os import listdir
import pygame
import sys


pygame.init()


class NPC(Character):
    """Торговцы"""
    save = Saving()
    
    def __init__(self, screen: pygame.surface.Surface,
                logger: HELogger) -> None:
        self.__screen = screen
        self.__logger = logger
        self.__npc = load("textures/npc.png", (65, 65), "convert_alpha")
    
    def placing(self, mouse_pos: tuple[int, int], player: Player,
                index: list[int, int]) -> None:
        """
        Отрисовка торговца
        
        Args:
            mouse_pos (tuple[int, int]): Позиция мыши,
            player (Player): Объект игрока,
            index (list[int, int]): Позиция игрока на карте.
        """
        self.__screen.blit(self.__npc, (100, 100))
        rect = self.__npc.get_rect(topleft=(100, 100))
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.__menu(player, index)
        elif rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[2]:
            self.get_stats()
        
    def __menu(self, player: Player, index: list[int, int]) -> None:
        """
        Меню торговли
        
        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Позиция игрока на карте.
        """
        cycle = 1
        text = font3.render(f"ВАШИ ДЕНЬГИ - {MoneySystem.MONEY}",
                            1, (0, 0, 0))
        trade_system = TradeSystem()
        while cycle:
            pygame.draw.rect(self.__screen, 
                            (255, 255, 255), (100, 100, 570, 570))
            self.__screen.blit(text, (240, 150))
            pygame.display.flip()
            
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.__logger.info("Выход из игры...")
                    self.save.saving(index, player.x, player.y,
                                    len(listdir("data/")))
                    sys.exit()
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                    cycle = 0
    
    @classmethod
    def change_fields(self) -> None:
        """Смена статических полей"""
        super().change_fields(2)
    
    def get_stats(self) -> None:
        """Получение информации об нпс"""
        super().get_stats(self.__screen, [100, 100], self.__logger, {1: 2})
        self.__logger.info("Выход из меню...")
    
    @staticmethod
    def die(self) -> None:
        """Смерть нпс (торговца)"""
        super().die()
