import time
import pygame

class Aimtrainer:
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0  # Popped on the screen without clicking it
    start_time = time.time()

    def __init__(self, win):
        self.win = win

    def draw(self, win):
        # bg color
        win.fill("yellow")

        for target in self.targets:
            target.draw(win)


