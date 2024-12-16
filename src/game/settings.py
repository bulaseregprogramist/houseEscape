"""Настройки игры"""

import pygame
import sys


pygame.init()


class Settings:
    """Основной класс"""
    
    def __init__(self) -> None:
        self.__run()
    
    def __run(self) -> None:
        """Основной метод класса"""
        cycle = 1
        while cycle:
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.type == pygame.KEYDOWN 
                            and event.key == pygame.K_ESCAPE):
                        cycle = 0
    
    