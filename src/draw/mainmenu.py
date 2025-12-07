"""Главное меню игры"""

import pygame
import sys
import webbrowser
import logging
from time import sleep
from ..other.configs import MainMenuConfig
from ..other.ai import ArtificalIntelligence
from ..game.settings import Settings
from ..game.logging import HELogger
from ..other.globals import load, font, game_exit, font3
from ..game.savemenu import SaveMenu
from ..game.experimental import Experimental
from ..api.api import HEAPI


pygame.init()


class MainMenu:
    """Главное меню (в нём Boosty, DonationAlerts, кнопку запуска)"""

    def __init__(self, screen: pygame.surface.Surface,
                logger: HELogger) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__logger = logger
        self.__textures = {
            "yes": load("textures/yes.png", (30, 30), "convert"),
            "no": load("textures/no.png", (30, 30), "convert"),
            "em": load("textures/em.png", (220, 140), "convert")}

    def to_menu(self) -> int:
        """
        Возвращение в главное меню

        Returns:
            int: Переменным, с которыми работает цикл, присвоено 0.
        """
        logging.info("Игрок возвращён в главное меню")
        return 0

    def exit_menu(self, mouse_pos: tuple[int, int]) -> None:
        """
        Меню выхода из игры
        
        Args:
            mouse_pos (tuple[int, int]): Позиция мыши
        """
        cycle = 1
        text = font.render("ВЫЙТИ?", 1, (0, 0, 0))
        while cycle:
            self.__screen.blit(self.__textures["em"], (270, 300))
            self.__screen.blit(text, (300, 310))
            self.__screen.blit(self.__textures["yes"], (325, 370))
            self.__screen.blit(self.__textures["no"], (405, 370))

            pygame.display.flip()
            rect_yes = self.__textures["yes"].get_rect(topleft=(325, 370))
            rect_no = self.__textures["no"].get_rect(topleft=(405, 370))
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

            if (rect_yes.collidepoint(mouse_pos) 
                    and pygame.mouse.get_pressed()[0]):
                self.__logger.info("Выход из игры...")
                sys.exit()
            elif (rect_no.collidepoint(mouse_pos) 
                    and pygame.mouse.get_pressed()[0]):
                break
                
            cycle: int = game_exit(self.__logger)

    @classmethod
    def act(cls, config: MainMenuConfig, *rects) -> int | SaveMenu | None:
        """
        Действия в главном меню

        Args:
            config (MainMenuConfig): Конфиг (позиция мыши, экран, ...)
            *rects (tuple): 'Квадраты' кнопок
        Returns:
            int: Выключение mainmenu_cycle или оставляет всё как есть,
            SaveMenu: Для получения номера сохранения,
            None: Вместо SaveMenu, если игрок ничего не сделал.
        """
        save = None
        if rects[0].collidepoint(config.mouse_pos):  # Кнопка запуска игры
            config.screen.blit(config.textures[2], (317, 300))  # Свечение
            if pygame.mouse.get_pressed()[0]:
                config.logger.info("Выход из главного меню")
                config.mmc = 0
                save = SaveMenu(config.screen, config.logger)
                if save.number == "to_menu":
                    config.mmc = 1
        elif (rects[1].collidepoint(config.mouse_pos) 
            and pygame.mouse.get_pressed()[0]):  # Boosty
            cls.open("https://boosty.to/sergey_pelmen", config.logger)
        elif (rects[2].collidepoint(config.mouse_pos) 
            and pygame.mouse.get_pressed()[0]):  # DonationAlerts
            cls.open("https://www.donationalerts.com/r/sergeyprojects",
                    config.logger)
        elif rects[3].collidepoint(config.mouse_pos):  # Гайд по API
            notepad2 = load("textures/notepad2.png", (105, 105),
                            "convert_alpha")
            config.screen.blit(notepad2, (660, 660))
            if pygame.mouse.get_pressed()[0]:
                HEAPI.guide(config.screen)
        elif rects[4].collidepoint(config.mouse_pos):  # Эксперименты
            flask2 = load("textures/flask2.png", (105, 105), "convert_alpha")
            config.screen.blit(flask2, (-10, 660))
            if pygame.mouse.get_pressed()[0]:
                exp = Experimental(config.screen)
                exp.run()
        elif rects[5].collidepoint(config.mouse_pos):  # Настройки
            config.screen.blit(config.textures[9], (460, 680))
            if pygame.mouse.get_pressed()[0]:
                Settings(config.screen)
        elif rects[6].collidepoint(config.mouse_pos):  # AI
            config.screen.blit(config.textures[11], (180, 660))
            if pygame.mouse.get_pressed()[0]:
                ArtificalIntelligence(config.screen, config.logger)
        return config.mmc, save

    @staticmethod
    def open(site: str, logger: HELogger) -> None:
        """
        Переправление пользователя на сайт (Boosty, DonationAlerts)

        Args:
            site (str): Ссылка на сайт,
            logger (HELogger): Переменная для логов
        """
        webbrowser.open(site)
        sleep(0.176)  # Чтобы предотвратить многократное срабатывание
        logger.info(f"Открытие сайта - {site}")
        pygame.mixer.Sound("textures/press.mp3").play()

    @staticmethod
    def __init_textures(logger: HELogger) -> tuple[pygame.surface.Surface]:
        """
        Инициализация текстур

        Args:
            logger (HELogger): Переменная для логов
        Returns:
            tuple[pygame.surface.Surface]: Загруженные текстуры
        """
        logger.debug(
            "Начало инициализации текстур для статического метода render")
        textures = (load("textures/bg.png", (770, 770), "convert"),
            load("textures/play.png", (130, 130), "convert_alpha"),
            load("textures/play2.png", (130, 130), "convert_alpha"),
            load("textures/boosty.png", (80, 80), "convert"),
            load("textures/da.jpg", (80, 80), "convert"),
            load("textures/logo.png", (210, 210), "convert"),
            load("textures/notepad.png", (105, 105), "convert_alpha"),
            load("textures/flask.png", (105, 105), "convert_alpha"),
            load("textures/settings.png", (80, 80), "convert_alpha"),
            load("textures/settings2.png", (80, 80), "convert_alpha"),
            load('textures/ai.png', (105, 105), 'convert_alpha'),
            load('textures/ai2.png', (105, 105), 'convert_alpha'))
        logger.debug(
            "Завершена инициализация текстур для статического метода render")
        return textures

    @staticmethod
    def render(screen: pygame.surface.Surface, logger: HELogger, Draw) -> int:
        """
        Рендеринг главного меню

        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            logger (HELogger): Переменная для логов,
            Draw (Draw): Класс, для отрисовки.
        Returns:
            int: Номер выбранного сохранения.
        """
        logger.info("Главное меню открыто!")
        mainmenu_cycle = 1
        textures: tuple = MainMenu.__init_textures(logger)
        author_name = font3.render("создано SergeyProjects",
                                1, (255, 255, 255))
        boosty_name = font3.render("Boosty", 1, (0, 255, 255))
        da_name = font3.render("DonationAlerts", 1, (0, 255, 255))

        while mainmenu_cycle:
            Draw.draw_mainmenu(screen, author_name,
                            boosty_name, da_name, textures)

            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            rects = (textures[1].get_rect(topleft=(317, 300)),
                textures[2].get_rect(topleft=(30, 30)),
                textures[3].get_rect(topleft=(660, 30)),
                textures[5].get_rect(topleft=(660, 660)),
                textures[7].get_rect(topleft=(-10, 660)),
                textures[8].get_rect(topleft=(460, 680)),
                textures[10].get_rect(topleft=(180, 660)))
            mainmenu_cycle, save = MainMenu.act(
                MainMenuConfig(mouse_pos, screen, textures,
                logger, mainmenu_cycle), *rects)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info("Выход из игры...")
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    mm = MainMenu(screen, logger)
                    mm.exit_menu(mouse_pos)

            pygame.display.flip()
        return save if save else 0

