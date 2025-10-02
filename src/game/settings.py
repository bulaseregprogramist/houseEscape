"""Настройки игры"""

import pygame
import sys

from ..game.saving import Saving
from ..other.globals import font, font5, load
import json


pygame.init()


class Settings:
    """Основной класс"""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__text = font.render("Настройки", True, (255, 255, 255))
        self.__text2 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        self.__text3 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        self.__text4 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        self.__text5 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        self.__text6 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        
        self.__checkmark1 = load("textures/checkmark1.png", (50, 50),
                                "convert")
        self.__checkmark2 = load("textures/checkmark2.png", (50, 50),
                                "convert")
        sound = pygame.mixer.Sound("textures/collect.mp3")
        sound.set_volume(0.4)
        sound.play()

        self.__music: int = self.check_music_activated()
        self.__run()

    def check_music_activated(self) -> int:
        """
        Проверка, включена ли музыка

        Returns:
            int: Включена ли музыка.
        """
        with open("game_settings/settings.json") as file:
            result: int = json.load(file)["MUSIC"]
        return result  # Для УО (0 или 1)

    def draw_settings(self) -> None:
        """Отрисовка кнопочек"""
        pygame.draw.rect(self.__screen, (35, 25, 25), (90, 90, 590, 590))
        pygame.draw.rect(self.__screen, (0, 0, 230), (120, 120, 530, 530))

        self.__screen.blit(self.__text, (250, 130))
        
        self.__screen.blit(self.__text2, (240, 186))
        self.__screen.blit(self.__text3, (240, 256))
        self.__screen.blit(self.__text4, (240, 326))
        self.__screen.blit(self.__text5, (240, 396))
        self.__screen.blit(self.__text6, (240, 466))

        if self.__music:  # Музыка включена
            self.__screen.blit(self.__checkmark1, (170, 180))
        else:
            self.__screen.blit(self.__checkmark2, (170, 180))
            
        self.__screen.blit(self.__checkmark1, (170, 250))
        self.__screen.blit(self.__checkmark1, (170, 320))
        self.__screen.blit(self.__checkmark1, (170, 390))
        self.__screen.blit(self.__checkmark1, (170, 460))
        self.main_functional()

    def main_functional(self) -> None:
        """Основной функционал настроек"""
        rect1 = self.__checkmark1.get_rect(topleft=(170, 180))
        rect2 = self.__checkmark2.get_rect(topleft=(170, 180))

        try:
            if (rect1.collidepoint(pygame.mouse.get_pos())
                and pygame.mouse.get_pressed()[0]):
                self.__music = 0
            elif rect2.collidepoint(
                pygame.mouse.get_pos() and pygame.mouse.get_pressed()[0]):
                self.__music = 1
        except TypeError:  # Если активировано одно из двух -- ошибка
            pass

    def __run(self) -> None:
        """Основной метод класса"""
        cycle = 1
        while cycle:
            self.draw_settings()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if (event.type == pygame.KEYDOWN 
                            and event.key == pygame.K_ESCAPE):
                        Saving.save_music(self.__music)
                        cycle = 0
