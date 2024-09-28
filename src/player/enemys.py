"""Враги в игре"""

from .character import Character


class Enemy(Character):
    __x: int
    __y: int
    __enemy_type: str
    
    def __init__(self, x: int, y: int, enemy_type: str) -> None:
        self.__x = x
        self.__y = y
        self.__enemy_type = enemy_type
    
    def enemy_move() -> None:
        """Движение NPC (AI)"""
        pass
    