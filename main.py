import random
import time
import pygame

from endscreen import Endscreen
from scorebar import Scorebar
from target import Target
from aimtrainer import Aimtrainer
import config

def main():
    run = True

    TARGET_EVENT = config.TARGET_EVENT
    TARGET_INCREMENT = config.TARGET_INCREMENT
    TARGET_PADDING = config.TARGET_PADDING
    WIDTH = config.WIDTH
    HEIGHT = config.HEIGHT
    TOP_BAR_HEIGHT = config.TOP_BAR_HEIGHT

    game = Aimtrainer(config.WIN)

    # Trigger target_event every increment (s)
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    print("Starting game loop")
    while config.run:
        game.clock.tick(config.FPS)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - game.start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.run = False
                break

            # Creating the target
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)

                target = Target(x, y)
                game.targets.append(target)

            # Click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                game.clicks += 1

        # Run target logic
        for target in game.targets:
            target.update()

            if target.size <= 0:
                game.targets.remove(target)
                game.misses += 1

            if click and target.collide(*mouse_pos):
                game.target_pressed += 1
                game.targets.remove(target)

        if game.misses >= config.LIVES:
            endscreen = Endscreen(config.WIN, elapsed_time, game.target_pressed, game.clicks)
            endscreen.draw()

        game.draw(config.WIN)
        scorebar = Scorebar(config.WIN, elapsed_time, game.target_pressed, game.misses, game.clicks)
        scorebar.draw(config.WIN)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()


