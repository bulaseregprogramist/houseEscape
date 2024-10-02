"""Игрок игры House Escape"""

import pygame
import sys
from keyboard import is_pressed
from src.player.move import Move
from ..game.logging import HELogger
from ..game.saving import Saving
from .character import Character
from .inventory import Inventory
#from ..player.player import Player


pygame.init()


class Player(Character):
    """Игрок и связанное с ним"""
    MAX_CAPACITY = 8  # Максимум предметов в инвентаре
    
    def __init__(self, logger: HELogger, screen: pygame.surface.Surface) -> None:
        logger.info("Начата работа конструктора Player")
        self.__save = Saving()
        self.x = self.__save.load_save()["x"]  # Изначальное положение игрока по x
        self.y = self.__save.load_save()["y"]  # Изначальное положение игрока по y
        self.player = pygame.transform.scale(
            pygame.image.load("textures/player.png").convert_alpha(), (60, 60))
        self.__inventory = pygame.transform.scale(
            pygame.image.load("textures/backpack.png").convert_alpha(), (90, 90))
        self.__screen = screen
        logger.info("Завершена работа конструктора Player")
        
    def __to_inventory(self, logger: HELogger, 
                    index: list[int, int], player: object) -> None:
        """
        Инвентарь игрока (открывается на E)
        
        Args:
            logger (HELogger): Переменная для логов,
            index (list[int, int]): Позиция игрока на карте,
            player (Player): Объект игрока
        """
        logger.info("Открытие инвентаря")
        Inventory.Player = self
        inventory = Inventory(self.__inventory, self.__screen)
        inventory.open(index, player)
        logger.info("Закрытие инвентаря")
        
    def player_interfaces(self, screen: pygame.surface.Surface,
                        player: object) -> pygame.surface.Surface:
        """
        Интерфейсы игрока (инвентарь)
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана
            player (Player): Объект класса Player
        Returns:
            pygame.surface.Surface: 'Квадрат' текстуры рюкзака (инвентаря)
        """
        screen.blit(self.__inventory, (10, 10))
        rect = self.__inventory.get_rect(topleft=(10, 10))
        rect2 = self.player.get_rect(topleft=(player.x, player.y))
        if rect.colliderect(rect2):
            self.__inventory.set_alpha(95)
        else:
            self.__inventory.set_alpha(300)
        return rect
        
    def blit(self) -> pygame.surface.Surface:
        """Вывод игрока на экран"""
        self.__screen.blit(self.player, (self.x, self.y))
        return self.player.get_rect(topleft=(self.x, self.y))
        
    def get_stats(self, logger: HELogger) -> None:
        """
        Получение информации об игроке
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        logger.info("Получение информации об игроке")
        result: dict = Character.filter_data(self)
        super().get_stats(self.__screen, [self.x, self.y], result)
        logger.info("Информация об игроке получена!")
    
    def die(self) -> None:
        """Смерть игрока"""
        super().die()
        
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
        
    def open_inventory(self, logger: HELogger, rect: pygame.surface.Surface) -> None:
        """
        Открытие инвентаря
        
        Args:
            logger (HELogger): Переменная для логов,
            rect (pygame.surface.Surface): 'Квадрат' рюкзака.
        """
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.__to_inventory(logger)
        
    def in_game(self, player: object, index: list[int, int], logger: HELogger,
                rect: pygame.surface.Surface) -> None:
        """
        Поведение игрока в игре

        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Карта дома,
            logger (HELogger): Переменная для логов
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Закрытие программы")
                self.__save.saving(index, player.x, player.y)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                logger.info(f"Нажата клавиша - {pygame.KEYDOWN}")
                if event.key == pygame.K_e:
                    self.__to_inventory(logger, index, player)
        if is_pressed("w") and Move.move_in_location(player.x, player.y, index) and self.x < 753:
            self.y -= 3 * self.speed
        elif is_pressed("a") and Move.move_in_location(player.x, player.y, index) and self.x > -23:
            self.x -= 3 * self.speed
        elif is_pressed("s") and Move.move_in_location(player.x, player.y, index) and self.y > -23:
            self.y += 3 * self.speed
        elif is_pressed("d") and Move.move_in_location(player.x, player.y, index) and self.x < 753:
            self.x += 3  * self.speed
        self.open_inventory(logger, rect)
        