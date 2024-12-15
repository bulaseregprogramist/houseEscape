"""Файл, содержащий класс для того, чтобы не было много аргументов"""

import pygame


pygame.init()


class Config:
    """Класс, содержащий все константы"""
    
    def __init__(self, logger, index: list[int, int], player, num: int,
                mp: tuple[int, int]):
        self.logger = logger
        self.index: list[int, int] = index
        self.player = player
        self.n: int = num
        self.mouse_pos: tuple[int, int] = mp
        
        
class StatsConfig:
    """Класс для информации о персонаже"""
    
    def __init__(self, screen: pygame.surface.Surface,
                index: list[int, int], logger, ch: list[int, int],
                n: int, player,
                ):
        self.screen = screen
        self.index: list[int, int] = index
        self.logger = logger
        self.ch: list[int, int] = ch
        self.n: int = n
        self.player = player
        
        