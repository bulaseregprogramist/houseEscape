"""Подвал"""

import pygame
from ..entity.player import Player
from ..game.logging import HELogger
from ..other.globals import load
from keyboard import is_pressed
from ..draw.pause import Pause


pygame.init()


class Basement(Player):
    """Подвал дома"""
    __map = [
        "111"
        "111"
        "111"
    ]
    
    def __init__(self, logger: HELogger,
                screen: pygame.surface.Surface, n: int) -> None:
        super().__init__(logger, screen, n)
        self.__logger = logger
        self.__n: int = n
        self.__index = [3, 2]
        self.__pl = Player(logger, screen, n)
        self.__room = load("textures/broom.png", (770, 770), "convert")
        self.__arrow = load("textures/arrow.png", (50, 50), "convert")
        self.__arrow2 = load("textures/arrow2.png", (50, 50), "convert")
        self.__clock = pygame.time.Clock()
        self.__run()
        
    def draw(self, mouse_pos: tuple[int, int]) -> int:
        """
        Отрисовка локаций и кнопки выхода
        
        Args:
            mouse_pos (tuple[int, int]): Позиция курсора мыши
        Returns:
            int: Оставит цикл включённым или выключит его
        """
        self._screen.blit(self.__room, (0, 0))
        self._screen.blit(self.__arrow, (370, 0))
        
        rect = self.__arrow.get_rect(topleft=(370, 0))
        if rect.collidepoint(mouse_pos):
            self._screen.blit(self.__arrow2, (370, 0))
            if pygame.mouse.get_pressed()[0]:
                return self.exit()
        return 1
        
    def exit(self) -> None:
        """Выход из подвала"""
        self.__logger.info("Выход из подвала...")
        return 0
    
    def __move(self, player: Player) -> None:
        """
        Проверка на выход за границу карты дома (вторая часть)
        
        Args:
            player (Player): Объект игрока
        """
        print(self.__index)
        if player.x < 0:
            self.__p.x, self.__pl.y = 385, 385
            self.__index[0] -= 1
        elif player.y < 0:
            self.__pl.x, self.__pl.y = 385, 385
            self.__index[1] -= 1
        elif player.x > 770:
            self.__pl.x, self.__pl.y = 385, 385
            self.__index[0] += 1
        elif player.y > 770:
            self.__p.x, self.__pl.y = 385, 385
            self.__index[1] += 1
        
    def __run(self) -> None:
        """Основной метод класса."""
        cycle = 1
        while cycle:
            self.__clock.tick(60)
            mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
            
            cycle: int = self.draw(mouse_pos)
            rect = self.blit(mouse_pos)
            rect2, rect3 = self.player_interfaces(
                self._screen, self.__pl, mouse_pos)
            self.in_game(self.__pl, self.__index, self.__logger,
                        rect2, self.__n, mouse_pos)
            self.__move(self.__pl)
            # Информация об игроке
            if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                self.get_stats(self.__logger)
            pygame.display.flip()
            if is_pressed("esc"):
                pause = Pause(self._screen, self.__logger, self.__index,
                    self.__pl, self.__n)
                cycle: int = pause.run()

