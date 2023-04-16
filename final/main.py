import pygame
import random
from connect4 import connect4_main
from constants import BLACK, WHITE, GREEN, RED, WIDTH, HEIGHT
from tictactoe import tictactoe_main

# Initialize Pygame
pygame.init()
# Set up font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Set up the window
screen_width = 1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Travel Adventure Game")

# Create buttons
start_button = font.render("Start", True, BLACK, WHITE)
start_rect = start_button.get_rect()
start_rect.center = (400, 300)

exit_button = font.render("Exit", True, BLACK, WHITE)
exit_rect = exit_button.get_rect()
exit_rect.center = (400, 350)

continue_button = font.render("Continue", True, BLACK, WHITE)
continue_rect = continue_button.get_rect()
continue_rect.center = (400, 500)

return_home_button = font.render("Return Home", True, BLACK, WHITE)
return_home_rect = return_home_button.get_rect()
return_home_rect.center = (500, 450)

connect4_button = font.render("Connect 4", True, BLACK, WHITE)
connect4_rect = connect4_button.get_rect()
connect4_rect.center = (400, 400)

tictactoe_button = font.render("Tic Tac Toe", True, BLACK, WHITE)
tictactoe_rect = tictactoe_button.get_rect()
tictactoe_rect.center = (400, 450)

play_another_game_button = font.render("Play Another Game", True, BLACK, WHITE)
play_another_game_rect = play_another_game_button.get_rect()
play_another_game_rect.center = (400, 550)


# Load text and images
destinations = ["Paris", "New York", "Tokyo", "Sydney", "Cairo"]
destinations_info = {
    "Paris": "Welcome to Paris, the city of love!",
    "New York": "Welcome to New York, the city that never sleeps!",
    "Tokyo": "Welcome to Tokyo, the heart of Japan!",
    "Sydney": "Welcome to Sydney, the largest city in Australia!",
    "Cairo": "Welcome to Cairo, home of the ancient pyramids!",
}

destination_images = {
    "Paris": pygame.image.load('paris.jpeg').convert(),
    "New York": pygame.image.load('newyork.jpeg').convert(),
    "Tokyo": pygame.image.load('tokyo.jpeg').convert(),
    "Sydney": pygame.image.load('Sydney.jpeg').convert(),
    "Cairo": pygame.image.load('cairo.jpeg').convert(),
}


player_won_text = font.render("You Won! Now we are moving to the next destination...", True, BLACK, WHITE)
computer_won_text = font.render("I Won! So sorry Try again.", True, BLACK, WHITE)

exit_message_text = font.render("Good Bye and thank you for adventuring with us", True, BLACK, WHITE)
exit_message_rect = exit_message_text.get_rect()
exit_message_rect.center = (screen_width // 2, screen_height // 2)

agent_image = pygame.image.load('agent.jpeg')
agent_rect = agent_image.get_rect()
agent_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

visited = []
location = ""
location_text = ""
win_text, win_text_rect = None, None
current_screen = "start"
winner = None

def set_caption(title):
    pygame.display.set_caption(title)

def draw_start_screen():
    agent_rect.center = (screen_width // 2, screen_height // 4)
    screen.blit(agent_image, agent_rect)
    screen.blit(start_button, start_rect)
    screen.blit(exit_button, exit_rect)

def draw_button(text, rect, text_color, button_color, action=None):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surface, text_rect)

    if action is not None:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(rect).collidepoint(event.pos):
                    action()

def draw_destination_screen():
    if location in destination_images:
        image = destination_images[location]
        image_rect = image.get_rect()
    else:
       pass

    # Calculate the position to center the image on the screen
    screen_width, screen_height = pygame.display.get_surface().get_size()
    image_rect.center = (screen_width // 2, screen_height // 2)

    # Draw the image on the screen
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.update()

def draw_game_choice_screen():
    screen.blit(connect4_button, connect4_rect)
    screen.blit(tictactoe_button, tictactoe_rect)


def draw_game_over_screen():
    if win_text is not None and win_text_rect is not None:
        screen.blit(win_text, win_text_rect)
    else:
        win_lose_text = font.render("I Won! So sorry Try again.", True, BLACK, WHITE)
        screen.blit(win_lose_text, win_lose_text.get_rect(center=(screen_width // 2, screen_height // 2)))

    screen.blit(continue_button, continue_rect)
    screen.blit(play_another_game_button, play_another_game_rect)



def draw_exit_message_screen():
    screen.blit(exit_message_text, exit_message_rect)

def win_screen(result):
    if not pygame.font.get_init():
        pygame.font.init()
    if result.strip() == "":
        result = "You won"
    win_text = font.render(f"{result}! Congratulations!", True, BLACK, WHITE)
    win_text_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2))

    # Add a delay before moving to the next destination
    pygame.time.delay(500)

    return win_text, win_text_rect


def lose_screen():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("You lost!", font, RED, screen, WIDTH // 2, HEIGHT // 4)
        draw_text("Press ESC to exit", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_button("Try again", (WIDTH // 2 - 50, HEIGHT - 100, 100, 50), BLACK, GREEN, game_choice)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    sys.exit()

        pygame.display.flip()


# Main game loop
running = True
while running:
    # 1. Handle the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # Update the game logic based on the events
        if current_screen == "start":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    current_screen = "destination"
                    location = random.choice(destinations)
                    visited.append(location)
                    location_text = destinations_info[location]
                elif exit_rect.collidepoint(event.pos):
                    running = False

        elif current_screen == "destination":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    current_screen = "game_choice"

        if current_screen == "game_choice":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if connect4_rect.collidepoint(event.pos):
                    winner = connect4_main()
                elif tictactoe_rect.collidepoint(event.pos):
                    winner = tictactoe_main()
                else:
                    winner = None
                if winner == "player":
                    win_text, win_text_rect = win_screen("You won the game")
                    location = random.choice([x for x in destinations if x not in visited])
                    visited.append(location)
                    location_text = destinations_info[location]
                    current_screen = "destination"
                elif winner == "computer":
                    pass
                else:
                    win_lose_text = None
                if winner is not None:
                    current_screen = "game_over"

        elif current_screen == "game_over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    location = random.choice([x for x in destinations if x not in visited])
                    visited.append(location)
                    location_text = destinations_info[location]
                    current_screen = "destination"
                elif play_another_game_rect.collidepoint(event.pos):
                    current_screen = "game_choice"
                elif return_home_rect.collidepoint(event.pos):
                    current_screen = "start"


    # 3. Draw the game elements on the screen
    screen.fill(WHITE)
    if current_screen == "start":
        draw_start_screen()
    elif current_screen == "destination":
        draw_destination_screen()
        screen.blit(font.render(location_text, True, BLACK), (screen_width // 2 - 100, 100))
        screen.blit(continue_button, continue_rect)
    elif current_screen == "game_choice":
        draw_game_choice_screen()
    elif current_screen == "game_over":
        draw_game_over_screen()
        screen.blit(return_home_button, return_home_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

