"""Движение монстра (врага)"""


class MonsterMove:
    __direction = 0
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def move1(cls, x: int, y: int) -> int:
        """
        Движение watcher'a
        
        Args:
            x (int): Позиция watcher'a по x,
            y (int): Позиция watcher'a по y
        Returns:
            int: Изменённые координаты watcher'a
        """
        if x > 100 and not cls.__direction:
            x -= 4.3
            if 101 <= x <= 107:
                cls.__direction = 1
        if x < 680 and cls.__direction:
            x += 4.3
            if x > 680:
                cls.__direction = 0
        return x, y
    
    def move2(self, x: int, y: int) -> int:
        """
        Движение blinder'a
        
        Args:
            x (int): Позиция blinder'a по x,
            y (int): Позиция blinder'a по y
        Returns:
            int: Изменённые координаты blinder'a
        """
        return x, y
    
    def move3(self, x: int, y: int) -> int:
        """
        Движение stalker'a
        
        Args:
            x (int): Позиция stalker'a по x,
            y (int): Позиция stalker'a по y
        Returns:
            int: Изменённые координаты stalker'a
        """
        return x, y
