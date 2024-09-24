from abc import ABC, abstractmethod


class GameObjects(ABC):
    """Этот класс является родителем для классов Item и Block"""
    
    @abstractmethod
    def placing(self) -> None:
        """Размещение предмета на карте"""
        pass
    
    @abstractmethod
    def functional(self) -> None:
        """Функционал игрового объекта"""
        pass