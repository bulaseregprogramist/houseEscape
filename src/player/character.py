"""Персонаж"""

from abc import abstractmethod, ABC


class Character(ABC):
    speed = 1
    
    @classmethod
    @abstractmethod
    def change_fields(cls, speed: int) -> None:
        """
        Изменяет статичные поля класса
        
        Args:
            speed (int): Скорость персонажа
        """
        cls.speed = speed
        
    @abstractmethod
    def get_stats(self) -> None:
        """Получение информации об персонаже"""
        pass
    
    @abstractmethod
    def die(self) -> None:
        """Смерть персонажа"""
        pass
    