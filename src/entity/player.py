"""Игрок игры House Escape"""

import pygame
import sys
from typing import Self
from src.entity.move import Move
from ..game.logging import HELogger
from ..game.saving import Saving
from ..other.globals import font, load, n
from ..other.use import Use
from .character import Character
from .inventory import Inventory
from ..other.configs import Config


pygame.init()
add = 0

def change() -> None:
    global add
    add = 1
    

class Player(Character):
    """Игрок и связанное с ним"""
    save = Saving()
    # Максимум предметов в инвентаре
    MAX_CAPACITY: int = save.load_save(n)["MAX_CAPACITY"]
    
    def __init__(self, logger: HELogger, screen, n: int) -> None:
        logger.info("Начата работа конструктора Player")
        self.__save = Saving()
        self.use = Use(screen, n, self)
        # Изначальное положение игрока по x и y
        self.x = self.__save.load_save(n)["x"]
        self.y = self.__save.load_save(n)["y"]
        self.player = load("textures/player.png", (60, 60), "convert_alpha")
        self.player2 = load("textures/player2.png", (60, 60), "convert_alpha")
        self.__inventory = load("textures/backpack.png", 
                                (90, 90), "convert_alpha")
        self.__inventory2 = load("textures/backpack2.png",
                                (90, 90), "convert_alpha")
        Inventory.Player = self
        logger.debug("Статичному полю Player класса Inventory присвоен self")
        self._screen: pygame.surface.Surface = screen
        logger.info("Завершена работа конструктора Player")
        
    def to_inventory(self, config: Config) -> None:
        """
        Инвентарь игрока (открывается на E)
        
        Args:
            config (Config): Объект класса Config
        """
        config.logger.info("Открытие инвентаря")
        sound = pygame.mixer.Sound("textures/open.mp3")
        sound.set_volume(0.4)
        sound.play()
        inventory = Inventory(self.__inventory, self.__inventory2,
                            self._screen)
        inventory.open(config.index, config.player, config.n,
                    config.logger, config.mouse_pos)
        config.logger.info("Закрытие инвентаря")
        
    def player_interfaces(self, *args) -> pygame.surface.Surface:
        """
        Интерфейсы игрока (инвентарь, кнопка использования)
        
        Args:
            *args (tuple): Экран игры, позиция мыши, расположение игрока
        Returns:
            pygame.surface.Surface: 'Квадрат' текстуры рюкзака (инвентаря)
                                    и игрока.
        """
        args[0].blit(self.__inventory, (10, 10))
        self.use.draw(args[2], args[3])
        rect = self.__inventory.get_rect(topleft=(10, 10))
        rect2 = self.player.get_rect(topleft=(args[1].x, args[1].y))
        if rect.colliderect(rect2):  # Рюкзак прозрачен, если в нём игрок.
            self.__inventory.set_alpha(95)
        else:
            self.__inventory.set_alpha(300)
        return rect, rect2
        
    def blit(self, mp: tuple[int, int]) -> pygame.surface.Surface:
        """
        Вывод игрока на экран
        
        Args:
            mp (tuple[int, int]): Позиция мыши.
        Returns:
            pygame.surface.Surface: 'Квадрат' игрока.
        """
        self._screen.blit(self.player, (self.x, self.y))
        rect = self.player.get_rect(topleft=(self.x, self.y))
        if rect.collidepoint(mp):  # Свечение игрока
            self._screen.blit(self.player2, (self.x, self.y))
        return rect  # Для того, чтобы получить информацию об игроке.
        
    def get_stats(self, logger: HELogger, indx: list[int, int],
                n: int) -> None:
        """
        Получение информации об игроке
        
        Args:
            logger (HELogger): Переменная для логов,
            indx (list[int, int]): Позиция на карте
            n (int): Номер выбранного сохранения
        """
        logger.info("Получение информации об игроке")
        result: dict = Character.filter_data(self)
        super().get_stats(self._screen, indx, n,
                        [self.x, self.y], logger, result)
        logger.info("Информация об игроке получена!")
    
    @staticmethod
    def die(screen: pygame.surface.Surface) -> None:
        """
        Смерть игрока
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана.
        """
        super(Player, Player).die()
        cycle = 1
        text = font.render("ВЫ УМЕРЛИ!", 1, (255, 0, 0))
        while cycle:
            screen.fill((0, 0, 0))
            screen.blit(text, (245, 300))
            pygame.display.flip()
            
            {sys.exit() for i in pygame.event.get() if i.type == pygame.QUIT}
        
    @classmethod
    def change_fields(cls, logger: HELogger, mc: int, speed: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            logger (HELogger): Переменная для логов,
            mc (int): Изменение статичного поля MAX_CAPACITY,
            speed (int): Изменение статичного поля speed.
        """
        logger.debug("Идёт смена полей класса...")
        super().change_fields(speed)
        cls.MAX_CAPACITY: int = mc
        logger.debug("Поля класса изменены!")
        
    def open_inventory(self, *args) -> None:
        """
        Открытие инвентаря
        
        Args:
            *args(tuple): Параметры игрока (позиция мыши, расположение, ...)
        """
        if args[3].collidepoint(args[5]):  # Свечение при наводке
            self._screen.blit(self.__inventory2, (10, 10))
            if pygame.mouse.get_pressed()[0]:
                self.to_inventory(Config(args[0], args[1], args[2],
                                        args[4], args[5]))
        
    def in_game(self, *args) -> None:
        """
        Поведение игрока в игре

        Args:
            *args(tuple): Параметры игрока (позиция мыши, расположение, ...)
        """
        global add
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                args[2].info("Закрытие программы")
                self.__save.saving(args[1], args[0].x, args[0].y, n, True)
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Открытие инвентаря
                Move.press_keydown(args[2], event, self, args[1], args[0], n,
                                args[5])
        self.x, self.y = Move.player_move(args[0], args[1], self.x, self.y,
                                        self.speed)
        self.open_inventory(args[2], args[1], args[0], args[3], n, args[5])
        if add:  # Удаление повторов в списке
            add = 0
            self.use.to_dict()
        