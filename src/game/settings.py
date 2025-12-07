"""Настройки игры"""

import pygame
import sys

from ..game.saving import Saving
from ..other.globals import font, font5, load, font3
import json


pygame.init()


class Settings:
    """Основной класс"""

    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.__screen: pygame.surface.Surface = screen
        self.__text = font.render("Настройки", True, (255, 255, 255))
        self.__text2 = font5.render("Вкл/Выкл музыку", True, (255, 255, 255))
        self.__text3 = font5.render("Вкл/Выкл звуки", True, (255, 255, 255))
        self.__text4 = font3.render("Верт. синхронизация",
                                    True, (255, 255, 255))
        self.__text5 = font5.render("Полный экран", True, (255, 255, 255))
        self.__text6 = font5.render("Моды", True, (255, 255, 255))
        
        self.__text7 = font5.render("Управление", True, (255, 255, 255))
        self.__text8 = font5.render("Управление", True, (255, 247, 0))
        
        self.__checkmark1 = load("textures/checkmark1.png", (50, 50),
                                "convert")
        self.__checkmark2 = load("textures/checkmark2.png", (50, 50),
                                "convert")
        sound = pygame.mixer.Sound("textures/collect.mp3")
        sound.set_volume(0.4)
        sound.play()

        self.__music: int = self.check_music_activated()
        self.__sounds_on_off = 1
        self.__vsync = 1
        self.__fullscreen = 1
        self.__mods_on_off = 1
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
        self.__square = pygame.Surface((300, 90))
        self.__square.set_alpha(0)

        self.__screen.blit(self.__text, (250, 130))
        
        self.__screen.blit(self.__text2, (240, 186))
        self.__screen.blit(self.__text3, (240, 256))
        self.__screen.blit(self.__text4, (240, 326))
        self.__screen.blit(self.__text5, (240, 396))
        self.__screen.blit(self.__text6, (240, 466))
        
        self.__screen.blit(self.__text7, (270, 556))
        self.__screen.blit(self.__square, (240, 526))

        if self.__music:  # Музыка включена
            self.__screen.blit(self.__checkmark1, (170, 180))
        else:
            self.__screen.blit(self.__checkmark2, (170, 180))
        
        if self.__sounds_on_off:  # Звуки включены
            self.__screen.blit(self.__checkmark1, (170, 250))
        else:
            self.__screen.blit(self.__checkmark2, (170, 250))
        
        if self.__vsync:  # Верт. Синхронизация включена
            self.__screen.blit(self.__checkmark1, (170, 320))
        else:
            self.__screen.blit(self.__checkmark2, (170, 320))
        
        if self.__fullscreen:  # Полный экран включён
            self.__screen.blit(self.__checkmark1, (170, 390))
        else:
            self.__screen.blit(self.__checkmark2, (170, 390))
        
        if self.__mods_on_off:  # Моды включены
            self.__screen.blit(self.__checkmark1, (170, 460))
        else:
            self.__screen.blit(self.__checkmark2, (170, 460))
        self.main_functional()

    def main_functional(self) -> None:
        """Основной функционал настроек"""
        rect1 = self.__checkmark1.get_rect(topleft=(170, 180))
        rect2 = self.__checkmark2.get_rect(topleft=(170, 180))
        
        rect3 = self.__checkmark1.get_rect(topleft=(170, 250))
        rect4 = self.__checkmark2.get_rect(topleft=(170, 250))
        
        rect5 = self.__checkmark1.get_rect(topleft=(170, 320))
        rect6 = self.__checkmark2.get_rect(topleft=(170, 320))
        
        rect7 = self.__checkmark1.get_rect(topleft=(170, 390))
        rect8 = self.__checkmark2.get_rect(topleft=(170, 390))
        
        rect9 = self.__checkmark1.get_rect(topleft=(170, 460))
        rect10 = self.__checkmark2.get_rect(topleft=(170, 460))
        
        rect11 = self.__square.get_rect(topleft=(240, 526))

        try:
            if (rect1.collidepoint(pygame.mouse.get_pos())
                    and pygame.mouse.get_pressed()[0]):
                self.__music = 0
            elif rect2.collidepoint(
                pygame.mouse.get_pos() and pygame.mouse.get_pressed()[0]):
                self.__music = 1
        except TypeError:  # Если активировано одно из двух -- ошибка
            pass
        
        if (rect11.collidepoint(pygame.mouse.get_pos())):
            self.__screen.blit(self.__text8, (270, 556))

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

