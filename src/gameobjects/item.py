"""Предметы игры"""

from ..other.configs import GameObjectsConfig, GameObjectsConfig2
from ..other.configs import GameObjectsConfig3
from src.gameobjects.gameobjects import GameObjects
import pygame
from ..entity.player import Player, change
from ..game.saving import Saving
from ..game.logging import HELogger
import json


pygame.init()


class Item(GameObjects):
    """Предметы в доме"""

    save = Saving()
    some_num = 1

    def __init__(self, logger: HELogger) -> None:
        self.__logger: HELogger = logger
        self.__logger.debug("Завершена работа конструктора класса Item")

    def placing(
        self, he_map: list[int, int], player: Player, n: int, have_functional=1
    ) -> None:
        """
        Размещение предмета

        Args:
            he_map (list[int, int]): Позиция игрока,
            player (Player): Игрок,
            n (int): Номер выбранного сохранения,
            have_functional (int): Выключается для анимаций
        """
        if self.some_num:  # Позиции предметов и их текстуры
            self.__items: dict[
                int: list, ...] = self.save.load_save(n)["items"]
        delete = 0
        for i in self.__items:
            texture = pygame.transform.scale(
                self._num_to_texture(self.__items[i][4]), (50, 50)
            )
            super().placing(
                GameObjectsConfig3(
                    self.__items[i][0],
                    self.__items[i][1],
                    [self.__items[i][2], self.__items[i][3]],
                    he_map, texture, player,
                )
            )
            if have_functional:
                delete, key = self.functional(
                    GameObjectsConfig(
                        self.__items[i][0],
                        self.__items[i][1],
                        texture, i, he_map,
                        [self.__items[i][2], self.__items[i][3]],
                    )
                )
            if delete:  # Чтобы не было бага
                break
        if delete:  # Помещение предмета в инвентарь
            self.__items.pop(key)
            self.__save_item(n)
            self.some_num = 0  # Для предотвращения повторного срабатывания УО

    def functional(self, config: tuple) -> int:
        """
        Функционал предметов

        Args:
            config (tuple): Параметры (конфиг) для предмета
        Returns:
            int: Два числа. Первое число отвечает за удаление из словаря,
                            второе за удаляемый ключ
        """
        result: int = super().functional(
            GameObjectsConfig2(
                config.x, config.y,
                config.texture, "item",
                config.he_map, config.location,
                config.i,
            )
        )
        if result == 1:  # Помещение предмета в инвентарь
            change()
            pygame.mixer.Sound("textures/press.mp3").play()
            self.__logger.debug("Данные успешно возвращены!")
            return 1, config.i  # Ключ будет удалён
        return 0, config.i  # Ключ не будет удалён

    def __save_item(self, n: int) -> None:
        """
        Сохранение предметов.

        Args:
            n (int): Номер выбранного сохранения.
        """
        some_dict: dict[str: int | dict | list] = self.save.load_save(n)
        some_dict["items"] = self.__items
        self.__logger.info("Предметы сохранены!")
        with open(f"data/data{n}.json", "w") as file:
            json.dump(some_dict, file, indent=2)
