"""Игрок игры House Escape"""

import pygame
import sys
from keyboard import is_pressed
from src.player.move import Move
from ..logging import HELogger
#from ..player.player import Player


pygame.init()


class Player:
    """Игрок и связанное с ним"""
    
    def __init__(self, logger: HELogger) -> None:
        logger.info("Начата работа конструктора Player")
        self.x, self.y = 385, 385  # Изначальное положение игрока
        self.player = pygame.transform.scale(pygame.image.load("textures/player.png").convert_alpha(), (60, 60))
        logger.info("Завершена работа конструктора Player")
        
    def in_game(self, player: object, index: list[int, int], logger: HELogger) -> None:
        """
        Движение игрока в игре

        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Карта дома,
            logger (HELogger): Переменная для логов
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Закрытие программы")
                sys.exit()
        if is_pressed("w") and Move.move_in_location(player.x, player.y, index):
            self.y -= 3
        elif is_pressed("a") and Move.move_in_location(player.x, player.y, index):
            self.x -= 3
        elif is_pressed("s") and Move.move_in_location(player.x, player.y, index):
            self.y += 3
        elif is_pressed("d") and Move.move_in_location(player.x, player.y, index):
            self.x += 3  
        