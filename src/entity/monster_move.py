"""Движение монстра (врага)"""

from random import randint
from ..entity.player import Player


class MonsterMove:
    __direction = 0
    __rand_direction = randint(1, 2)  # Для watcher'a
    
    def __init__(self, monster_speed: int, player: Player = None) -> None:
        self.speed = monster_speed
        self.__moving_right = 1  # Для blinder'a
        if player is not None:  # stalker требует координат игрока
            self.px = player.x
            self.py = player.y
    
    @classmethod
    def move1(cls, x: int, y: int) -> int:
        """
        Движение watcher'a (влево-вправо или вверх-вниз)
        
        Args:
            x (int): Позиция watcher'a по x,
            y (int): Позиция watcher'a по y
        Returns:
            int: Изменённые координаты watcher'a
        """
        if cls.__rand_direction == 1:  # Влево-вправо
            if x > 100 and not cls.__direction:
                x -= 4.3
                if 101 <= x <= 107:
                    cls.__direction = 1
            if x < 680 and cls.__direction:
                x += 4.3
            if x > 680:  # Идёт налево
                cls.__direction = 0
        else:  # Сверху вниз и снизу вверх
            if y > 100 and not cls.__direction:
                y -= 4.3
                if 101 <= y <= 107:
                    cls.__direction = 1
            if y < 680 and cls.__direction:
                y += 4.3
            if y > 680:  # Идёт вверх
                cls.__direction = 0
        return x, y
    
    def move2(self, x: int, y: int) -> int:
        """
        Движение blinder'a (от левого угла к правому)
        
        Args:
            x (int): Позиция blinder'a по x,
            y (int): Позиция blinder'a по y
        Returns:
            int: Изменённые координаты blinder'a
        """
        if self.__moving_right:
            if x < 770:
                x += self.speed
            if y < 770:
                y += self.speed
            if x >= 770 and y >= 770:
                self.__moving_right = 0
        else:
            if x > 0:
                x -= self.speed
            if y > 0:
                y -= self.speed
            if x <= 0 and y <= 0:
                self.__moving_right = 1
        return x, y
    
    def move3(self, x: int, y: int) -> int:
        """
        Движение stalker'a (двигается за игроком)
        
        Args:
            x (int): Позиция stalker'a по x,
            y (int): Позиция stalker'a по y
        Returns:
            int: Изменённые координаты stalker'a
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
