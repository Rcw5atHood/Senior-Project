import pygame
import random
from pygconnect4 import pygconnect4_main

# Initialize Pygame
pygame.init()

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Set up the window
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Travel Adventure Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up button surfaces
start_button = font.render("Start", True, BLACK, WHITE)
start_rect = start_button.get_rect()
start_rect.center = (400, 300)

exit_button = font.render("Exit", True, BLACK, WHITE)
exit_rect = exit_button.get_rect()
exit_rect.center = (400, 350)

continue_button = font.render("Continue", True, BLACK, WHITE)
continue_rect = continue_button.get_rect()
continue_rect.center = (400, 500)

accept_game_button = font.render("Accept", True, BLACK, WHITE)
accept_game_rect = accept_game_button.get_rect()
accept_game_rect.center = (300, 400)

try_again_button = font.render("Try Again", True, BLACK, WHITE)
try_again_rect = try_again_button.get_rect()
try_again_rect.center = (300, 450)

return_home_button = font.render("Return Home", True, BLACK, WHITE)
return_home_rect = return_home_button.get_rect()
return_home_rect.center = (500, 450)

# Set up text surfaces
destinations = ["Paris", "New York", "Tokyo", "Sydney", "Cairo"]
destinations_info = {
    "Paris": "Welcome to Paris, the city of love!",
    "New York": "Welcome to New York, the city that never sleeps!",
    "Tokyo": "Welcome to Tokyo, the heart of Japan!",
    "Sydney": "Welcome to Sydney, the largest city in Australia!",
    "Cairo": "Welcome to Cairo, home of the ancient pyramids!",
}
exit_message_text = font.render("Good Bye and thank you for adventuring with us", True, BLACK, WHITE)
exit_message_rect = exit_message_text.get_rect()
exit_message_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

# Load images for destinations
paris_image = pygame.image.load('paris.jpg')
new_york_image = pygame.image.load('newyork.jpeg')
tokyo_image = pygame.image.load('tokyo.jpg')
sydney_image = pygame.image.load('sydney.jpg')
cairo_image = pygame.image.load('cairo.jpg')

# Store images in a dictionary
destination_images = {
       "Paris": paris_image,
    "New York": new_york_image,
    "Tokyo": tokyo_image,
    "Sydney": sydney_image,
    "Cairo": cairo_image,
}

visited = []
location = ""
location_text = None


player_won_text = font.render("You Won! Now we are moving to the next destination...", True, BLACK, WHITE)
computer_won_text = font.render("I Won! So sorry Try again.", True, BLACK, WHITE)
win_lose_text = None

agent_image = pygame.image.load('agent.jpg')
agent_rect = agent_image.get_rect()
agent_rect.center = (screen.get_width() // 2, screen.get_height() // 4)

# Set up game loop
running = True
current_screen = "start"
while running:

    if current_screen == "start":
        pygame.display.set_caption("Start")
    elif current_screen == "destination":
        pygame.display.set_caption(f"Destination {len(visited) + 1}: {location}")
    elif current_screen == "game_offer":
        pygame.display.set_caption("Would you like to play a game?")
    elif current_screen == "win_screen":
        pygame.display.set_caption("Player Won!")
    elif current_screen == "lose_screen":
        pygame.display.set_caption("Player Lost!")
    elif current_screen == "exit_screen":
        screen.fill(WHITE)
        screen.blit(exit_message_text, exit_message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Display the exit message for 2 seconds
        running = False

    if current_screen == "start":
        screen.blit(agent_image, agent_rect)
        screen.blit(start_button, start_rect)
        screen.blit(exit_button, exit_rect)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()


            if exit_rect.collidepoint(mouse_pos):
                current_screen = "exit_screen"

            if current_screen == "start":
                if start_rect.collidepoint(mouse_pos):
                    current_screen = "destination"
                    location = random.choice([x for x in destinations_info.keys() if x not in visited])
                    location_text = font.render("Current location: " + location, True, BLACK, WHITE)
                    location_info_text = font.render(destinations_info[location], True, BLACK, WHITE)

            elif current_screen == "destination":
                if continue_rect.collidepoint(mouse_pos):
                    current_screen = "game_offer"

            elif current_screen == "game_offer":
                if accept_game_rect.collidepoint(mouse_pos):
                    won_game = pygconnect4_main("Connect 4 Game")
                    if won_game == 1:
                        visited.append(location)
                        win_lose_text = player_won_text
                        current_screen = "win_screen"
                    else:
                        win_lose_text = computer_won_text
                        current_screen = "lose_screen"

            elif current_screen == "win_screen":
                if continue_rect.collidepoint(mouse_pos):
                    current_screen = "destination"
                    location = random.choice([x for x in destinations if x not in visited])
                    location_text = font.render("Current location: " + location, True, BLACK, WHITE)
                    location_info_text = font.render(destinations_info[location], True, BLACK, WHITE)

            elif current_screen == "lose_screen":
                if try_again_rect.collidepoint(mouse_pos):
                    current_screen = "game_offer"
                elif return_home_rect.collidepoint(mouse_pos):
                    current_screen = "start"

    # Draw the screen
    screen.fill(WHITE)
    if current_screen == "start":
        screen.blit(start_button, start_rect)
        screen.blit(exit_button, exit_rect)
    elif current_screen == "destination":
        if location in destination_images:
            image = destination_images[location]
            image_rect = image.get_rect()
            image_rect.center = (screen.get_width() // 2, screen.get_height() // 4)
            screen.blit(image, image_rect)

        location_info_text_width, location_info_text_height = location_info_text.get_size()
        location_info_text_x = (screen.get_width() - location_info_text_width) // 2
        location_info_text_y = (screen.get_height() - location_info_text_height) // 2
        screen.blit(location_info_text, (location_info_text_x, location_info_text_y))

        location_text_y = location_info_text_y - location_text.get_height() - 20
        screen.blit(location_text, (location_info_text_x, location_text_y))

        screen.blit(continue_button, continue_rect)

    elif current_screen == "game_offer":
        game_offer_text = font.render(
            "Would you like to play a game? To continue you'll have to win.", True, BLACK,
            WHITE)
        game_offer_text_rect = game_offer_text.get_rect()
        game_offer_text_rect.center = (screen.get_width() // 2, screen.get_height() // 4)
        screen.blit(game_offer_text, game_offer_text_rect)

        screen.blit(accept_game_button, accept_game_rect)
        screen.blit(exit_button, exit_rect)

    elif current_screen == "win_screen":
        win_lose_text_rect = win_lose_text.get_rect()
        win_lose_text_rect.center = (screen.get_width() // 2, screen.get_height() // 4)
        screen.blit(win_lose_text, win_lose_text_rect)

        screen.blit(continue_button, continue_rect)

    elif current_screen == "lose_screen":
        win_lose_text_rect = win_lose_text.get_rect()
        win_lose_text_rect.center = (screen.get_width() // 2, screen.get_height() // 4)
        screen.blit(win_lose_text, win_lose_text_rect)

        screen.blit(try_again_button, try_again_rect)
        screen.blit(return_home_button, return_home_rect)

    pygame.display.flip()
    clock.tick(FPS)
    if not running and current_screen == "exit_screen":
        screen.fill(WHITE)
        screen.blit(exit_message_text, exit_message_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

pygame.quit()

