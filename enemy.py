import pygame

class Enemy(pygame.sprite.Sprite):
    id_counter = 1

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.max_hp = 30
        self.hp = self.max_hp
        self.attack_power = 5
        self.name = f"Enemy {Enemy.id_counter}"
        Enemy.id_counter += 1
