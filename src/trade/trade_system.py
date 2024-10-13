"""Торговая система"""

from ..trade.money_system import MoneySystem


class TradeSystem:
    """Торговая система у торговца"""
    
    def draw_items(self) -> None:
        """Отрисовка предметов"""
        pass
    
    def buy_items(self) -> None:
        """Покупка предметов"""
        MoneySystem()
        MoneySystem.change_money(1)
