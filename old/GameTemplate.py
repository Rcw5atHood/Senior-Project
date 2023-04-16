import pygame

# Initialize pygame
pygame.init()

# Set up the display
display_width = pygame.display.Info().current_w
display_height = pygame.display.Info().current_h

screen_width = int(0.75 * display_width)
screen_height = int(0.75 * display_height)

screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the start button
start_button_width = screen_width // 4
start_button_height = screen_height // 10
start_button_x = (screen_width - start_button_width) // 2
start_button_y = (screen_height - start_button_height) // 2
start_button_rect = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)

# Set up the text for the start button
start_font = pygame.font.Font(None, start_button_height // 2)
start_text = start_font.render("Start", True, red)
start_text_rect = start_text.get_rect(center=(start_button_x + start_button_width // 2, start_button_y + start_button_height // 2))

# Set up the bingo text
bingo_font = pygame.font.Font(None, screen_height // 15)
bingo_text = bingo_font.render("Bingo", True, red)
bingo_text_rect = bingo_text.get_rect(center=(screen_width // 2, screen_height // 2))

# Set up the game loop
running = True
game_screen = 1
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and game_screen == 1:
            if start_button_rect.collidepoint(event.pos):
                game_screen = 2
        elif event.type == pygame.MOUSEBUTTONUP and game_screen == 2:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the start button
    pygame.draw.rect(screen, white, start_button_rect)
    screen.blit(start_text, start_text_rect)

    # Draw the bingo text
    if game_screen == 2:
        screen.fill(white)
        screen.blit(bingo_text, bingo_text_rect)

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
