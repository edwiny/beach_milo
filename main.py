import random

import milo.sprite_util
from milo.constants import *
import milo.strip
import milo.animated_sprite
from milo.resources import GameResources, GameFactory

pygame.mixer.init()
pygame.init()
pygame.mixer.music.set_volume(0.3)
clock = pygame.time.Clock()
score = 0
lives = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.time.set_timer(EVENT_ADDENEMY, 5000 * 1 // (score + 1))
pygame.time.set_timer(EVENT_CRABSPAWN, CRAB_RESPAWN_MS)
pygame.time.set_timer(EVENT_ADDCLOUD, 5000)

GameResources.load()

pygame.display.set_icon(GameResources.milo_sprites[0])
# create player and background objects
player = GameFactory.get_player()
sky = GameFactory.get_sky()
deep_ocean = GameFactory.get_deep_ocean()
shallow_ocean = GameFactory.get_shallow_ocean()
beach = GameFactory.get_beach()
font = GameFactory.get_font()

# create sprite groups to manage rendering and collision detection
enemies = pygame.sprite.Group()
crabbies = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
visible_sprites = pygame.sprite.Group()
visible_sprites.add(player)
backgrounds.add(beach)

# credit: https://freesound.org/people/kwahmah_02/sounds/260614/
collision_sound = pygame.mixer.Sound("assets/sounds/pop.ogg")

# credit: https://freesound.org/people/crazymonke9/
bark_sound = pygame.mixer.Sound("assets/sounds/bark.ogg")

running = True


def handle_event(gameplay_event):
    global running, visible_sprites, lives, player
    if gameplay_event.type == pygame.KEYDOWN:
        if gameplay_event.key == pygame.K_ESCAPE:
            running = False
    elif gameplay_event.type == pygame.QUIT:
        running = False
    elif gameplay_event.type == EVENT_ADDENEMY:
        if len(enemies) == 0:
            new_enemy = GameFactory.spawn_enemy()
            enemies.add(new_enemy)
            visible_sprites.add(new_enemy)
    elif gameplay_event.type == EVENT_CRABSPAWN:
        if len(crabbies) < MAX_CRABS:
            new_crab = GameFactory.spawn_crab()
            crabbies.add(new_crab)
            visible_sprites.add(new_crab)
    elif gameplay_event.type == EVENT_ADDCLOUD:
        new_cloud = GameFactory.spawn_cloud()
        backgrounds.add(new_cloud)
        visible_sprites.add(new_cloud)
    elif gameplay_event.type == EVENT_SOUNDBARK:
        bark_sound.play()
    elif gameplay_event.type == EVENT_PLAYERSPAWN:
        player = GameFactory.get_player()
        visible_sprites.add(player)


while running:
    for event in pygame.event.get():
        handle_event(event)

    player.update(pygame.key.get_pressed())
    enemies.update()
    crabbies.update()
    backgrounds.update()

    screen.fill((135, 206, 250))

    # render
    for entity in backgrounds:
        screen.blit(entity.surf, entity.rect)
    screen.blit(sky.surf, sky.surf.get_rect(topleft=(0, SKY_TOP)))
    screen.blit(deep_ocean.surf, deep_ocean.surf.get_rect(topleft=(0, DEEP_OCEAN_TOP)))
    screen.blit(shallow_ocean.surf, shallow_ocean.surf.get_rect(topleft=(0, SHALLOW_OCEAN_TOP)))

    for entity in visible_sprites:
        screen.blit(entity.surf, entity.rect)
    fs = font.render(f"Lives: {lives} Score: {score}", False, (255, 255, 255))
    screen.blit(fs, fs.get_rect(topleft=(SCREEN_WIDTH - (SCREEN_WIDTH / 3), 10)))

    # collision detection
    if pygame.sprite.spritecollideany(player, enemies) and not player.is_dying():
        player.die()
        lives -= 1
        if lives == 0:
            running = False

    disappearing_crabbies = [crab.disappear() for crab in crabbies if pygame.sprite.spritecollide(crab, enemies, False)]

    # scoring
    caught_crabbies = pygame.sprite.spritecollide(player, crabbies, False)
    for crab in caught_crabbies:
        score += 1
        collision_sound.play()
        crab.die()

    # display everything drawn since last flip
    pygame.display.flip()
    # Calcs the delay based on clock ticks and machine speed.
    clock.tick(FPS)

fs = font.render(f"Game Over!", False, (255, 255, 255))
screen.blit(fs, fs.get_rect(topleft=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)))
pygame.display.flip()

pygame.time.wait(2000)
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
