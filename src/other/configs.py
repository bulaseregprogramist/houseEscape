"""Файл, содержащий класс для того, чтобы не было много аргументов"""

import pygame


pygame.init()


class Config:
    """Класс, содержащий все константы"""

    def __init__(
        self, logger, index: list[int, int], player, num: int, mp: tuple[int, int]
    ):
        self.logger = logger
        self.index: list[int, int] = index
        self.player = player
        self.n: int = num
        self.mouse_pos: tuple[int, int] = mp


class StatsConfig:
    """Класс для информации о персонаже"""

    def __init__(
        self,
        screen: pygame.surface.Surface,
        index: list[int, int],
        logger,
        ch: list[int, int],
        n: int,
        player,
    ):
        self.screen = screen
        self.index: list[int, int] = index
        self.logger = logger
        self.ch: list[int, int] = ch
        self.n: int = n
        self.player = player


class MainMenuConfig:
    """Класс с конфигом для главном меню"""

    def __init__(
        self,
        mouse_pos: tuple[int, int],
        screen: pygame.surface.Surface,
        textures: tuple,
        logger,
        mmc: int,
    ):
        self.screen = screen
        self.mouse_pos: tuple[int, int] = mouse_pos
        self.textures: tuple = textures
        self.logger = logger
        self.mmc: int = mmc


class GameObjectsConfig:
    """Конфиг для игровых объектов"""

    def __init__(
        self,
        x: int,
        y: int,
        texture,
        index: int,
        he_map: list[int, int],
        location: list[int, int],
    ) -> None:
        self.x = x
        self.y = y
        self.texture = texture
        self.i = index
        self.he_map: list[int, int] = he_map
        self.location: list[int, int] = location


class GameObjectsConfig2:
    """Конфиг для игровых объектов"""

    def __init__(
        self,
        x: int,
        y: int,
        texture,
        name: str,
        he_map: list[int, int],
        location: list[int, int],
        i: int,
    ) -> None:
        self.x = x
        self.y = y
        self.texture = texture
        self.name: str = name
        self.he_map: list[int, int] = he_map
        self.location: list[int, int] = location
        self.i = i


class GameObjectsConfig3:
    """Конфиг для игровых объектов (блоки)"""

    def __init__(
        self, x: int, y: int, some_list: list, he_map: list[int, int], texture, player
    ) -> None:
        self.x = x
        self.y = y
        self.some_list = some_list
        self.he_map: list[int, int] = he_map
        self.texture = texture
        self.player = player


class GameObjectsConfig4:
    """Конфиг для игровых объектов (блоки, интерфейсы)"""

    def __init__(
        self, i: int, screen, n: int, he_map: list[int, int], player, logger, use
    ) -> None:
        self.i: int = i
        self.screen = screen
        self.n: int = n
        self.he_map = he_map
        self.player = player
        self.logger = logger
        self.use = use


class GameObjectsConfig5:
    """Конфиг для игровых объектов"""

    def __init__(
        self,
        x: int,
        y: int,
        texture,
        he_map: list[int, int],
        some_list: list,
        i: int,
        n: int,
        player,
        use,
    ) -> None:
        self.x = x
        self.y = y
        self.texture = texture
        self.he_map: list[int, int] = he_map
        self.some_list = some_list
        self.i: int = i
        self.n: int = n
        self.player = player
        self.use = use
