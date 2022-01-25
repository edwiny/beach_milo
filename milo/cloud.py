import pygame
import random

import milo.animated_sprite
from milo.constants import *


class Cloud(milo.animated_sprite.AnimatedSprite):
    def __init__(self, sprites, top_zone, bottom_zone):
        super(Cloud, self).__init__(sprites)
        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(topleft=(
            SCREEN_WIDTH - self.surf.get_width(),
            random.randint(top_zone, bottom_zone)
        ))
        self.top_zone = top_zone
        self.bottom_zone = bottom_zone
        self.speed = random.randint(1, 2)

    def update(self):
        if self.rect.right <= 0:
            self.kill()
        else:
            self.rect.move_ip(-self.speed, 0)
            self.animate()

    def animate(self):
        if self.millis_since_last_animation() > 40:
            self.forward()
