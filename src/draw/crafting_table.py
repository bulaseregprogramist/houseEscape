"""Стол для создания предметов"""

import pygame
from ..game.saving import Saving
from ..entity.inventory import Inventory
from time import sleep
from ..other.globals import load, some_dict
from ..game.logging import HELogger
from ..entity.player import Player
from copy import copy
import sys
import json
import re
import logging


pygame.init()


class CraftingTable:
    save = Saving()
    logger: HELogger

    def __init__(
        self, screen: pygame.surface.Surface,
        text, n: int,
        index: list[int, int], player: Player,
    ) -> None:
        self.__index: list[int, int] = index
        self.__player: Player = player
        self.__screen: pygame.surface.Surface = screen
        self.__text = text
        self.__n: int = n
        self.__pickaxe = load("textures/pickaxe.png", (60, 60),
                            "convert_alpha")
        self.__keys: list[str, ...] = self.save.load_save(n)["items_id"]
        self.__some_list = copy(Inventory.inventory_list)
        self.__tnt = load("textures/tnt.png", (60, 60), "convert_alpha")
        self.__ntt(self.__keys)
        self.__rects_list = []
        self.__run()

    def __ntt(self, inv_list: list[str, ...]) -> None:
        """
        От id к текстуре

        Args:
            inv_list (list[str, ...]): Список с id.
        """
        logging.debug("Начало работы метода ntt")
        inv_list2 = []
        for i in inv_list:  # Загрузка текстур
            pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

            match = re.search(pattern, some_dict["items"][int(i)][4])
            inv_list2.append([load(match.group(1), (60, 60), "convert_alpha"),
                            i])
        self.__some_list.extend(inv_list2)
        logging.debug("Конец работы метода ntt")

    def __get_free_space(self,
                        texture: pygame.surface.Surface, y: int) -> None:
        """
        Сокращение кода (если предметов для крафта нет)

        Args:
            texture (pygame.surface.Surface): Текстура создаваемого предмета,
            y (int): Позиция создаваемого предмета по y
        """
        counter = 0
        for i in self.__some_list:
            try:
                if i[1] == "1" or i[1] == "2":
                    counter += 1
            except TypeError:
                pass
        if counter == 2:  # Отрисовка предметов инвентаря
            self.__screen.blit(texture, (120, y))
            self.__rects_list.append([texture.get_rect(topleft=(120, y)), 1])

    def __recipes(self) -> None:
        """Рецепты в верстаке"""
        self.__rects_list.clear()
        y = 180
        if "1" in self.__keys and "2" in self.__keys:
            self.__screen.blit(self.__pickaxe, (120, y))
            self.__rects_list.append([
                self.__pickaxe.get_rect(topleft=(120, y)), 1])
        else:
            self.__get_free_space(self.__pickaxe, y)
        y += 50
        if "3" in self.__keys and "5" in self.__keys:
            self.__screen.blit(self.__tnt, (120, y))
            self.__rects_list.append(
                [self.__tnt.get_rect(topleft=(120, y)), 2])
        else:
            self.__get_free_space(self.__tnt, y)
        y += 50
        self.__crafting()

    def __after_craft(self, new_item: str, *args: str) -> None:
        """
        После создания предмета

        Args:
            new_item (str): Предмет, который создали.
            *args (str): Предметы, необходимые для создания
        """
        with open(f"data/data{self.__n}.json") as file:
            result: dict[str : list | int | dict] = json.load(file)
        items_id: list[str, ...] = result["items_id"]
        for i in args:  # Удаление из списка
            try:
                items_id.remove(i)
                logging.debug(f"Потрачена вещь - {i}")
            except ValueError:
                pass
        items_id.append(new_item)
        self.__some_list.append(
            load(some_dict["items"][int(new_item)][5],
                (60, 60), "convert_alpha")
        )
        result["items_id"] = items_id
        with open(f"data/data{self.__n}.json", "w") as file:
            json.dump(result, file, indent=3)
        logging.debug("Данные обновлены!")

    def __crafting(self) -> None:
        """Крафты в верстаке"""
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        for i in self.__rects_list:
            if type(i[0]) is pygame.rect.Rect:
                if (i[0].collidepoint(mouse_pos) 
                        and pygame.mouse.get_pressed()[0]):
                    pygame.mixer.Sound("textures/open.mp3").play()
                    if i[1] == 1:
                        logging.info("Создана кирка!")
                        sleep(0.41)
                        self.__after_craft("4", "1", "2")
                    elif i[1] == 2:
                        logging.info("Создана взрывчатка!")
                        sleep(0.41)
                        self.__after_craft("6", "3", "5")
                    self.__some_list = copy(Inventory.inventory_list)
                    self.__some_list.extend(Inventory.inventory_list2)

    def __run(self) -> None:
        """Основной метод класса."""
        crafting_table_cycle = 1
        while crafting_table_cycle:
            pygame.draw.rect(self.__screen, (255, 255, 255), 
                            (100, 100, 570, 570))
            self.__screen.blit(self.__text, (139, 130))
            self.__recipes()
            x, y = 170, 490

            # Отрисовка предметов в инвентаре
            for i in range(len(self.__some_list)):
                try:  # УО нужен для отрисовки хранимых в инвентаре предметов.
                    self.__screen.blit(self.__some_list[i], (x, y))
                except TypeError:
                    self.__screen.blit(self.__some_list[i][0], (x, y))
                x += 70
                if (i + 1) % 6 == 0:  # Перенос предметов вниз.
                    x = 170
                    y += 70
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.logger.info("Выход из игры...")
                    self.save.saving(
                        self.__index, self.__player.x, 
                        self.__player.y, self.__n, True
                    )
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sleep(0.15)
                        crafting_table_cycle = 0
