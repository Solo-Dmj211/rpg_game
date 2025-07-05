import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed

class PlayerCharacter:
    def __init__(self):
        self.max_hp = 40
        self.hp = self.max_hp
        self.attack_power = 8

    def take_damage(self, amount):
        self.hp -= amount
        self.hp = max(self.hp, 0)
        print(f"Player took {amount} damage! Current HP: {self.hp}")

    def is_defeated(self):
        return self.hp <= 0
