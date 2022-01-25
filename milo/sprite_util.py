from pathlib import Path
from typing import Tuple

import pygame
import random
from milo.constants import *


def load_sprites(directory: str, pattern: str) -> Tuple[pygame.Surface]:
    surfaces = []

    files = sorted(Path(directory).glob(pattern))

    print(f"Load sprites: {files}")

    for f in files:
        s = pygame.image.load(f).convert()
        if s is not None and type(s) == pygame.Surface:
            surfaces.append(s)
    return tuple(surfaces)


def load_sprite_sheet(filename, rows, cols) -> Tuple[pygame.Surface]:
    surfaces = []

    sheet = pygame.image.load(filename).convert()
    if sheet is None or type(sheet) != pygame.Surface:
        print(f"ERROR: failed to load sprite sheet {filename}")
        return []

    # figure out sprite size
    sprite_width = sheet.get_width() // cols
    sprite_height = sheet.get_height() // rows

    for r in range(rows):
        for c in range(cols):
            s = pygame.Surface((sprite_width, sprite_height))
            s.blit(sheet, (0, 0), area=sheet.get_rect(topleft=(
                c * sprite_width, r * sprite_height
            )))
            surfaces.append(s)
    print(f"Loaded {len(surfaces)} sprites from sprite sheet {filename}")
    return tuple(surfaces)
