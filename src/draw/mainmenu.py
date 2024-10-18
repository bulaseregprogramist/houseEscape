"""Главное меню игры"""

import pygame
import sys
import webbrowser
from ..game.logging import HELogger
from ..other.globals import load
from ..game.savemenu import SaveMenu
from ..api.api import HEAPI
from time import sleep
import logging


pygame.init()


class MainMenu:
    """Главное меню (в нём Boosty, DonationAlerts, кнопку запуска)"""
    
    def to_menu(self) -> int:
        """
        Возвращение в главное меню
        
        Returns:
            int: Переменным, с которыми работает цикл, присвоено 0.
        """
        logging.info("Игрок возвращён в главное меню")
        return 0
    
    @staticmethod
    def open(site: str, logger: HELogger) -> None:
        """
        Переправление пользователя на сайт (Boosty, DonationAlerts)

        Args:
            site (str): Ссылка на сайт,
            logger (HELogger): Переменная для логов
        """
        webbrowser.open(site)
        # Если игрок нажимает, срабатывает несколько раз, 
        # sleep для того, чтобы это предотвратить.
        sleep(0.176)
        logger.info(f"Открытие сайта - {site}")
        pygame.mixer.Sound("textures/press.mp3").play()
        
    @staticmethod
    def __init_textures(logger: HELogger) -> pygame.surface.Surface:
        """
        Инициализация текстур
        
        Args:
            logger (HELogger): Переменная для логов
        Returns:
            pygame.surface.Surface: Загруженные текстуры
        """
        logger.debug(
            "Начало инициализации текстур для статического метода render")
        bg = load("textures/bg.png", (770, 770), "convert")
        play = load("textures/play.png", (130, 130), "convert_alpha")
        play2 = load("textures/play2.png", (130, 130), "convert_alpha")
        boosty = load("textures/boosty.png", (80, 80), "convert")
        da = load("textures/da.jpg", (80, 80), "convert")
        logo = load("textures/logo.png", (210, 210), "convert")
        notepad = load("textures/notepad.png", (105, 105), "convert_alpha")
        logger.debug(
            "Завершена инициализация текстур для статического метода render")
        return bg, play, boosty, da, logo, notepad, play2
    
    @staticmethod
    def render(screen: pygame.surface.Surface, logger: HELogger) -> int:
        """
        Рендеринг главного меню

        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            logger (HELogger): Переменная для логов
        Returns:
            int: Номер выбранного сохранения.
        """
        mainmenu_cycle = 1
        logger.debug("Переменной cycle присвоен 1")
        bg, play, boosty, da, logo, notepad, play2 = MainMenu.__init_textures(
            logger)
        
        while mainmenu_cycle:
            screen.blit(bg, (0, 0))
            screen.blit(play, (317, 300))
            
            screen.blit(boosty, (30, 30))
            screen.blit(da, (660, 30))
            screen.blit(logo, (280, 30))
            screen.blit(notepad, (660, 660))
            
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            rect1 = play.get_rect(topleft=(317, 300))
            rect2 = boosty.get_rect(topleft=(30, 30))
            rect3 = da.get_rect(topleft=(660, 30))  # 'Квадрат' DonationAlerts
            rect4 = notepad.get_rect(topleft=(660, 660))
            
            # Кнопка запуска игры
            if rect1.collidepoint(mouse_pos):
                screen.blit(play2, (317, 300))
                if pygame.mouse.get_pressed()[0]:
                    logger.info("Выход из главного меню")
                    mainmenu_cycle = 0
                    save = SaveMenu(screen, logger)
            # Boosty
            elif (rect2.collidepoint(mouse_pos) 
                    and pygame.mouse.get_pressed()[0]):
                MainMenu.open("https://boosty.to/sergey_pelmen", logger)
            # DonationAlerts
            elif (rect3.collidepoint(mouse_pos)
                    and pygame.mouse.get_pressed()[0]):
                MainMenu.open(
                    "https://www.donationalerts.com/r/sergeyprojects", logger)
            # Гайд по API
            elif (rect4.collidepoint(mouse_pos)
                    and pygame.mouse.get_pressed()[0]):
                HEAPI.guide()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info("Выход из игры...")
                    sys.exit()
            pygame.display.flip()
        return save.number
        