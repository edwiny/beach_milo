import pygame
import random
from milo.constants import *


class TiledRect(pygame.sprite.Sprite):
    def __init__(self, top, height, width, bg_img):
        super(TiledRect, self).__init__()
        self.top = top
        self.height = height
        self.width = width
        self.surf = pygame.Surface((self.width, height))
        self.bg_surf = pygame.image.load(bg_img).convert()
        self.bg_surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        # self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(topleft=(top, 0))

    def tile(self):
        for row in range(self.height // self.bg_surf.get_height() + 1):
            for col in range(self.width // self.bg_surf.get_width() + 1):
                tile_x = 0 + (self.bg_surf.get_width() * col)
                tile_y = self.bg_surf.get_height() * row
                self.surf.blit(self.bg_surf,
                               self.surf.get_rect(topleft=(tile_x, tile_y))
                               )

    def update(self):
        self.rect = self.surf.get_rect(topleft=(0, self.top))
        self.tile()
