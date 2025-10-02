from random import randint
from ..entity.player import Player

class MonsterMove:
    def __init__(self, monster_speed: int, player: Player = None) -> None:
        self.speed = monster_speed
        self.__direction = 0
        self.__rand_direction = randint(1, 2)
        self.__moving_right = True
        if player is not None:  # Если есть игрок, то запоминаем его позицию.
            self.px: int = player.x
            self.py: int = player.y

    def move1(self, x: int, y: int) -> tuple[int, int]:
        """
        Асинхронное движение Watcher (влево-вправо или вверх-вниз).
        
        Args:
            x (int): Позиция монстра по x
            y (int): Позиция монстра по y
        Returns:
            tuple[int, int]: Новая позиция монстра по x и y
        """
        if self.__rand_direction == 1:  # Горизонтальное движение
            if x > 100 and not self.__direction:
                x -= 4.3
                if 101 <= x <= 107:
                    self.__direction = 1
            if x < 680 and self.__direction:
                x += 4.3
            if x > 680:
                self.__direction = 0
        else:  # Вертикальное движение
            if y > 100 and not self.__direction:
                y -= 4.3
                if 101 <= y <= 107:
                    self.__direction = 1
            if y < 680 and self.__direction:
                y += 4.3
            if y > 680:
                self.__direction = 0
        return x, y

    def move2(self, x: int, y: int) -> tuple[int, int]:
        """
        Асинхронное движение Blinder (диагональное).
        
        Args:
            x (int): Позиция монстра по x
            y (int): Позиция монстра по y
        Returns:
            tuple[int, int]: Новая позиция монстра по x и y
        """
        if self.__moving_right:
            if x < 770:
                x += self.speed
            if y < 770:
                y += self.speed
            if x >= 770 and y >= 770:
                self.__moving_right = False
        else:
            if x > 0:
                x -= self.speed
            if y > 0:
                y -= self.speed
            if x <= 0 and y <= 0:
                self.__moving_right = True
        return x, y

    def move3(self, x: int, y: int) -> tuple[int, int]:
        """
        Асинхронное движение Stalker (преследование игрока).
        
        Args:
            x (int): Позиция монстра по x
            y (int): Позиция монстра по y
        Returns:
            tuple[int, int]: Новая позиция монстра по x и y
        """
        if self.px > x:
            x += self.speed
        if self.py > y:
            y += self.speed
        if self.px < x:
            x -= self.speed
        if self.py < y:
            y -= self.speed
        return x, y