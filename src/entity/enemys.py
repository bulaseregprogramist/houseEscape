"""Враги в игре"""

from ..entity.character import Character
from ..entity.player import Player
from ..entity.monster_move import MonsterMove
from ..game.logging import HELogger
from ..game.saving import Saving
from ..other.globals import n, load
import pygame
import re


pygame.init()


class Enemy(Character):
    """Враги игрока"""
    save = Saving()
    enemy_dict: dict[int: list, ...] = save.load_save(n)["enemys"]
    field_of_view: int = save.load_save(n)["FOV"]  # FOV
    
    def __init__(self, x: int, y: int, enemy_type: str, screen) -> None:
        self.__screen = screen
        self.x = x
        self.y = y
        # В enemy_type может быть watcher, blinder, stalker
        self.__enemy_type: str = enemy_type
        self.__mm = MonsterMove()
        
    @classmethod
    def change_fields(cls, logger: HELogger, speed: int, fov: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            logger (HELogger): Переменная для логов,
            speed (int): Изменение статичного поля speed,
            fov (int): Поле зрения врага.
        """
        logger.debug("Идёт смена полей класса...")
        super().change_fields(speed)
        cls.field_of_view: int = fov
        logger.debug("Поля класса изменены!")
        
    def get_stats(self, logger: HELogger) -> None:
        """
        Получение информации о враге
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        logger.info("Получение информации об враге")
        result: dict = Character.filter_data()
        super().get_stats(self.__screen, [self.x, self.y], result)
        logger.info("Информация о враге получена!")
        
    def __to_texture(self, command: str) -> pygame.surface.Surface:
        """
        От команды к текстуре в игре.
        
        Args:
            command (str): Команда для загрузки текстуры монстра.
        Returns:
            pygame.surface.Surface: Текстура монстра.
        """
        pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

        match = re.search(pattern, command)
        return load(match.group(1), (60, 60), "convert_alpha")
    
    @staticmethod
    def die(logger: HELogger) -> None:
        """
        Смерть врага
        
        Args:
            logger (HELogger): Переменная для логов.
        """
        super().die()
        logger.info("Враг побеждён!")
        
    def draw_fov(self, player: Player, mp: tuple[int, int]) -> None:
        """
        Отрисовка поля зрения врага и вычисление
        соприкосновения с игроком
        
        Args:
            player (Player): Объект игрока,
            mp (tuple[int, int]): Позиция курсора мыши
        """
        pygame.draw.circle(self.__screen, (255, 0, 0),
                        (self.x + 25, self.y + 35), self.field_of_view, 4)
        if self.check_collision(player) or self.check_collision2(mp):
            Player.die(self.__screen)
        
    def check_collision(self, player: Player) -> bool:
        """
        Проверка на столкновение с игроком
        
        Args:
            player (Player | tuple[int, int]): Объект игрока.
        Returns:
            bool: Проверка на соприкосновение
        """
        distance_squared: float = (
            player.x - (self.x + 25)) ** 2 + (
                player.y - (self.y + 35)) ** 2
        return distance_squared <= (self.field_of_view + 30) ** 2
                
    def check_collision2(self, mp: tuple[int, int]) -> bool:
        """
        Проверка на столкновение с нажатым курсором мыши игрока.
        
        Args:
            mp (tuple[int, int]): Позиция мыши
        Returns:
            bool: Проверка на соприкосновение
        """
        distance_squared: float = (
            mp[0] - (self.x + 25)) ** 2 + (
                mp[1] - (self.y + 35)) ** 2
        return (distance_squared <= (self.field_of_view + 30) ** 2
                and pygame.mouse.get_pressed()[0])
    
    def enemy_draw_and_move(self, player: Player, mp: tuple[int, int]) -> int:
        """
        Движение и отрисовка врага (AI)
        
        Args:
            player (Player): Объект игрока,
            mp (tuple[int, int]): Позиция мыши.
        Returns:
            int: x и y врага.
        """
        self.draw_fov(player, mp)
        if self.__enemy_type == "watcher":
            self.__screen.blit(self.__to_texture(self.enemy_dict['1'][4]),
                            (self.x, self.y))
            self.x, self.y = self.__mm.move1(self.x, self.y)
        elif self.__enemy_type == "blinder":
            self.__screen.blit(self.__to_texture(self.enemy_dict['3'][4]),
                            (self.x, self.y))
            self.x, self.y =  self.__mm.move2(self.x, self.y)
        elif self.__enemy_type == "stalker":
            self.__screen.blit(self.__to_texture(self.enemy_dict['2'][4]),
                            (self.x, self.y))
            self.x, self.y = self.__mm.move3(self.x, self.y)
        return self.x, self.y
    