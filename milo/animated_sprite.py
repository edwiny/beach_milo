import pygame
from typing import Tuple


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprites: Tuple[pygame.Surface]):
        super(AnimatedSprite, self).__init__()

        self.colour_key = sprites[0].get_at((0, 0))
        self.width = sprites[0].get_width()
        self.height = sprites[0].get_height()
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.set_colorkey(self.colour_key, pygame.RLEACCEL)
        self.frames = sprites
        self.frame_pos = 0
        # millis since game start
        self.created = pygame.time.get_ticks()
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.last_anim_time = self.created
        self.flip_x = False
        self.flip_y = False
        self.blit()

    def blit(self):
        self.surf.blit(self.frames[self.frame_pos], (0, 0))
        if self.flip_x or self.flip_y:
            self.surf = pygame.transform.flip(self.surf, self.flip_x, self.flip_y)

    def flip(self, flip_x = False, flip_y = False):
        self.flip_x = flip_x
        self.flip_y = flip_y

    def forward(self):
        if self.frame_pos < 0 or self.frame_pos >= len(self.frames):
            self.frame_pos = 0
        self.blit()
        self.frame_pos += 1
        self.last_anim_time = pygame.time.get_ticks()

    def backward(self):
        if self.frame_pos < 0 or self.frame_pos >= len(self.frames):
            self.frame_pos = len(self.frames) - 1
        self.blit()
        self.frame_pos -= 1
        self.last_anim_time = pygame.time.get_ticks()

    def reset(self):
        self.frame_pos = 0
        self.blit()
        self.last_anim_time = 0

    def millis_since_last_animation(self):
        return pygame.time.get_ticks() - self.last_anim_time

    def num_frames(self):
        return len(self.frames)


class AnimatedTiledSprite(pygame.sprite.Sprite):
    def __init__(self, sprites: Tuple[pygame.Surface], rows, cols):
        super(AnimatedTiledSprite, self).__init__()
        self.rows = rows
        self.cols = cols
        self.sprite_width = sprites[0].get_width()
        self.sprite_height = sprites[0].get_height()

        self.colour_key = sprites[0].get_at((0, 0))
        self.width = self.sprite_width * cols
        self.height = self.sprite_height * rows
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.set_colorkey(self.colour_key, pygame.RLEACCEL)
        self.frames = sprites
        self.frame_pos = 0
        # millis since game start
        self.created = pygame.time.get_ticks()
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.last_anim_time = self.created
        self.flip_x = False
        self.flip_y = False
        self.blit()

    def blit(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.surf.blit(self.frames[self.frame_pos], (col * self.sprite_width, row * self.sprite_height))

        self.last_anim_time = pygame.time.get_ticks()

    def flip(self, flip_x=False, flip_y=False):
        self.flip_x = flip_x
        self.flip_y = flip_y

    def forward(self):
        if self.frame_pos == len(self.frames):
            self.frame_pos = 0
        self.blit()
        self.frame_pos += 1

    def reset(self):
        self.frame_pos = 0
        self.blit()
        self.last_anim_time = 0

    def millis_since_last_animation(self):
        return pygame.time.get_ticks() - self.last_anim_time

