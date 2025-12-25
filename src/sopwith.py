import pygame

def create_game_screen():
    # Create a new window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sopwith Game")
    return screen

def create_background() -> pygame.Surface:
    background_image = pygame.image.load("assets/images/background.png")
    return background_image

def create_player_image():
    player_image = pygame.image.load("assets/images/sopwith.png")
    return player_image

def create_player_rect(player_image, screen):
    player_rect = player_image.get_rect()
    player_rect.left = screen.get_width() - player_rect.width - 10
    player_rect.top = 50
    return player_rect

def create_bomb(player_rect, screen) -> pygame.Rect:
    bomb_image = pygame.image.load("assets/images/bomb.png")
    bomb_rect = bomb_image.get_rect()
    bomb_rect.top = player_rect.bottom - 8
    bomb_rect.midtop = player_rect.midbottom
    screen.blit(bomb_image, (bomb_rect.x, bomb_rect.y))
    return bomb_rect

def draw_bomb_update(bomb_rect, screen) -> pygame.Rect:
    bomb_image = pygame.image.load("assets/images/bomb.png")
    old_rect = bomb_image.get_rect()
    old_rect.right = bomb_rect.right
    old_rect.top = bomb_rect.top + 5

    screen.blit(bomb_image, old_rect)
    return old_rect


def display_coordination_text(screen, player_rect: pygame.Rect):
    # Create a font for displaying text
    font = pygame.font.Font(None, 24)

    # Render and display coordinates in top right
    coord_text = font.render(f'Player Coordinate: {player_rect.center}',
                             True, (255, 255, 255))

    text_rect = coord_text.get_rect()
    text_rect.topleft = (10, 10)  # 10 pixels from top and left edge

    screen.blit(coord_text, text_rect)

def display_bombs_dropped(screen, bombs_dropped):
    # Create a font for displaying text
    font = pygame.font.Font(None, 18)

    # Render and display coordinates in top right
    coord_text = font.render(f'Bombs Dropped: {bombs_dropped}',
                             True, (255, 255, 255))

    text_rect = coord_text.get_rect()
    text_rect.topleft = (650, 10)  # 10 pixels from top and left edge

    screen.blit(coord_text, text_rect)

def draw_player(horizontal_speed, player_image, player_rect, screen, vertical_speed) -> pygame.Rect:
    screen.blit(player_image, (player_rect.x, player_rect.y))
    player_rect = update_player_coordinates(horizontal_speed, player_rect, screen, vertical_speed)
    return player_rect


def update_player_coordinates(horizontal_speed, player_rect, screen, vertical_speed) -> pygame.Rect:

    if player_rect.left <= 10:
        player_rect.left = screen.get_width() - player_rect.width - 10
        player_rect.top = player_rect.top + vertical_speed

    player_rect.left += horizontal_speed

    return player_rect


def main():

    # Game loop
    running = True

    # Initialize the game
    pygame.init()

    # Create the game screen
    screen = create_game_screen()
    background = create_background()

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Create the player image and rect
    player_image = create_player_image()
    player_rect = create_player_rect(player_image, screen)

    # Set the initial horizontal and vertical speeds
    vertical_speed = 50
    horizontal_speed = -2

    bombs: list = []
    number_of_bombs_dropped = 0

    # Game loop
    while running:


        # Display the background image
        screen.blit(background, (0, 0))

        # Draw the player
        player_rect = draw_player(horizontal_speed, player_image, player_rect, screen, vertical_speed)

        if len(bombs) > 0:
            bomb_rect = bombs.pop(0)
            new_bomb_rect = draw_bomb_update(bomb_rect, screen)
            if new_bomb_rect.bottom < screen.get_height() - 50:
                bombs.append(new_bomb_rect)



        # Display the player coordinates
        display_coordination_text(screen, player_rect)
        display_bombs_dropped(screen, number_of_bombs_dropped)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(bombs) == 0:
                        bomb_rect = create_bomb(player_rect, screen)
                        number_of_bombs_dropped += 1
                        bombs.append(bomb_rect)

            if event.type == pygame.QUIT:
                running = False



        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()





if __name__ == '__main__':
    main()
