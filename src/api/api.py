"""Модуль, отвечающий за API игры (внутренняя реализация)"""

from ..game.logging import HELogger
from os import listdir
from ..other.globals import font
import logging
import pygame
import sys


pygame.init()


class HEAPI:
    """API игры HouseEscape"""
    
    @classmethod
    def get_mods_data(cls) -> dict:
        """Получение данных о модах"""

    @staticmethod
    def guide(screen: pygame.surface.Surface) -> None:
        """
        Руководство по примению API
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана.
        """
        sound = pygame.mixer.Sound("textures/collect.mp3")
        sound.set_volume(0.4)
        sound.play()
        text = font.render("Гайд по API", 1, (0, 0, 0))

        cycle = 1
        while cycle:
            screen.fill((255, 255, 255))
            screen.blit(text, (230, 50))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    cycle = 0

    @staticmethod
    def load(logger: HELogger) -> None:
        """
        Загрузка модов в игру

        Args:
            logger (HELogger): Переменная для логов
        """
        logging.basicConfig(level=logging.INFO,
            format="[%(name)s] - [%(levelname)s] - %(message)s",
            encoding="utf-8",
        )
        logger.info("Загрузка модов...")
        if len(listdir("mods/")) > 0:
            logger.info("Моды обнаружены!")
            logger.info(f"Загрузка {len(listdir("mods/"))} модов.")
            HEAPI.__initialize_mods()
        else:
            logger.warning("Модов не обнаружено!")
        logger.info("Загрузка модов завершена!")

    @staticmethod
    def __initialize_mods() -> None:
        """Инициализация модов"""
        list_of_mods: list[str, ...] = listdir("mods/")
        for i in list_of_mods:
            if i.endswith(".json"):
                with open(f"mods/{i}") as file:
                    result: dict = HEAPI.get_mods_data()
