"""Персонаж"""


class Character:
    speed = 1
    
    def change(self, speed: int) -> None:
        self.speed = speed
    