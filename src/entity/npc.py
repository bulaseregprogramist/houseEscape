"""Неигровые персонажи (НПС)"""

from ..entity.character import Character


class NPC(Character):
    """Среди неигровых персонажей есть торговцы"""
    
    @classmethod
    def change_fields(self) -> None:
        """Смена статических полей"""
        pass
    
    def get_stats(self) -> None:
        """Получение информации об нпс"""
        pass
    
    @staticmethod
    def die(self) -> None:
        """Смерть нпс"""
        pass
