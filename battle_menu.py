import pygame


class BattleMenu:
    def __init__(self, options, player, enemies):
        self.options = options
        self.selected_index = 0
        self.font = pygame.font.SysFont(None, 36)
        self.selection_color = (255, 255, 0)
        self.default_color = (255, 255, 255)
        self.message = ""
        self.player = player
        self.enemies = enemies
        self.turn = "player"
        self.state = "main_menu"  # or "target_select"
        self.target_index = 0

    def handle_input(self, event):
        if self.turn != "player":
            return

        if self.state == "main_menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    choice = self.options[self.selected_index]
                    if choice == "Attack":
                        self.state = "target_select"
                        self.target_index = 0
                    else:
                        self.message = f"{choice} not implemented"

        elif self.state == "target_select":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.target_index = (self.target_index + 1) % len(self.enemies)
                elif event.key == pygame.K_LEFT:
                    self.target_index = (self.target_index - 1) % len(self.enemies)
                elif event.key == pygame.K_RETURN:
                    target = self.enemies[self.target_index]
                    dmg = self.player.attack_power
                    target.take_damage(dmg)
                    self.message = f"You hit {target.name} for {dmg}!"
                    self.state = "main_menu"
                    self.turn = "enemy"

    def update(self):
        if self.turn == "enemy":
            pygame.time.delay(500)
            living_enemies = [e for e in self.enemies if e.hp > 0]
            if living_enemies:
                attacker = living_enemies[0]
                dmg = attacker.attack_power
                self.player.take_damage(dmg)
                self.message = f"{attacker.name} hits you for {dmg}!"
            else:
                self.message = "All enemies defeated!"
            self.turn = "player"

    def draw(self, surface):
        if self.state == "main_menu":
            x, y = 50, 350
            for i, option in enumerate(self.options):
                color = self.selection_color if i == self.selected_index else self.default_color
                text = self.font.render(option, True, color)
                surface.blit(text, (x, y + i * 40))

        elif self.state == "target_select":
            for i, enemy in enumerate(self.enemies):
                if enemy.hp <= 0:
                    continue
                rect = enemy.rect
                outline = pygame.Rect(rect.x - 2, rect.y - 2, rect.width + 4, rect.height + 4)
                if i == self.target_index:
                    pygame.draw.rect(surface, (255, 255, 0), outline, 2)

        # Display HP
        surface.blit(self.font.render(f"Player HP: {self.player.hp}", True, (100, 255, 100)), (50, 50))

        for i, enemy in enumerate(self.enemies):
            hp_color = (255, 100, 100) if enemy.hp > 0 else (100, 100, 100)
            hp_text = f"{enemy.name}: {enemy.hp}" if enemy.hp > 0 else f"{enemy.name} (defeated)"
            surface.blit(self.font.render(hp_text, True, hp_color), (400, 40 + i * 30))

        if self.message:
            msg = self.font.render(self.message, True, (255, 255, 255))
            surface.blit(msg, (50, 100))
