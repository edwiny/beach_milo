import pygame
import random
from enum import Enum


class GradientRect:
    def __init__(self, topleft_x, topleft_y, width, height):
        self.width = width
        self.height = height
        self.topleft_x = topleft_x
        self.topleft_y = topleft_y
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(topleft=(topleft_x, topleft_y))

    def vertical_fill(self, bottom_colour: tuple, top_colour: tuple) -> pygame.Surface:
        for row in range(0, self.height):
            factor = (row + 1) / self.height
            red = bottom_colour[0] + (top_colour[0] - bottom_colour[0]) * factor
            green = bottom_colour[1] + (top_colour[1] - bottom_colour[1]) * factor
            blue = bottom_colour[2] + (top_colour[2] - bottom_colour[2]) * factor
            pygame.draw.line(self.surf,
                             (
                                 int(red), int(green), int(blue)
                             ),
                             (0, row),
                             (self.width, row)
                             )
        return self.surf
