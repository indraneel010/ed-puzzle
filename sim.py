import pygame
from time import sleep


class Visualizer:
    COLORS = {
        "background": (0, 0, 0),
        "highlight": (0, 255, 0)
    }
    SCALE_FACTOR = 16

    def __init__(self):
        pygame.init()
        display_size = 56 * self.SCALE_FACTOR
        self.window = pygame.display.set_mode((display_size, display_size))

    def draw_rectangle(self, top_left, dimensions, color, border=0):
        x, y = top_left
        width, height = dimensions
        rect = pygame.Rect(x, y, width, height)
        if border > 0:
            pygame.draw.rect(self.window, color, rect, border)
        else:
            pygame.draw.rect(self.window, color, rect)

    def visualize(self, objects):
        self.window.fill(self.COLORS["background"])

        for obj in objects:
            piece_dim, pos = obj
            scaled_dim = (piece_dim[0] * self.SCALE_FACTOR, piece_dim[1] * self.SCALE_FACTOR)
            scaled_pos = (pos[0] * self.SCALE_FACTOR, pos[1] * self.SCALE_FACTOR)

            self.draw_rectangle(scaled_pos, scaled_dim, self.COLORS["highlight"])
            self.draw_rectangle(
                (scaled_pos[0] + 5, scaled_pos[1] + 5),
                (scaled_dim[0] - 10, scaled_dim[1] - 10),
                self.COLORS["background"]
            )

        pygame.display.flip()
        sleep(0.01)
