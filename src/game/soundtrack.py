"""Музыка"""

import pygame


pygame.init()


class SoundTrack:
    """Класс для музыки"""

    def __init__(self):
        pygame.mixer.music.load("textures/music.mp3")
        pygame.mixer.music.set_volume(0.41)

    def play(self) -> None:
        """Воспроизведение музыки"""
        pygame.mixer.music.play(-1)
