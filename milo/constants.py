import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 5
FPS = 60
MAX_CRABS = 5
CRAB_RESPAWN_MS = 3000
WAVE_HEIGHT = 200
SKY_HEIGHT = SCREEN_HEIGHT // 7
DEEP_OCEAN_HEIGHT = SCREEN_HEIGHT // 7
SHALLOW_OCEAN_HEIGHT = SCREEN_HEIGHT // 3

SKY_TOP = 0
DEEP_OCEAN_TOP = SKY_TOP + SKY_HEIGHT
SHALLOW_OCEAN_TOP = DEEP_OCEAN_TOP + DEEP_OCEAN_HEIGHT
BEACH_TOP = SHALLOW_OCEAN_TOP + SHALLOW_OCEAN_HEIGHT
BEACH_HEIGHT = SCREEN_HEIGHT - BEACH_TOP

PLAY_AREA_TOP = SHALLOW_OCEAN_TOP + int(SHALLOW_OCEAN_HEIGHT * 0.66)
PLAY_AREA_HEIGHT = SCREEN_HEIGHT - PLAY_AREA_TOP - 20

EVENT_ADDENEMY = pygame.USEREVENT + 1
EVENT_ADDCLOUD = pygame.USEREVENT + 3
EVENT_CRABSPAWN = pygame.USEREVENT + 2
EVENT_SOUNDBARK = pygame.USEREVENT + 4

