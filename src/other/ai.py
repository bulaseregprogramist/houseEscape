"""Искусственный интеллект"""

import pygame
from ..other.globals import game_exit, font, font3


pygame.init()


class ArtificalIntelligence:
    """Искусственный интеллект"""
    
    def __init__(self, screen: pygame.surface.Surface, logger) -> None:
        self.__screen = screen
        self.__logger = logger
        self.__text = font.render('Esc - для выхода', True, (0, 0, 0),
                                (255, 255, 255))
        self.__text1 = font.render('Искусственный интеллект', True, (0, 0, 0),
                                (255, 255, 255))
        self.load_ai()
        
    def f1(self) -> None:
        """
        
        """
        pass
    
    def f2(self) -> None:
        """
        
        """
        pass
    
    def load_ai(self) -> None:
        """
        Основная функция класса
        """
        cycle = 1
        
        while cycle:
            pygame.draw.rect(self.__screen, (255, 255, 255),
                            (0, 0, 900, 900))
            self.__screen.blit(self.__text, (30, 700))
            self.__screen.blit(self.__text1, (60, 20))
            
            pygame.display.flip()
            
            cycle = game_exit(self.__logger)         

