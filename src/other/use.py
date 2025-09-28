"""Использование предметов"""

from ..other.globals import load, some_dict
from ..other.after_use import AfterUse
from ..game.saving import Saving
import pygame
import logging
from time import sleep
from ..entity.inventory import Inventory
import re

pygame.init()


class Use:
    """Кнопка использования"""

    save = Saving()

    def __init__(self, screen: pygame.surface.Surface, n: int,
                player: object) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__player: object = player
        self.__visible = 0
        self.__keys: list[str, ...] = self.save.load_save(n)["items_id"]
        self.__rects_list = []
        self.__item_visible = 0  # Отображение предмета при нажатии ЛКМ
        self.some_list = []
        self.__n: int = n
        self.__texture_id = ""
        self.to_dict()
        self.__button = load("textures/act.png", (70, 70), "convert_alpha")
        self.__button2 = load("textures/act2.png", (70, 70), "convert_alpha")
        self.__slot = load("textures/menu.png", (21, 21), "convert")
        self.__slot2 = load("textures/menu2.png", (21, 21), "convert")
        self.res = None
        self.__slot.set_alpha(96)
        self.__mouse_was_pressed = False

    def append(self, sl: dict) -> None:
        self.some_list.append(sl)

    def to_dict(self) -> None:
        """Из списка в словарь"""
        self.__from_num_to_texture()  # Для удаления повторов в списке
        lst = []
        for i in self.some_list:
            try:  # Для того, чтобы предметы не дублировались
                lst.append({i[1]: i[0]})
            except KeyError:
                pass
            except IndexError:
                lst.append({list(i[0].keys())[0]: list(i[0].values())[0]})
        self.some_list = lst
        logging.info("Завершена работа метода to_dict")

    def __from_num_to_texture(self) -> None:
        """
        От id к текстуре
        """
        logging.debug("Начало работы метода __from_num_to_texture")
        inv_list2 = []
        for i in self.__keys:  # Загрузка из строк в текстуры
            pattern = r"pygame\.image\.load\(['\"](.*?)['\"]\)"

            match = re.search(pattern, some_dict["items"][int(i)][4])
            inv_list2.append([load(match.group(1),
                                (60, 60), "convert_alpha"), i])
        self.some_list.extend(Inventory.inventory_list)
        self.some_list.extend(inv_list2)
        logging.debug("Конец работы метода __from_num_to_texture")

    def __draw_inventory_slots(self, index: list[int, int]) -> None:
        """
        Отрисовка инвентаря

        Args:
            index (list[int, int]): Позиция игрока на карте
        """
        x, y = 605, 75
        self.__rects_list.clear()

        for i in range(self.__player.MAX_CAPACITY):
            if i % 8 == 0 and i != 0:  # Перенос на новую строку
                y += 21
                x = 605
            self.__screen.blit(self.__slot, (x, y))
            try:
                texture = pygame.transform.scale(
                    list(self.some_list[i].values())[0], (20, 20)
                )
                self.__screen.blit(texture, (x + 2, y))
                self.__rects_list.append(
                    [
                        texture.get_rect(topleft=(x + 2, y)),
                        texture,
                        list(self.some_list[i].keys())[0],
                    ]
                )
            except AttributeError:
                texture = pygame.transform.scale(
                    list(self.some_list[i][0].values())[0], (20, 20)
                )
                self.__screen.blit(texture, (x + 2, y))
                self.__rects_list.append(
                    [
                        texture.get_rect(topleft=(x + 2, y)),
                        texture,
                        list(self.some_list[i][0].keys())[0],
                    ]
                )
            except IndexError:
                pass
            x += 21
        self.__after_click(index)

    def draw(self, pos: tuple[int, int], index: list[int, int]) -> None:
        """
        Отрисовка

        Args:
            pos (tuple[int, int]): Позиция мыши,
            index (list[int, int]): Позиция игрока на карте
        """
        self.__screen.blit(self.__button, (700, 0))
        rect = self.__button.get_rect(topleft=(700, 0))
        rect2 = self.__player.player.get_rect(
            topleft=(self.__player.x, self.__player.y)
        )

        if rect.collidepoint(pos):  # Кнопка действия
            self.__screen.blit(self.__button2, (700, 0))
            if pygame.mouse.get_pressed()[0]:
                sleep(0.10379)
                if not self.__visible:
                    self.__visible = 1
                else:
                    self.__visible = 0
        if rect.colliderect(rect2):  # Прозрачность кнопки, если в ней игрок
            self.__button.set_alpha(70)
        else:  # Непрозрачность кнопки
            self.__button.set_alpha(800)

        if self.__visible:  # Для открытия/сворачивания
            self.__draw_inventory_slots(index)

    def item_draw(self, mp: tuple[int, int],
                texture: pygame.surface.Surface) -> None:
        """
        Отрисовка применяемого предмета.

        Args:
            mp (tuple[int, int]): Позиция курсора мыши,
            texture (pygame.surface.Surface): Текстура выбранного предмета.
        """
        texture = pygame.transform.scale(texture, (55, 55))
        self.__screen.blit(texture, (mp[0] - 15, mp[1] - 15))

    def __after_click(self, index: list[int, int]) -> None:
        """Функционал после клика"""
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        mouse_pressed: tuple[bool, bool, bool] = pygame.mouse.get_pressed()[0]

        for i in self.__rects_list:
            if i[0].collidepoint(mouse_pos):
                self.__screen.blit(self.__slot2, (i[0][0], i[0][1]))
                self.__screen.blit(i[1], (i[0][0], i[0][1]))
                if mouse_pressed and not self.__mouse_was_pressed:
                    self.__item_visible = not self.__item_visible
                    self.res: pygame.surface.Surface = i[1]
                    self.__texture_id: int = i[2]

        self.__mouse_was_pressed: bool = self.handle_events(
            pygame.event.get())

        if self.__item_visible:  # Предмет на курсоре мыши
            self.item_draw(mouse_pos, self.res)
            if mouse_pressed and not self.__mouse_was_pressed:
                ae = AfterUse(self.__texture_id, index, self.__n)
                ae.functional(mouse_pos)

    def handle_events(self, events: list[pygame.event.Event]) -> bool:
        """
        Обработка событий мыши

        Args:
            events (list[pygame.event.Event]): Список событий Pygame.
        Returns:
            bool: Активация условного оператора.
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
