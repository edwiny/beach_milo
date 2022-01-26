import enum

import pygame
from milo.constants import *
from milo.animated_sprite import AnimatedSprite

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_w,
    K_DOWN,
    K_s,
    K_LEFT,
    K_a,
    K_RIGHT,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


class Player(AnimatedSprite):
    class State(enum.Enum):
        NORMAL = 1
        DYING = 2

    def __init__(self, sprites):
        super(Player, self).__init__(sprites)
        self.rect = self.surf.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10))
        self.is_moving = False
        self.last_bark_time = 0
        self.state = Player.State.NORMAL
        self.dying_expiry = 0

    def update(self, pressed_keys):
        saved_state = self.is_moving
        ticks = pygame.time.get_ticks()

        if self.state == Player.State.NORMAL:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -MOVE_DISTANCE)
                self.animate_running()
                self.is_moving = True
            elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0, MOVE_DISTANCE)
                self.animate_running()
                self.is_moving = True
            elif pressed_keys[K_LEFT] or pressed_keys[K_a]:
                self.flip(flip_x=True)
                self.rect.move_ip(-MOVE_DISTANCE, 0)
                self.animate_running()
                self.is_moving = True
            elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                self.flip(flip_x=False)
                self.rect.move_ip(MOVE_DISTANCE, 0)
                self.animate_running()
                self.is_moving = True
            else:
                self.reset()
                self.is_moving = False

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= PLAY_AREA_TOP:
                self.rect.top = PLAY_AREA_TOP
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

            if (saved_state is False
                    and self.is_moving is True
                    and ticks > self.last_bark_time + 3000):
                pygame.event.post(pygame.event.Event(EVENT_SOUNDBARK))
                self.last_bark_time = ticks

        elif self.state == Player.State.DYING:
            if ticks > self.dying_expiry:
                self.kill()
                pygame.event.post(pygame.event.Event(EVENT_PLAYERSPAWN))

    def animate_running(self):
        if self.millis_since_last_animation() > 40:
            self.forward()

    def die(self):
        self.state = Player.State.DYING
        self.dying_expiry = pygame.time.get_ticks() + 1000
        self.flip(flip_x=False, flip_y=True)
        self.blit()

    def is_dying(self):
        return self.state == Player.State.DYING



