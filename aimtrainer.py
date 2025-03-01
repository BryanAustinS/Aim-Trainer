import math
import random
import time
import pygame
from target import Target

pygame.init()

# Create Window
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Aim Trainer')

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30
FPS = 144

def draw(win, targets):
    # bg color
    win.fill("yellow")

    for target in targets:
        target.draw(win)

    pygame.display.update()

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses = 0 # Popped on the screen without clicking it
    start_time = time.time()

    # Trigger target_event every increment (s)
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(FPS)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            # Creating the target
            if event.type == TARGET_EVENT:
                # [30, 870]
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                # [30, 1570]
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)

                target = Target(x, y)
                targets.append(target)

            # Click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        # Run target logic
        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

        draw(WIN, targets)


    pygame.quit()

if __name__ == "__main__":
    main()


