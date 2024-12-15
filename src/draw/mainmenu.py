"""Главное меню игры"""

import pygame
import sys
import webbrowser
from ..game.logging import HELogger
from ..other.globals import load, font
from ..game.savemenu import SaveMenu
from ..game.experimental import Experimental
from ..api.api import HEAPI
from time import sleep
import logging


pygame.init()


class MainMenu:
    """Главное меню (в нём Boosty, DonationAlerts, кнопку запуска)"""
    
    def __init__(self, screen: pygame.surface.Surface,
                logger: HELogger) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__logger: HELogger = logger
        self.__yes = load("textures/yes.png", (30, 30), "convert")
        self.__no = load("textures/no.png", (30, 30), "convert")
        self.__em = load("textures/em.png", (220, 140), "convert")
    
    def to_menu(self) -> int:
        """
        Возвращение в главное меню
        
        Returns:
            int: Переменным, с которыми работает цикл, присвоено 0.
        """
        logging.info("Игрок возвращён в главное меню")
        return 0
    
    def exit_menu(self, mp: tuple[int, int]) -> None:
        """Меню выхода из игры"""
        cycle = 1
        text = font.render("ВЫЙТИ?", 1, (0, 0, 0))
        while cycle:
            self.__screen.blit(self.__em, (270, 300))
            self.__screen.blit(text, (300, 310))
            self.__screen.blit(self.__yes, (325, 370))
            self.__screen.blit(self.__no, (405, 370))
            
            pygame.display.flip()
            rect1 = self.__yes.get_rect(topleft=(325, 370))
            rect2 = self.__no.get_rect(topleft=(405, 370))
            if rect1.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                self.__logger.info("Выход из игры...")
                sys.exit()
            elif rect2.collidepoint(mp) and pygame.mouse.get_pressed()[0]:
                cycle = 0
            
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.__logger.info("Выход из игры...")
                    sys.exit()
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                    cycle = 0
    
    @classmethod
    def act(cls, mouse_pos: tuple[int, int], screen: pygame.surface.Surface,
            logger: HELogger, play2, mmc: int,
            *rects) -> int | SaveMenu | None:
        """
        Действия в главном меню
        
        Args:
            mouse_pos (tuple[int, int]): Позиция курсора мыши,
            screen (pygame.surface.Surface): Переменная экрана,
            logger (HELogger): Переменная для логов,
            play2 (pygame.surface.Surface): Кнопка запуска (подсвеченная),
            mmc (int): mainmenu_cycle (цикл главного меню),
            *rects (tuple): 'Квадраты' кнопок
        Returns:
            int: Выключение mainmenu_cycle или оставляет всё как есть,
            SaveMenu: Для получения номера сохранения,
            None: Вместо SaveMenu, если игрок ничего не сделал.
        """
        save = None
        if rects[0].collidepoint(mouse_pos):  # Кнопка запуска игры
            screen.blit(play2, (317, 300))  # Свечение
            if pygame.mouse.get_pressed()[0]:
                logger.info("Выход из главного меню")
                mmc = 0
                save = SaveMenu(screen, logger)
                if save.number == "to_menu":
                    mmc = 1
        elif (rects[1].collidepoint(mouse_pos)  # Boosty
                and pygame.mouse.get_pressed()[0]):
            MainMenu.open("https://boosty.to/sergey_pelmen", logger)
        elif (rects[2].collidepoint(mouse_pos)   # DonationAlerts
                and pygame.mouse.get_pressed()[0]):
            MainMenu.open("https://www.donationalerts.com/r/sergeyprojects",
                        logger)
        elif (rects[3].collidepoint(mouse_pos)  # Гайд по API
                and pygame.mouse.get_pressed()[0]):
            HEAPI.guide(screen)
        elif (rects[4].collidepoint(mouse_pos)
                and pygame.mouse.get_pressed()[0]):
            exp = Experimental(screen)
            exp.run()
        return mmc, save
    
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
        flask = load("textures/flask.png", (105, 105), "convert_alpha")
        logger.debug(
            "Завершена инициализация текстур для статического метода render")
        return bg, play, boosty, da, logo, notepad, play2, flask
    
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
        logger.info("Главное меню открыто!")
        mainmenu_cycle = 1
        logger.debug("Переменной cycle присвоен 1")
        bg, play, boosty, da, logo, notepad, play2, flask = MainMenu.__init_textures(
            logger)
        
        while mainmenu_cycle:
            screen.blit(bg, (0, 0))
            screen.blit(play, (317, 300))
            
            screen.blit(boosty, (30, 30))
            screen.blit(da, (660, 30))
            screen.blit(logo, (280, 30))
            screen.blit(notepad, (660, 660))
            screen.blit(flask, (-10, 660))
            
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            rect1 = play.get_rect(topleft=(317, 300))
            rect2 = boosty.get_rect(topleft=(30, 30))
            rect3 = da.get_rect(topleft=(660, 30))  # 'Квадрат' DonationAlerts
            rect4 = notepad.get_rect(topleft=(660, 660))
            rect5 = flask.get_rect(topleft=(-10, 660))
            
            mainmenu_cycle, save = MainMenu.act(mouse_pos, screen, logger,
                    play2, mainmenu_cycle,
                    rect1, rect2, rect3, rect4, rect5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info("Выход из игры...")
                    sys.exit()
                elif event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    mm = MainMenu(screen, logger)
                    mm.exit_menu(mouse_pos)
            pygame.display.flip()
        return save.number
        