"""Меню сохранений"""

import pygame
from ..other.globals import load, font4, some_dict
from ..game.logging import HELogger
from os import listdir
from time import sleep
import json
import sys


pygame.init()


class SaveMenu:
    """Основной класс для меню"""
    
    def __init__(self, screen: pygame.surface.Surface,
                logger: HELogger) -> None:
        self.__logger = logger
        self.__bg = load("textures/sm.png", (220, 770), "convert")
        self.__st = font4.render("СОХРАНЕНИЕ", 1, (255, 255, 255))
        self.__screen = screen
        self.__plus = load("textures/plus.png", (40, 40), "convert_alpha")
        self.number = self.__start()
        
    def create_save(self) -> None:
        """Создание сохранения"""
        sleep(0.5)
        sl: list = listdir("data/")
        if len(sl) < 5:  # Если кол-во сохранений меньше 5.
            with open(f"data/data{len(sl) + 1}.json", "w") as file:
                json.dump(some_dict, file, indent=3)
            self.__logger.debug("Сохранение успешно создано!")
        else:
            self.__logger.error("Превышено максимальное кол-во сохранений")
    
    def __start(self) -> int:
        """
        Запуск меню сохранений
        
        Returns:
            int: Номер выбранного сохранения.
        """
        save_menu_cycle = 1
        rects_list = []
        while save_menu_cycle:
            saves_list = listdir("data/")
            
            self.__screen.fill((50, 50, 50))
            self.__screen.blit(self.__bg, (270, 0))
            self.__screen.blit(self.__plus, (550, 1))
            rects_list.clear()
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            rect = self.__plus.get_rect(topleft=(550, 1))
            
            y = 60
            for _ in saves_list:  # Отрисовка сохранений
                self.__screen.blit(self.__st, (310, y))
                rects_list.append(self.__st.get_rect(topleft=(310, y)))
                y += 40
                
            for j in range(len(rects_list)):  # Запуск сохранения
                if (rects_list[j].collidepoint(mouse_pos)
                        and pygame.mouse.get_pressed()[0]):
                    return j  # Номер сохранения
            pygame.display.flip()
            if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                self.__logger.info("Идёт создание сохранения")
                self.create_save()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__logger.info("Выход из игры...")
                    sys.exit()
    