from player import Player, PlayerCharacter
from enemy import Enemy
from battle_menu import BattleMenu
import pygame

# Init
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
game_state = "exploration"

# Create player first
player_sprite = Player(100, 100)
player_char = PlayerCharacter()

# Then create enemies
enemies = [
    Enemy(300, 150),
    Enemy(400, 200),
    Enemy(350, 250)
]

# Group sprites for drawing
enemy_group = pygame.sprite.Group(enemies)
all_sprites = pygame.sprite.Group(player_sprite, *enemies)

# Create battle menu
battle_menu = BattleMenu(["Attack", "Skill", "Item", "Run"], player_char, enemies)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if game_state == "exploration":
        player_sprite.update()
        if pygame.sprite.spritecollide(player_sprite, enemy_group, False):
            game_state = "battle"

    elif game_state == "battle":
        battle_menu.update()


        if pygame.sprite.spritecollide(player_sprite, enemy_group, False):
            print("Entering battle...")
            game_state = "battle"

    screen.fill((30, 30, 30))

    if game_state == "exploration":
        all_sprites.draw(screen)
    elif game_state == "battle":
        # Placeholder battle scene
        screen.fill((10, 10, 50))
        font = pygame.font.SysFont(None, 50)
        text = font.render("Battle Started!", True, (255, 255, 255))
        screen.blit(text, (180, 220))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()