import os
import pygame

# Initialize pygame
pygame.init()

# Set up the display
display_width = pygame.display.Info().current_w
display_height = pygame.display.Info().current_h

screen_width = int(0.80 * display_width)
screen_height = int(0.80 * display_height)

screen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Load and scale the agent image
agent_path = os.path.join(os.getcwd(), 'agent.jpeg')
agent = pygame.image.load(agent_path)
agent_width = int(screen_width * 0.70)
agent_height = int(agent_width * agent.get_height() / agent.get_width())
agent = pygame.transform.scale(agent, (agent_width, agent_height))
agent_rect = agent.get_rect(center=(screen_width // 2, screen_height // 2))

# Add black border to agent_rect
border_thickness = 2
border_rect = pygame.Rect(agent_rect.left - border_thickness, agent_rect.top - border_thickness,
                          agent_rect.width + 2 * border_thickness, agent_rect.height + 2 * border_thickness)
agent_rect = pygame.Rect(agent_rect.left, agent_rect.top, agent_rect.width, agent_rect.height)

# Load and scale the dog image
dog_path = os.path.join(os.getcwd(), 'dog.jpeg')
dog = pygame.image.load(dog_path)
dog_width = int(screen_width * 0.70)
dog_height = int(dog_width * dog.get_height() / dog.get_width())
dog = pygame.transform.scale(dog, (dog_width, dog_height))
dog_rect = dog.get_rect(center=(screen_width // 2, screen_height // 2))

# Add black border to dog_rect
dog_border_rect = pygame.Rect(dog_rect.left - border_thickness, dog_rect.top - border_thickness,
                              dog_rect.width + 2 * border_thickness, dog_rect.height + 2 * border_thickness)
dog_rect = pygame.Rect(dog_rect.left, dog_rect.top, dog_rect.width, dog_rect.height)

# Set up the start button
start_button_width = screen_width // 4
start_button_height = screen_height // 10
start_button_x = (screen_width - start_button_width) // 2
start_button_y = (screen_height - start_button_height) // 2
start_button_rect = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)

# Set up the text for the start button
start_font = pygame.font.Font(None, start_button_height // 2)
start_text = start_font.render("Start", True, red)
start_text_rect = start_text.get_rect(
    center=(start_button_x + start_button_width // 2, start_button_y + start_button_height // 2))

# Set up the "next" button
next_button_width = screen_width // 4
next_button_height = screen_height // 10
next_button_x = (screen_width - next_button_width) // 2
next_button_y = screen_height - next_button_height * 2
next_button_rect = pygame.Rect(next_button_x, next_button_y, next_button_width, next_button_height)

next_font = pygame.font.Font(None, next_button_height // 2)
next_text = next_font.render("Next", True, red)
next_text_rect = next_text.get_rect(
    center=(next_button_x + next_button_width // 2, next_button_y + next_button_height // 2))

# Set up the bingo text and button
bingo_button_width = screen_width // 4
bingo_button_height = screen_height // 10
bingo_button_x = (screen_width - bingo_button_width) // 2
bingo_button_y = (screen_height - bingo_button_height) // 2
bingo_button_rect = pygame.Rect(bingo_button_x, bingo_button_y, bingo_button_width, bingo_button_height)

bingo_button_font = pygame.font.Font(None, bingo_button_height // 2)
bingo_button_text = bingo_button_font.render("Bingo", True, white)
bingo_button_text_rect = bingo_button_text.get_rect(
    center=(bingo_button_x + bingo_button_width // 2, bingo_button_y + bingo_button_height // 2))

# Set up scrolling text
scrolling_font = pygame.font.Font(None, screen_height // 20)
scrolling_text = scrolling_font.render("Welcome traveler ", True, white)
scrolling_text_rect = scrolling_text.get_rect(midtop=(screen_width // 2, 0))

scrolling_speed = 1
scrolling_offset = 1

# Set up the game loop
running = True
game_screen = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if game_screen == 0:  # Check if on start screen
                if start_button_rect.collidepoint(event.pos):
                    game_screen = 1  # Set game screen to 1 (continue screen)
            elif game_screen == 1:  # Check if on continue screen
                if next_button_rect.collidepoint(event.pos):
                    game_screen = 2  # Set game screen to 2 (bingo screen)
            elif game_screen == 2:  # Check if on bingo screen
                if bingo_button_rect.collidepoint(event.pos):
                    running = False  # Exit game loop and quit the program

    # Clear the screen
    screen.fill((0, 0, 0))

    # Scroll the text
    scrolling_offset += scrolling_speed
    if scrolling_offset > scrolling_text_rect.width:
        scrolling_offset = 0
    scrolling_text_rect.left = scrolling_offset
    screen.blit(scrolling_text, scrolling_text_rect)

    if game_screen == 0:
        # Draw the agent
        screen.blit(agent, agent_rect)
        pygame.draw.rect(screen, black, border_rect, border_thickness)  # Draw black border
        # Draw the start button
        pygame.draw.rect(screen, white, start_button_rect)
        screen.blit(start_text, start_text_rect)
        pygame.draw.rect(screen, black, border_rect, border_thickness)  # Draw black border

    elif game_screen == 1:
        # Draw the dog
        screen.blit(dog, dog_rect)
        pygame.draw.rect(screen, black, border_rect, border_thickness)  # Draw black border
        # Draw the "Next" button
        pygame.draw.rect(screen, white, next_button_rect)
        screen.blit(next_text, next_text_rect)

    elif game_screen == 2:
        # Draw the bingo text and button
        screen.fill(white)
        screen.blit(bingo_button_text, bingo_button_text_rect)
        pygame.draw.rect(screen, red, bingo_button_rect)
        screen.blit(bingo_button_text, bingo_button_text_rect)

    # Update the screen
    pygame.display.update()

# Quit
pygame.quit()
