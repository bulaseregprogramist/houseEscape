"""Экспериментальные функции"""

import pygame
import sys
from ..other.globals import font3, load
import json
from time import sleep


pygame.init()


class Experimental:

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__sound1 = pygame.mixer.Sound("textures/collect.mp3")
        self.__text1 = font3.render("Экспериментальные возможности", 1,
                                    (0, 0, 0))
        self.__checkmark1 = load("textures/checkmark1.png", (55, 55),
                                "convert")
        self.__checkmark2 = load("textures/checkmark2.png", (55, 55),
                                "convert")
        self.__rects_list = []
        self.__sound1.set_volume(0.41)
        self.dict_name = "EXPERIMENTS"  # Ключ словаря в файле settings.json
        self.load_settings()

        self.__text2 = font3.render("Гайд по API", 1, (0, 0, 0))
        self.__text3 = font3.render("Новые виды противников", 1, (0, 0, 0))
        self.__text4 = font3.render("Система здоровья", 1, (0, 0, 0))
        self.__text5 = font3.render("Внимание! Могут быть баги!", 1,
                                    (255, 0, 0))

    def load_settings(self) -> None:
        """Загрузка экспериментальных настроек"""
        with open("game_settings/settings.json") as file:
            self.__result: dict[str: dict[str: int] | int] = json.load(file)

    def save_settings(self) -> None:
        """Сохранение экспериментальных настроек"""
        with open("game_settings/settings.json", "w") as file:
            json.dump(self.__result, file, indent=2)

    def draw_experimental(self) -> None:
        """Отрисовка кнопочек и получение 'квадратов'"""
        self.__rects_list.clear()
        self.__screen.fill((255, 255, 255))
        self.__screen.blit(self.__text1, (150, 50))

        if not self.__result[self.dict_name]["1"]:
            self.__screen.blit(self.__checkmark1, (100, 100))
        else:
            self.__screen.blit(self.__checkmark2, (100, 100))
        if not self.__result[self.dict_name]["2"]:
            self.__screen.blit(self.__checkmark1, (100, 200))
        else:
            self.__screen.blit(self.__checkmark2, (100, 200))
        if not self.__result[self.dict_name]["3"]:
            self.__screen.blit(self.__checkmark1, (100, 300))
        else:
            self.__screen.blit(self.__checkmark2, (100, 300))

        self.__screen.blit(self.__text2, (190, 120))
        self.__screen.blit(self.__text3, (190, 220))
        self.__screen.blit(self.__text4, (190, 320))
        self.__screen.blit(self.__text5, (150, 420))

        self.__rects_list.append(
            self.__checkmark1.get_rect(topleft=(100, 100)))
        self.__rects_list.append(
            self.__checkmark1.get_rect(topleft=(100, 200)))
        self.__rects_list.append(
            self.__checkmark1.get_rect(topleft=(100, 300)))

    def off_on(self, mouse_pos: tuple[int, int]) -> None:
        """
        Взаимодействие с кнопками

        Args:
            mouse_pos (tuple[int, int]): Позиция курсора мыши.
        """
        key1, key2, key3 = "1", "2", "3"
        if (
            self.__rects_list[0].collidepoint(mouse_pos)
            and pygame.mouse.get_pressed()[0]
        ):
            if not self.__result[self.dict_name][key1]:
                sleep(0.4)
                self.__result[self.dict_name][key1] = 1
            elif self.__result[self.dict_name][key1]:
                sleep(0.4)
                self.__result[self.dict_name][key1] = 0

        elif (
            self.__rects_list[1].collidepoint(mouse_pos)
            and pygame.mouse.get_pressed()[0]
        ):
            if not self.__result[self.dict_name][key2]:
                sleep(0.4)
                self.__result[self.dict_name][key2] = 1
            elif self.__result[self.dict_name][key2]:
                sleep(0.4)
                self.__result[self.dict_name][key2] = 0

        elif (
            self.__rects_list[2].collidepoint(mouse_pos)
            and pygame.mouse.get_pressed()[0]
        ):
            if not self.__result[self.dict_name][key3]:
                sleep(0.4)
                self.__result[self.dict_name][key3] = 1
            elif self.__result[self.dict_name][key3]:
                sleep(0.4)
                self.__result[self.dict_name][key3] = 0

    def run(self) -> None:
        """Основной метод класса"""
        self.__sound1.play()
        cycle = 1
        while cycle:
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            self.draw_experimental()  # Отрисовка кнопок
            self.off_on(mouse_pos)  # Включение и выключение функций

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_settings()
                    sys.exit()
                elif (event.type == pygame.KEYDOWN 
                        and event.key == pygame.K_ESCAPE):
                    cycle = 0
