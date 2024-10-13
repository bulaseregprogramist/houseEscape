"""Методы и поля, использующиеся в других файлах"""

import pygame
from os import listdir


pygame.init()


screen = pygame.display.set_mode((770, 770))
font = pygame.font.Font("textures/font.otf", 43)
font2 = pygame.font.Font("textures/font.otf", 10)
font3 = pygame.font.Font("textures/font.otf", 25)
font4 = pygame.font.Font("textures/font.otf", 20)

n = len(listdir("data/"))
if n == 0:
    n += 1
some_dict = {
    "index": [3, 3], 
    "x": 385, 
    "y": 385, 
    "blocks": { 
        1: [450, 150, 3, 3,
            "pygame.image.load(\"textures/table.png\")"],
        2: [120, 320, 3, 3,
            "pygame.image.load(\"textures/lamp.png\")"],
        3: [320, 470, 3, 2,
            "pygame.image.load(\"textures/trapdoor.png\")"]
    },
    "items": {  
        1: [150, 150, 3, 3,
            "pygame.image.load(\"textures/stick.png\")"],
        2: [320, 320, 3, 3,
            "pygame.image.load(\"textures/stone.png\")"],
        3: [220, 220, 3, 1,
            "pygame.image.load(\"textures/poroh.png\")"]
    },
    "enemys": {
        1: [550, 150, 3, 3, 'pygame.image.load(\"textures/watcher.png\")'],
        2: [20, 320, 3, 2, 'pygame.image.load(\"textures/stalker.png\")'],
        3: [20, 320, 2, 2, 'pygame.image.load(\"textures/blinder.png\")']
        },
    "MAX_CAPACITY": 8,
    "SPEED": 1,
    "FOV": 32,
    "items_id": []}

traps_dict = {
    1: [100, 100, 3, 3, "poison"],
    2: [190, 190, 0, 2, "trap"],
    3: [110, 110, 2, 1, "ice"]
}

def load(path: str, size: tuple[int, int],
        convert_type: str) -> pygame.surface.Surface:
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
    