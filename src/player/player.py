"""Игрок игры House Escape"""

import pygame
import sys
from keyboard import is_pressed
from src.player.move import Move
from ..game.logging import HELogger
from .character import Character
from .inventory import Inventory
#from ..player.player import Player


pygame.init()


class Player(Character):
    """Игрок и связанное с ним"""
    MAX_CAPACITY = 8  # Максимум предметов в инвентаре
    
    def __init__(self, logger: HELogger, screen: pygame.surface.Surface) -> None:
        logger.info("Начата работа конструктора Player")
        self.x, self.y = 385, 385  # Изначальное положение игрока
        self.player = pygame.transform.scale(pygame.image.load("textures/player.png").convert_alpha(), (60, 60))
        self.__inventory = pygame.transform.scale(pygame.image.load("textures/backpack.png").convert_alpha(), (90, 90))
        self.__screen = screen
        logger.info("Завершена работа конструктора Player")
        
    def __to_inventory(self, logger: HELogger) -> None:
        """
        Инвентарь игрока (открывается на E)
        
        Args:
            logger (HELogger): Переменная для логов
        """
        logger.info("Открытие инвентаря")
        Inventory.Player = self
        inventory = Inventory(self.__inventory, self.__screen)
        inventory.open()
        logger.info("Закрытие инвентаря")
        
    def player_interfaces(self, screen: pygame.surface.Surface) -> None:
        """
        Интерфейсы игрока (инвентарь)
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана
        """
        screen.blit(self.__inventory, (10, 10))
        
    def get_stats(self) -> None:
        """Получение информации об игроке"""
        pass
    
    def die(self) -> None:
        """Смерть игрока"""
        pass
        
    @classmethod
    def change_fields(cls, logger: HELogger, mc: int, speed: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            logger (HELogger): Переменная для логов,
            mc (int): Изменение статичного поля MAX_CAPACITY,
            speed (int): Изменение статичного поля speed
        """
        logger.debug("Идёт смена полей класса...")
        super().change_fields(speed)
        cls.MAX_CAPACITY = mc
        logger.debug("Поля класса изменены!")
        
    def in_game(self, player: object, index: list[int, int], logger: HELogger) -> None:
        """
        Движение игрока в игре и нажатие на клавиши

        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Карта дома,
            logger (HELogger): Переменная для логов
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Закрытие программы")
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                logger.info(f"Нажата клавиша - {pygame.KEYDOWN}")
                if event.key == pygame.K_e:
                    self.__to_inventory(logger)
        if is_pressed("w") and Move.move_in_location(player.x, player.y, index) and self.x < 753:
            self.y -= 3 * self.speed
        elif is_pressed("a") and Move.move_in_location(player.x, player.y, index) and self.x > -23:
            self.x -= 3 * self.speed
        elif is_pressed("s") and Move.move_in_location(player.x, player.y, index) and self.y > -23:
            self.y += 3 * self.speed
        elif is_pressed("d") and Move.move_in_location(player.x, player.y, index) and self.x < 753:
            self.x += 3  * self.speed
        