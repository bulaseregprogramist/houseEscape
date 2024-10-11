"""Этот модуль отвечает за логи игры"""

from logging import Logger, basicConfig, INFO, ERROR, CRITICAL, getLogger
from logging import WARNING, DEBUG
from typing import Any, Self
import coloredlogs  # Для выделения особым цветом разных логов
import sys


class HELogger(Logger):
    """Этот класс дополняет класс из стандартной библиотеки Python"""
    
    def __init__(self, name='', level=''):
        if name != '' and level != '':  # Для второго запуска конструктора.
            super().__init__(name, level)
        print("[INFO] Logger activated!")
        
    def change_name(self, logger: Self) -> Any:
        """
        Смена названия логгера
        
        Args:
            logger (HELogger): Переменная для логов
        Returns:
            Запуск логгера.
        """
        name = "HouseEscape"
        logger_name = "Logger"
        try:
            if sys.argv[1] == "CHANGE_NAME":
                name = input("Введите первое имя: ")
                logger_name = input("Введите имя логгера: ")
        except IndexError:  # Если пользователь не указал argv.
            pass
        logger = HELogger(name, DEBUG)
        return logger.getChild(logger_name)
        
    @staticmethod
    def set_level(level: int) -> None:
        """
        Установка уровня логирования
        
        Args:
            level (int): Уровень логирования.
        """
        getLogger().handlers = []  # Очистка предыдущего уровня логирования.
        basicConfig(level=level,
                    format="[%(name)s] - [%(levelname)s] - %(message)s",
                    encoding="utf-8")
                
    @staticmethod
    def better_info(logger: Self) -> None:
        """
        Цвета для логов или изменение их уровня.
        
        Args:
            logger (HELogger): Переменная для логов
        """
        try:
            if sys.argv[1] == "BETTER":
                coloredlogs.install(level='DEBUG', logger=logger)
            elif sys.argv[1] == "CHANGE_TO_INFO":
                HELogger.set_level(INFO)
            elif sys.argv[1] == "CHANGE_TO_WARNING":         
                HELogger.set_level(WARNING)
            elif sys.argv[1] == "CHANGE_TO_ERROR":
                HELogger.set_level(ERROR)
            elif sys.argv[1] == "CHANGE_TO_CRITICAL":
                HELogger.set_level(CRITICAL)
        except IndexError:
            pass
    