"""Персонаж"""

from abc import abstractmethod, ABC
import sys  # Только для sys.exit()
import pygame
from ..other.globals import load, font2, n  # load - загрузка текстур.
from ..game.saving import Saving
from time import sleep
from copy import copy


pygame.init()


class Character(ABC):
    """Персонаж (игрок, монстр, нпс (торговец))"""

    save = Saving()
    speed: int = save.load_save(n)["SPEED"]

    @classmethod
    @abstractmethod
    def change_fields(cls, speed: int) -> None:
        """
        Изменяет статичные поля класса

        Args:
            speed (int): Скорость персонажа
        """
        cls.speed = speed

    @abstractmethod
    def get_stats(self, config: object, *args: dict) -> None:
        """
        Получение информации об персонаже.

        Args:
            config (StatsConfig): Информация о персонаже,
            *args (dict): Статичные поля класса.
        """
        data_menu_cycle, y = 1, config.ch[1] - 30
        y2: int = copy(y)
        menu = load("textures/menu.png", (152, 150), "convert")
        texts_list = [
            font2.render(str(i), 1, (255, 255, 255)) for i in args[0].values()
        ]
        while data_menu_cycle:  # Цикл нужен для отображения меню персонажа
            config.screen.blit(menu, (config.ch[0] - 30, config.ch[1] - 30))
            config.screen.blit(config.player.player, 
                            (config.player.x, config.player.y))

            for j in texts_list:  # Вывод характеристик персонажа
                config.screen.blit(j, (config.ch[0] - 30, y))
                y += 25
            y = copy(y2)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.logger.info("Выход из игры...")
                    self.save.saving(
                        config.index, config.ch[0], config.ch[1],
                        config.n, True
                    )
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    sleep(0.15)
                    data_menu_cycle = 0

    @staticmethod
    def filter_data(dct: dict) -> dict:
        """
        Для получения статичных полей

        Args:
            dct (dict): Статичные поля класса.
        Returns:
            dict: Отфильтрованные поля класса.
        """
        class_attributes = {
            key: value
            for key, value in dct.__dict__.items()
            if not callable(value)
            and not key.startswith("__")
            and not isinstance(value, classmethod)
            and not key.startswith("_")
            or key.isupper()
        }
        # Возвращение атрибутов класса
        return class_attributes

    @staticmethod
    @abstractmethod
    def die() -> None:
        """Смерть персонажа"""
        sound = pygame.mixer.Sound("textures/die.mp3")
        sound.set_volume(0.4)
        sound.play()
