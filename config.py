import math
import pygame

pygame.init()

# Window
WIDTH, HEIGHT = 1600, 900
WIN = None  # Initialize as None
TOP_BAR_HEIGHT = 75

# Game settings
FPS = 60
LIVES = 3
run = True
paused = False
restart = False

# Target
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT
TARGET_PADDING = 30

# UI Settings
LABEL_FONT = pygame.font.SysFont('Arial', 24)

# Other Methods
def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli:02d}"

def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2