"""Главное меню игры"""

import pygame
import sys
import webbrowser
from ..logging import HELogger
from time import sleep


pygame.init()


class MainMenu:
    """Главное меню (включает в себя Boosty, DonationAlerts, кнопку запуска)"""
    
    @staticmethod
    def open(site: str, logger: HELogger) -> None:
        """
        Переправление пользователя на сайт (Boosty, DonationAlerts)

        Args:
            site (str): Ссылка на сайт,
            logger (HELogger): Переменная для логов
        """
        webbrowser.open(site)
        sleep(0.176)
        logger.info(f"Открытие сайта - {site}")
        pygame.mixer.Sound("textures/press.mp3").play()
    
    @staticmethod
    def render(screen: pygame.surface.Surface, logger: HELogger) -> None:
        """
        Рендеринг главного меню

        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            logger (HELogger): Переменная для логов
        """
        logger.debug("Начало инициализации текстур статического метода render")
        cycle = 1
        bg = pygame.transform.scale(pygame.image.load("textures/bg.png").convert(), (770, 770))
        play = pygame.transform.scale(pygame.image.load("textures/play.png").convert_alpha(), (130, 130))
        boosty = pygame.transform.scale(pygame.image.load("textures/boosty.png").convert(), (80, 80))
        da = pygame.transform.scale(pygame.image.load("textures/da.jpg").convert(), (80, 80))
        logger.debug("Завершена инициализация текстур статического метода render")
        
        while cycle:
            screen.blit(bg, (0, 0))
            screen.blit(play, (317, 300))
            
            screen.blit(boosty, (30, 30))
            screen.blit(da, (660, 30))
            pygame.display.flip()
            
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            rect1 = play.get_rect(topleft=(317, 300))
            rect2 = boosty.get_rect(topleft=(30, 30))
            rect3 = da.get_rect(topleft=(660, 30))
            
            if rect1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Кнопка запуска игры
                cycle = 0
            elif rect2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # Boosty
                MainMenu.open("https://boosty.to/sergey_pelmen", logger)
            elif rect3.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:  # DonationAlerts
                MainMenu.open("https://www.donationalerts.com/r/sergeyprojects", logger)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        