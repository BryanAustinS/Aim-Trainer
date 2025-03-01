import pygame
import config

class Endscreen:
    font = config.LABEL_FONT

    def __init__(self, win, elapsed_time, target_pressed, clicks):
        self.win = win
        self.elapsed_time = elapsed_time
        self.target_pressed = target_pressed
        self.clicks = clicks

    def draw(self):
        LABEL_FONT = config.LABEL_FONT

        self.win.fill("grey")

        time_label = LABEL_FONT.render(f"Time: {config.format_time(self.elapsed_time)}", 1, "black")

        speed = round(self.target_pressed / self.elapsed_time, 1)
        speed_label = LABEL_FONT.render(f"Speed: {speed} target/second", 1, "black")

        hits_label = LABEL_FONT.render(f"Hits: {self.target_pressed}", 1, "black")

        accuracy = round(self.target_pressed / self.clicks * 100, 1)
        accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "black")

        self.win.blit(time_label, (get_middle(time_label), 100))
        self.win.blit(speed_label, (get_middle(speed_label), 200))
        self.win.blit(hits_label, (get_middle(hits_label), 300))
        self.win.blit(accuracy_label, (get_middle(accuracy_label), 400))

        pygame.display.update()

        while config.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    quit()

def get_middle(surface):
    return config.WIDTH / 2 - surface.get_width() / 2