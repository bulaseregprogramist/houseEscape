"""Модуль, отвечающий за API игры"""

from src.game.logging import HELogger
from os import listdir
import logging


class HEAPI:
    """API игры HouseEscape"""
    
    @staticmethod
    def guide() -> None:
        """Руководство по примению API"""
        pass
    
    @staticmethod
    def load(logger: HELogger) -> None:
        """
        Загрузка модов в игру
        
        Args:
            logger (HELogger): Переменная для логов
        """
        logging.basicConfig(level=logging.INFO, 
                        format="[%(name)s] - [%(levelname)s] - %(message)s",
                        encoding="utf-8")
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
            with open(f"mods/{i}") as file:
                pass
    