import pygame




class SopwithGame:

    FRAME_RATE = 60
    GROUND_LEVEL = 37
    HIGH_ALTITUDE = 350
    MEDIUM_ALTITUDE = 150
    MINIMUM_ALTITUDE = 50
    MARGIN = 10

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create the game screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Sopwith Game")

        # Load images
        self.background = pygame.image.load("assets/images/background.png")
        self.runway = pygame.image.load("assets/images/runway.png")
        self.player_image = pygame.image.load("assets/images/sopwith.png")
        self.bomb_image = pygame.image.load("assets/images/bomb.png")

        # Create player rect
        self.player_rect = self.player_image.get_rect()
        self.player_rect.left = self.screen.get_width() - self.player_rect.width - self.MARGIN
        self.player_rect.top = 50

        # Game state variables
        self.running = True
        self.game_mode = 0
        self.score = 0
        self.altitude = 0
        self.bombs_dropped = 0
        self.bombs = []

        # Movement speeds
        self.vertical_speed = 50
        self.horizontal_speed = -2

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Font for text display
        self.font_large = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)

        # Colors for text display
        self.white = pygame.Color(255, 255, 255)
        self.orange = pygame.Color(255, 128, 0)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)

    def update_altitude(self):
        """Calculate current altitude based on player position"""
        self.altitude = self.screen.get_height() - self.player_rect.bottom - self.GROUND_LEVEL

    def create_bomb(self) -> pygame.Rect:
        """Create a new bomb at the player's position"""
        bomb_rect = self.bomb_image.get_rect()
        bomb_rect.top = self.player_rect.bottom
        bomb_rect.midtop = self.player_rect.midbottom
        self.screen.blit(self.bomb_image, (bomb_rect.x, bomb_rect.y))
        return bomb_rect

    def draw_bomb_update(self, bomb_rect: pygame.Rect) -> pygame.Rect:
        """Update and draw a falling bomb"""
        old_rect = self.bomb_image.get_rect()
        old_rect.right = bomb_rect.right
        old_rect.top = bomb_rect.top + 5
        self.screen.blit(self.bomb_image, old_rect)
        return old_rect

    def manage_bombs(self):
        """Update all active bombs"""
        if len(self.bombs) > 0:
            bomb_rect = self.bombs.pop(0)
            new_bomb_rect = self.draw_bomb_update(bomb_rect)
            if new_bomb_rect.bottom < self.screen.get_height() - self.GROUND_LEVEL:
                self.bombs.append(new_bomb_rect)

    def update_player_coordinates(self):
        """Update player position based on movement speeds"""
        if self.player_rect.left <= 10:
            self.player_rect.left = self.screen.get_width() - self.player_rect.width - 10
            self.player_rect.top = self.player_rect.top + self.vertical_speed

        self.player_rect.left += self.horizontal_speed

    def draw_player(self):
        """Draw the player and update their position"""
        self.screen.blit(self.player_image, (self.player_rect.x, self.player_rect.y))
        self.update_player_coordinates()

    def display_hud(self):
        """Display game information (altitude, bombs, score)"""
        # Display altitude
        self.display_altitude()

        # Display bombs dropped
        bombs_text = self.font_small.render(
            f'Bombs Dropped: {self.bombs_dropped}',
            True, (255, 255, 255)
        )
        bombs_rect = bombs_text.get_rect()
        bombs_rect.topleft = (650, 10)
        self.screen.blit(bombs_text, bombs_rect)

        # Display score (for future use)
        score_text = self.font_small.render(
            f'Score: {self.score}',
            True, (255, 255, 255)
        )
        score_rect = score_text.get_rect()
        score_rect.topleft = (650, 30)
        self.screen.blit(score_text, score_rect)

    def display_altitude(self):

        color = self.green
        if self.altitude < self.HIGH_ALTITUDE and self.altitude >= self.MEDIUM_ALTITUDE:
            color = self.orange
        elif self.altitude < self.MEDIUM_ALTITUDE:
            color = self.red

        x_pos = 10
        y_pos = 10

        parts = [
            (self.font_small.render('Altitude: ', True, self.white)),
            (self.font_small.render(f'{self.altitude}', True, color)),
            (self.font_small.render(' ft', True, self.white)),
        ]

        for text_surface in parts:
            self.screen.blit(text_surface, (x_pos, y_pos))
            x_pos += text_surface.get_width()  # Move to the right

    def handle_events(self):
        """Process game events"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(self.bombs) == 0:
                        bomb_rect = self.create_bomb()
                        self.bombs_dropped += 1
                        self.bombs.append(bomb_rect)

            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game state"""
        self.update_altitude()

        if self.game_mode == 0:
            # Display the background image
            self.screen.blit(self.background, (0, 0))

            # Draw the player
            self.draw_player()

            # Draw bombs (if needed)
            self.manage_bombs()

        if self.altitude < self.MINIMUM_ALTITUDE:
            self.running = False

    def render(self):
        """Render everything to the screen"""
        # Display HUD
        self.display_hud()

        # Update the display
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            # Update game state
            self.update()

            # Handle events
            self.handle_events()

            # Render everything
            self.render()

            # Control frame rate
            self.clock.tick(self.FRAME_RATE)    # Play speed

        pygame.quit()


def main():
    game = SopwithGame()
    game.run()


if __name__ == '__main__':
    main()
