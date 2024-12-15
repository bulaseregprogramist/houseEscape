"""Файл, содержащий класс для того, чтобы не было много аргументов"""


class Config:
    """Класс, содержащий все константы"""
    
    def __init__(self, logger, index: list[int, int], player, num: int,
                mp: tuple[int, int]):
        self.logger = logger
        self.index: list[int, int] = index
        self.player = player
        self.n: int = num
        self.mouse_pos: tuple[int, int] = mp
        
        