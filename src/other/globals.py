"""Методы и поля, использующиеся в других файлах"""

import pygame


pygame.init()


screen = pygame.display.set_mode((770, 770))
font = pygame.font.Font("textures/font.otf", 43)
font2 = pygame.font.Font("textures/font.otf", 10)
font3 = pygame.font.Font("textures/font.otf", 25)
font4 = pygame.font.Font("textures/font.otf", 20)
some_dict = {
    "index": [3, 3], 
    "x": 385, 
    "y": 385, 
    "blocks": { 
        1: [450, 150, 3, 3,
            "pygame.image.load(\"textures/table.png\")"],
        2: [20, 320, 3, 3,
            "pygame.image.load(\"textures/boosty.png\")"]
    },
    "items": {  
        1: [150, 150, 3, 3,
            "pygame.image.load(\"textures/stick.png\")"],
        2: [320, 320, 3, 3,
            "pygame.image.load(\"textures/stone.png\")"]
    },
    "items_keys": []}
traps_dict = {
    1: [100, 100, 3, 3, "poison"]
}

def load(path: str, size: tuple[int, int], convert_type: str) -> pygame.surface.Surface:
    """
    Загрузка текстур
    
    Args:
        path (str): Путь к текстуре,
        size (tuple[int, int]): Размер текстуры,
        convert_type (str): Тип конвертации (convert, convert_alpha)
    Returns:
        pygame.surface.Surface: Загруженная текстура
    """
    if convert_type == "convert":
        return pygame.transform.scale(pygame.image.load(path).convert(), size)
    elif convert_type == "convert_alpha":
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(),
                                    size)
    