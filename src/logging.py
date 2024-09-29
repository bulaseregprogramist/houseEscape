"""Этот модуль отвечает за логи игры"""

from logging import Logger
import coloredlogs  # Для выделения особым цветом разных логов
import sys


class HELogger(Logger):
    """Этот класс дополняет класс из стандартной библиотеки Python"""
    
    def __init__(self, name, level):
        super().__init__(name, level)
        print("[INFO] Logger activated!")
    
    @staticmethod
    def better_info(logger: object) -> None:
        """
        Цвета для логов
        
        Args:
            logger (HELogger): Переменная для логов
        """
        try:
            if sys.argv[1] == "BETTER":
                coloredlogs.install(level='DEBUG', logger=logger)
        except IndexError:
            pass
    