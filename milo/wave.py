import pygame
import random
from enum import Enum

import milo.animated_sprite


class WaveState(Enum):
    ADVANCING = 1
    RETREATING = 2


class Wave(milo.animated_sprite.AnimatedTiledSprite):
    def __init__(self, sprites, x_offset, width, top_zone, bottom_zone):
        super(Wave, self).__init__(sprites, 1, 10)
        # self.surf.fill((255, 255, 250))
        self.rect = self.surf.get_rect(topleft=(x_offset, top_zone))
        self.speed = random.randint(1, 3)
        self.original_speed = self.speed
        self.top_zone = top_zone
        self.bottom_zone = bottom_zone
        self.state = WaveState.ADVANCING

    def animate(self):
        if self.millis_since_last_animation() > 200:
            self.forward()

    def update(self):
        # how far is the wave from the end of it's run
        factor = self.rect.bottom / (self.bottom_zone - self.top_zone)
        if self.speed > 1:
          self.speed = int(self.original_speed * 1 / factor)

        self.rect.move_ip(0, self.speed)
        # if self.state == WaveState.ADVANCING and self.rect.bottom > self.bottom_zone:
        #     self.state = WaveState.RETREATING
        #     self.speed = -self.speed
        # if self.state == WaveState.RETREATING and self.rect.top < self.top_zone:
        #     self.kill()
        if self.state == WaveState.ADVANCING and self.rect.bottom > self.bottom_zone:
            self.kill()
        else:
            self.animate()
