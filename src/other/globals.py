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
some_dict = {  # Эти данные в каждом файле в папке data
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
            "pygame.image.load(\"textures/poroh.png\")"],
        4: [0, 0, 9, 9,
            'pygame.image.load(\"textures/pickaxe.png\")',
            'textures/pickaxe.png'],
        5: [300, 300, 1, 1,
            'pygame.image.load(\'textures/paper.png\')'],
        6: [0, 0, 9, 9,
            'pygame.image.load(\'textures/tnt.png\')',
            'textures/tnt.png'],
        7: [0, 0, 9, 8, 'pygame.image.load(\"textures/key.png\")',
            'textures/key.png'],
        8: [0, 0, 9, 7, 'pygame.image.load(\"textures/kusachki.png\")',
            'textures/kusachki.png'],
        9: [0, 0, 9, 6, "pygame.image.load(\'textures/pila.png\')",
            'textures/pila.png'],
        10: [0, 0, 9, 5, "pygame.image.load(\'textures/shovel.png\')",
            'textures/shovel.png'],
        11: [0, 0, 9, 5, "pygame.image.load(\'textures/ognivo.png\')",
            'textures/ognivo.png']
    },
    "pictures": {
        1: [250, 200, 3, 2]
    },
    "enemys": {
        1: [550, 150, 3, 3, 'pygame.image.load(\"textures/watcher.png\")'],
        2: [20, 320, 3, 2, 'pygame.image.load(\"textures/stalker.png\")'],
        3: [20, 320, 2, 2, 'pygame.image.load(\"textures/blinder.png\")']
        },
    "MAX_CAPACITY": 8,
    "SPEED": 1,
    "FOV": 32,
    "items_id": [],
    "MON": 100,
    "money": {
        1: [300, 300, 1, 2, 100],
        2: [350, 250, 1, 3, 350]
    },
    "npc_products": {
        1: [150, "textures/key.png"],
        2: [350, "textures/kusachki.png"],
        3: [1000, "textures/pila.png"],
        4: [580, 'textures/shovel.png'],
        5: (475, 'textures/ognivo.png')
    }
}

traps_dict = {
    1: [100, 100, 3, 3, "poison"],
    2: [190, 590, 0, 2, "trap"],
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
    