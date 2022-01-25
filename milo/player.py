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
    def __init__(self, sprites):
        super(Player, self).__init__(sprites)
        self.rect = self.surf.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10))
        self.is_moving = False

    # this update method has to be implemented in the Sprite subclass as the Sprite
    # Groups call it when you call group.update()
    def update(self, pressed_keys):
        saved_state = self.is_moving

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
        if saved_state == False and self.is_moving == True:
            pygame.event.post(pygame.event.Event(EVENT_SOUNDBARK))

    def animate_running(self):
        if self.millis_since_last_animation() > 40:
            self.forward()


