"""Игрок игры House Escape"""

import pygame
import sys
from keyboard import is_pressed
from src.entity.move import Move
from ..game.logging import HELogger
from ..game.saving import Saving
from ..other.globals import font, load
from .character import Character
from .inventory import Inventory


pygame.init()


class Player(Character):
    """Игрок и связанное с ним"""
    MAX_CAPACITY = 8  # Максимум предметов в инвентаре
    
    def __init__(self, logger: HELogger,
                screen: pygame.surface.Surface, n: int) -> None:
        logger.info("Начата работа конструктора Player")
        self.__save = Saving()
        self.x = self.__save.load_save(n)["x"]  # Изначальное положение игрока по x
        self.y = self.__save.load_save(n)["y"]  # Изначальное положение игрока по y
        self.player = load("textures/player.png", (60, 60), "convert_alpha")
        self.__inventory = load("textures/backpack.png", 
                                (90, 90), "convert_alpha")
        Inventory.Player = self
        logger.debug("Статичному полю Player класса Inventory присвоен self")
        self.__screen = screen
        logger.info("Завершена работа конструктора Player")
        
    def __to_inventory(self, logger: HELogger, 
                    index: list[int, int], player: object, n: int) -> None:
        """
        Инвентарь игрока (открывается на E)
        
        Args:
            logger (HELogger): Переменная для логов,
            index (list[int, int]): Позиция игрока на карте,
            player (Player): Объект игрока,
            n (int): Номер выбранного сохранения.
        """
        logger.info("Открытие инвентаря")
        sound = pygame.mixer.Sound("textures/open.mp3")
        sound.set_volume(0.4)
        sound.play()
        inventory = Inventory(self.__inventory, self.__screen)
        inventory.open(index, player, n)
        logger.info("Закрытие инвентаря")
        
    def player_interfaces(self, screen: pygame.surface.Surface,
                        player: object) -> pygame.surface.Surface:
        """
        Интерфейсы игрока (инвентарь)
        
        Args:
            screen (pygame.surface.Surface): Переменная экрана,
            player (Player): Объект класса Player.
        Returns:
            pygame.surface.Surface: 'Квадрат' текстуры рюкзака (инвентаря)
                                    и игрока.
        """
        screen.blit(self.__inventory, (10, 10))
        rect = self.__inventory.get_rect(topleft=(10, 10))
        rect2 = self.player.get_rect(topleft=(player.x, player.y))
        if rect.colliderect(rect2):  # Рюкзак прозрачен, если в нём игрок.
            self.__inventory.set_alpha(95)
        else:
            self.__inventory.set_alpha(300)
        return rect, rect2
        
    def blit(self) -> pygame.surface.Surface:
        """
        Вывод игрока на экран
        
        Returns:
            pygame.surface.Surface: 'Квадрат' игрока.
        """
        self.__screen.blit(self.player, (self.x, self.y))
        return self.player.get_rect(topleft=(self.x, self.y))
        
    def get_stats(self, logger: HELogger) -> None:
        """
        Получение информации об игроке
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        logger.info("Получение информации об игроке")
        result: dict = Character.filter_data(self)
        super().get_stats(self.__screen, [self.x, self.y], result)
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
        cls.MAX_CAPACITY = mc
        logger.debug("Поля класса изменены!")
        
    def open_inventory(self, logger: HELogger, index: list[int, int],
                    player: object, rect: pygame.rect.Rect, n: int) -> None:
        """
        Открытие инвентаря
        
        Args:
            logger (HELogger): Переменная для логов,
            index (list[int, int]): Позиция игрока на карте,
            player (Player): Переменная игрока,
            rect (pygame.rect.Rect): 'Квадрат' рюкзака.
        """
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.__to_inventory(logger, index, player, n)
        
    def in_game(self, player: object, index: list[int, int], logger: HELogger,
                rect: pygame.surface.Surface, n: int) -> None:
        """
        Поведение игрока в игре

        Args:
            player (Player): Объект игрока,
            index (list[int, int]): Карта дома,
            logger (HELogger): Переменная для логов,
            rect (pygame.surface.Surface): 'Квадрат' рюкзака,
            n (int): Номер выбранного игроком сохранения.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Закрытие программы")
                self.__save.saving(index, player.x, player.y, n)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                logger.info(f"Нажата клавиша - {pygame.KEYDOWN}")
                if event.key == pygame.K_e:
                    self.__to_inventory(logger, index, player, n)
        if is_pressed("w") and Move.move_in_location(player.x, player.y, index) and self.y < 753:
            self.y -= 3 * self.speed
        elif is_pressed("a") and Move.move_in_location(player.x, player.y, index) and self.x > -23:
            self.x -= 3 * self.speed
        elif is_pressed("s") and Move.move_in_location(player.x, player.y, index) and self.y > -23:
            self.y += 3 * self.speed
        elif is_pressed("d") and Move.move_in_location(player.x, player.y, index) and self.x < 753:
            self.x += 3  * self.speed
        self.open_inventory(logger, index, player, rect, n)
        