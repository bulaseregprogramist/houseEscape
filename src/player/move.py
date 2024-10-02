"""Движение игрока"""

# Есть места в комнате, в которых не должен быть игрок
# Но они видимы. 
# Например: кровать в спальне.


class Move:
    """Движение игрока по определённым местам в комнате"""
    
    @staticmethod
    def move_in_location(x: int, y: int, index: list[int, int]) -> bool:
        """
        Даёт доступ только в определённые места

        Args:
            x (int): позиция игрока по x,
            y (int): позиция игрока по y,
            index (list[int, int]): карта дома

        Returns:
            bool: Можно ли идти в этой зоне дома (True или False)
        """
        if index == [3, 3]:
            return True
        elif index == [3, 2]:
            return True
        elif index == [3, 1]:
            return True
        elif index == [2, 3]:
            return True
        elif index == [2, 2]:
            return True
        elif index == [2, 1]:
            return True
        elif index == [1, 3]:
            return True
        elif index == [1, 2]:
            return True
        elif index == [1, 1]:
            return True
        elif index == [0, 2]:
            return True
        return False
    