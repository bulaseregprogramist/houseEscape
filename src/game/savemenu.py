"""Меню сохранений"""

import pygame
from ..other.globals import load, font4, some_dict
from ..game.logging import HELogger
from os import listdir, remove
from time import sleep
from typing import Any
import json
import sys


pygame.init()


class SaveMenu:
    """Основной класс для меню"""
    
    def __init__(self, screen: pygame.surface.Surface,
                logger: HELogger) -> None:
        self.__logger: HELogger = logger
        self.__bg = load("textures/sm.png", (220, 770), "convert")
        self.__st = font4.render("СОХРАНЕНИЕ", 1, (255, 255, 255))
        self.__st2 = font4.render("СОХРАНЕНИЕ", 1, (229, 255, 0))
        self.__screen: pygame.surface.Surface = screen
        self.__plus = load("textures/plus.png", (40, 40), "convert_alpha")
        self.__plus2 = load("textures/plus2.png", (40, 40), "convert_alpha")
        self.__delete = load("textures/delete.png", (40, 40), "convert_alpha")
        self.__delete2 = load("textures/delete2.png", (40, 40),
                            "convert_alpha")
        self.__to_menu = load("textures/to_menu.png",
                            (45, 45), "convert_alpha")
        self.__to_menu2 = load("textures/to_menu2.png",
                            (45, 45), "convert_alpha")
        self.number = self.__start()  # Количество сохранений в папке data
        
    def create_save(self) -> None:
        """Создание сохранения"""
        sleep(0.5)
        sl: list[str, ...] = listdir("data/")  # Получение кол-ва сохранений
        if len(sl) < 5:  # Если кол-во сохранений меньше 5.
            with open(f"data/data{len(sl) + 1}.json", "w",
                    encoding="utf-8") as file:
                json.dump(some_dict, file, indent=2)
            self.__logger.debug("Сохранение успешно создано!")
        else:
            self.__logger.error("Превышено максимальное кол-во сохранений")
            
    def delete_save(self) -> None:
        """Удаление сохранений"""
        sleep(0.5)
        saves: list[str, ...] = listdir("data/")
        
        try:
            remove(f"data/data{len(saves)}.json")
            self.__logger.info("Сохранение удалено!")
        except FileNotFoundError:
            self.__logger.error("Ошибка. Сохранений у игрока нет!")
        self.__logger.debug("Метод delete_save завершил работу!")

    def draw(self, rects_list: list, saves_list: list[str, ...]) -> Any:
        """
        Отрисовка меню сохранений
        
        Args:
            rects_list (list[pygame.rect.Rect, ...]): Список с 'квадратами',
            saves_list (list[str, ...]): Список с сохранениями.
        Returns:
            pygame.rect.Rect: 'Квадрат' плюса, креста, выхода из меню,
            tuple[int, int]: Позиция мыши.
        """
        self.__screen.fill((50, 50, 50))
        self.__screen.blit(self.__bg, (270, 0))
        self.__screen.blit(self.__plus, (550, 1))
        self.__screen.blit(self.__delete, (600, 1))
        self.__screen.blit(self.__to_menu, (5, 5))
        
        rects_list.clear()
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        rect = self.__plus.get_rect(topleft=(550, 1))
        rect2 = self.__delete.get_rect(topleft=(600, 1))
        rect3 = self.__to_menu.get_rect(topleft=(5, 5))
            
        y = 60
        for _ in saves_list:  # Отрисовка сохранений
            self.__screen.blit(self.__st, (310, y))
            rects_list.append(self.__st.get_rect(topleft=(310, y)))
            y += 40
        return rect, rect2, rect3, mouse_pos
    
    def __act(self, rect, rect2, rect3, mouse_pos: tuple[int, int]) -> int:
        """
        Действия в меню сохранений
        
        Args:
            rect (pygame.rect.Rect): 'Квадрат' кнопки плюс,
            rect2 (pygame.rect.Rect): 'Квадрат' кнопки минус,
            rect3 (pygame.rect.Rect): 'Квадрат' кнопки выхода в главное меню.
            mouse_pos (tuple[int, int]): Позиция курсора мыши.
        Returns:
            int: Выключение цикла, если нажата кнопку выхода в главное меню.
        """
        if rect.collidepoint(mouse_pos):  # Создание сохранения
            self.__screen.blit(self.__plus2, (550, 1))
            if pygame.mouse.get_pressed()[0]:
                self.__logger.info("Идёт создание сохранения")
                self.create_save()
        elif rect2.collidepoint(mouse_pos):  # Удаление сохранения
            self.__screen.blit(self.__delete2, (600, 1))
            if pygame.mouse.get_pressed()[0]:
                self.__logger.info("Идёт удаление сохранения")
                self.delete_save()
        elif rect3.collidepoint(mouse_pos):  # Выход в главное меню
            self.__screen.blit(self.__to_menu2, (5, 5))
            if pygame.mouse.get_pressed()[0]:
                self.__logger.info("Выход из меню сохранений")
                return 0
        return 1
                    
    def __start(self) -> int | str:
        """
        Запуск меню сохранений
        
        Returns:
            int | str: Номер выбранного сохранения или выход в главное меню.
        """
        save_menu_cycle = 1
        rects_list = []
        while save_menu_cycle:
            saves_list: list[str, ...] = listdir("data/")
            rect, rect2, rect3, mouse_pos = self.draw(rects_list, saves_list)
            
            for j in range(len(rects_list)):  # Запуск (перечисление)
                if rects_list[j].collidepoint(mouse_pos):  # Свечение
                    self.__screen.blit(self.__st2, (310, rects_list[j][1]))
                    if pygame.mouse.get_pressed()[0]:  # Запуск
                        return j + 1  # Номер сохранения
                
            save_menu_cycle: int = self.__act(rect, rect2, rect3, mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__logger.info("Выход из игры...")
                    sys.exit()
            pygame.display.flip()
        return 'to_menu'
    