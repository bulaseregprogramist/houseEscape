"""Денежная система"""


class MoneySystem:
    MONEY = 100
    
    @classmethod
    def change_money(cls, money: int) -> None:
        """
        Изменение кол-ва денег
        
        Args:
            money (int): Потраченные деньги
        """
        cls.MONEY -= money
