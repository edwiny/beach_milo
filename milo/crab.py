import pygame
import random
from enum import Enum
import milo.animated_sprite
from milo.constants import *


class Crab(milo.animated_sprite.AnimatedSprite):
    class LifeCycle(Enum):
        SPAWNING = 1
        ENJOYING_LIFE = 2
        DISAPPEARING = 3
        DYING = 4

    def __init__(self, sprites, top_zone, bottom_zone):
        super(Crab, self).__init__(sprites)

        self.rect = self.surf.get_rect(topleft=(
            random.randint(64, SCREEN_WIDTH - 64),
            random.randint(top_zone, bottom_zone)
        ))
        self.top_zone = top_zone
        self.bottom_zone = bottom_zone
        self.ttl = random.randint(2000, 5000)
        self.created = pygame.time.get_ticks() # millis since game start
        self.lifecycle = Crab.LifeCycle.SPAWNING
        self.anim_index = 0

    def update(self):
        if self.millis_since_last_animation() > 40:
            if self.lifecycle == Crab.LifeCycle.SPAWNING:
                if self.anim_index >= self.num_frames():
                    self.lifecycle = Crab.LifeCycle.ENJOYING_LIFE
                    self.anim_index = 0
                else:
                    self.forward()
                    self.anim_index += 1
            if self.lifecycle == Crab.LifeCycle.DISAPPEARING:
                if self.anim_index >= self.num_frames():
                    self.kill()
                else:
                    self.backward()
                    self.anim_index += 1

        if pygame.time.get_ticks() - self.created > self.ttl:
            self.disappear()

    def die(self):
        self.kill()

    def disappear(self):
        self.lifecycle = Crab.LifeCycle.DISAPPEARING
