"""Этот модуль отвечает за логи игры"""

from logging import Logger


class HELogger(Logger):
    """Этот класс дополняет класс из стандартной библиотеки Python"""
    
    def __init__(self, name, level):
        super().__init__(name, level)
        print("[INFO] Logger activated!")
