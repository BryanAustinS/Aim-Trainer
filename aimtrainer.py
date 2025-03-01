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
FPS = 60

TOP_BAR_HEIGHT = 50
LIVES = 3

LABEL_FONT = pygame.font.SysFont('Arial', 24)

def draw(win, targets):
    # bg color
    win.fill("yellow")

    for target in targets:
        target.draw(win)

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli:02d}"

def statistics(win, elapsed_time, target_pressed, misses, clicks):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))

    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(target_pressed / elapsed_time, 1) if elapsed_time > 0 else 0
    speed_label = LABEL_FONT.render(f"Speed: {speed} target/second", 1, "black")

    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "black")

    lives_label = LABEL_FONT.render(f"Lives: {LIVES - misses}", 1, "black")

    accuracy = round(target_pressed / clicks * 100, 1) if clicks > 0 else 0
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

    # Dynamically position labels based on window width
    margin = 20  # Padding from the left
    spacing = WIDTH // 5  # Equal spacing for labels

    win.blit(time_label, (margin, 5))
    win.blit(speed_label, (spacing * 1, 5))
    win.blit(hits_label, (spacing * 2, 5))
    win.blit(lives_label, (spacing * 3, 5))
    win.blit(accuracy_label, (spacing * 4, 5))

def end_screen(win, elapsed_time, target_pressed, clicks):
    win.fill("grey")

    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")

    speed = round(target_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} target/second", 1, "black")

    hits_label = LABEL_FONT.render(f"Hits: {target_pressed}", 1, "black")

    accuracy = round(target_pressed / clicks * 100, 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2

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
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            # Creating the target
            if event.type == TARGET_EVENT:
                # [30, 870]
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                # [30, 1520]
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)

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

            if click and target.collide(*mouse_pos):
                target_pressed += 1
                targets.remove(target)

        if misses >= LIVES:
            end_screen(WIN, elapsed_time, target_pressed, clicks)

        draw(WIN, targets)
        statistics(WIN, elapsed_time, target_pressed, misses, clicks)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


