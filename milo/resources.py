import milo.sprite_util
import milo.player
import milo.cloud
import milo.crab
import milo.wave
import milo.gradient
import milo.strip
from milo.constants import *
import random


class GameResources:
    cloud_sprites = None
    wave_sprites = None
    crab_sprites = None
    milo_sprites = None
    test_sprites = None

    @classmethod
    def load(cls):
        cls.cloud_sprites = milo.sprite_util.load_sprite_sheet("assets/images/cloud_sheet.png", 3, 1)
        cls.wave_sprites = milo.sprite_util.load_sprite_sheet("assets/images/waves.png", 3, 1)
        cls.crab_sprites = milo.sprite_util.load_sprite_sheet("assets/images/crab.png", 8, 1)
        cls.milo_sprites = milo.sprite_util.load_sprites("assets/images", "milo*.png")


class GameFactory:
    @classmethod
    def get_player(cls):
        return milo.player.Player(GameResources.milo_sprites)

    @classmethod
    def spawn_crab(cls):
        return milo.crab.Crab(GameResources.crab_sprites,
                              PLAY_AREA_TOP, PLAY_AREA_TOP + PLAY_AREA_HEIGHT)

    @classmethod
    def spawn_cloud(cls):
        return milo.cloud.Cloud(GameResources.cloud_sprites,
                                SKY_TOP, (SKY_TOP + SKY_HEIGHT // 2))

    @classmethod
    def spawn_enemy(cls):
        wave_width = random.randint(200, SCREEN_WIDTH / 2)
        new_enemy = milo.wave.Wave(
            sprites=GameResources.wave_sprites,
            width=wave_width,
            x_offset=random.randint(0, SCREEN_WIDTH - wave_width),
            top_zone=SHALLOW_OCEAN_TOP,
            bottom_zone=BEACH_TOP + random.randint(0, BEACH_HEIGHT // 2)
        )
        return new_enemy

    @classmethod
    def get_sky(cls):
        sky = milo.gradient.GradientRect(0, SKY_HEIGHT, SCREEN_WIDTH, SKY_HEIGHT)
        sky.vertical_fill((35, 70, 150), (215, 166, 13))
        return sky

    @classmethod
    def get_deep_ocean(cls):
        deep_ocean = milo.gradient.GradientRect(0, DEEP_OCEAN_TOP, SCREEN_WIDTH, DEEP_OCEAN_HEIGHT)
        deep_ocean.vertical_fill((0, 0, 180), (0, 0, 255))
        return deep_ocean

    @classmethod
    def get_beach(cls):
        return milo.strip.TiledRect(BEACH_TOP, BEACH_HEIGHT, SCREEN_WIDTH, "assets/images/sand.png")




