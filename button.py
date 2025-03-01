import pygame
import config

class Button:
    def __init__(self, x, y, w, h, text, color, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, win):
        LABEL_FONT = config.LABEL_FONT

        pygame.draw.rect(win, self.color, self.rect)
        label = LABEL_FONT.render(self.text, 1, "black")
        win.blit(label, (self.rect.x + 10, self.rect.y + 10))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

