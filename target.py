import math

import pygame

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        # Stop growing if the size reaches max size
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        # Grow if grow = True, Reduce size if grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x_click, y_click):
        # Check if the mouse click clicks the target
        dis = math.sqrt((x_click - self.x)**2 + (y_click - self.y)**2)
        return dis <= self.size
