import pygame
import config
from button import Button

def pause_game():
    config.paused = not config.paused

class Scorebar:
    def __init__(self, win, elapsed_time, target_pressed, misses, clicks):
        self.win = win
        self.elapsed_time = elapsed_time
        self.target_pressed = target_pressed
        self.misses = misses
        self.clicks = clicks
        self.pause_button = Button(
            config.WIDTH // 6 * 5, 5, 100, 50, "Pause", "green", pause_game)

    def draw(self, win):
        LABEL_FONT = config.LABEL_FONT
        pygame.draw.rect(win, "grey", (0, 0, config.WIDTH, config.TOP_BAR_HEIGHT))

        time_label = LABEL_FONT.render(f"Time: {config.format_time(self.elapsed_time)}", 1, "black")

        speed = round(self.target_pressed / self.elapsed_time, 1) if self.elapsed_time > 0 else 0
        speed_label = LABEL_FONT.render(f"Speed: {speed} target/second", 1, "black")

        hits_label = LABEL_FONT.render(f"Hits: {self.target_pressed}", 1, "black")

        lives_label = LABEL_FONT.render(f"Lives: {config.LIVES - self.misses}", 1, "black")

        accuracy = round(self.target_pressed / self.clicks * 100, 1) if self.clicks > 0 else 0
        accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

        # Dynamically position labels based on window width
        margin = 10  # Padding from the left
        spacing = config.WIDTH // 6  # Equal spacing for labels

        win.blit(time_label, (margin, 5))
        win.blit(speed_label, (spacing * 1, 5))
        win.blit(hits_label, (spacing * 2, 5))
        win.blit(lives_label, (spacing * 3, 5))
        win.blit(accuracy_label, (spacing * 4, 5))
        self.pause_button.draw(self.win)




