"""
Меню загрузки игры
"""

import pygame
from src.other.globals import load, font5
from time import sleep


pygame.init()


class LoadMenu:
    """
    Класс меню загрузки игры
    """
    
    def __init__(self, screen):
        self.__screen = screen
        self.__text = font5.render("Загрузка...", True, (255, 255, 255))
        
        self.run()
    
    def run(self) -> None:
        """Основной метод класса"""
        sleep(0.365)
        pygame.draw.rect(self.__screen, (0, 0, 0), (0, 0, 2000, 2000))
        self.__screen.blit(self.__text, (270, 150))

        pygame.display.flip()

