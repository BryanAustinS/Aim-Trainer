import pygame
import config
from button import Button

class Endscreen:
    font = config.LABEL_FONT

    def __init__(self, win, elapsed_time, target_pressed, clicks):
        self.win = win
        self.elapsed_time = elapsed_time
        self.target_pressed = target_pressed
        self.clicks = clicks
        self.restart_button = Button(
            x = config.WIDTH / 2,
            y = 500,
            w = 100,
            h = 50,
            text = "Restart",
            color = "green",
            action = self.restart_game
        )

    def restart_game(self):
        config.run = False
        config.restart = True

    def draw(self):
        LABEL_FONT = config.LABEL_FONT

        self.win.fill("grey")

        time_label = LABEL_FONT.render(f"Time: {config.format_time(self.elapsed_time)}", 1, "black")

        speed = round(self.target_pressed / self.elapsed_time, 1)
        speed_label = LABEL_FONT.render(f"Speed: {speed} target/second", 1, "black")

        hits_label = LABEL_FONT.render(f"Hits: {self.target_pressed}", 1, "black")

        if self.clicks > 0:
            accuracy = round(self.target_pressed / self.clicks * 100, 1)
        else:
            accuracy = 0
        accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

        self.win.blit(time_label, (config.get_middle(time_label), 100))
        self.win.blit(speed_label, (config.get_middle(speed_label), 200))
        self.win.blit(hits_label, (config.get_middle(hits_label), 300))
        self.win.blit(accuracy_label, (config.get_middle(accuracy_label), 400))
        self.restart_button.draw(self.win)
        pygame.display.update()

        while config.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.restart_button.check_click(event.pos)

