import pygame
pygame.init()
import random
from connect4 import connect4_main
from tictactoe import tictactoe_main
from tetris import tetris_main
from constants import *


def load_destination_images(destination_filenames):
    destination_images = {}
    for destination, filename in destination_filenames.items():
        destination_images[destination] = pygame.transform.scale(
            pygame.image.load(filename).convert(), (800, 600)
        )
    return destination_images

pygame.mixer.init()
soundtracks = ['slowjam.mp3', 'slowjam1.mp3', 'slowjam2.mp3', 'slowjam3.mp3','slowjam5.mp3']
current_track = 0

pygame.mixer.music.load(soundtracks[current_track])
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
pygame.mixer.music.set_volume(0.25)

# Set up font
font = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()
FPS = 60
# Set up the window
screen_width = 1425
screen_height = 825
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)

# Load and scale the destination images
destination_images = load_destination_images(destination_filenames)
pygame.display.set_caption("Travel Adventure Game")
buffer = pygame.Surface((screen_width, screen_height))


welcome_font = pygame.font.SysFont('comicsans', 30)

gameman_images = ['gameman1.jpeg', 'gameman2.jpeg', 'gameman3.jpeg', 'gameman4.jpeg']


def get_random_gameman_image():
    return pygame.transform.scale(pygame.image.load(random.choice(gameman_images)).convert(), (800, 600))
current_gameman_image = get_random_gameman_image()


visited = []
location = ""
location_text = ""
win_text, win_text_rect = None, None
current_screen = "start"
winner = None
back_to_base = False #

def set_caption(title):
    pygame.display.set_caption(title)


def draw_start_screen():
    agent_rect.center = (750, 450)
    buffer.blit(agent_image, agent_rect)
    buffer.blit(start_button, start_rect)
    buffer.blit(exit_button, exit_rect)

    if back_to_base:
        hood_image = pygame.image.load('Hood College.jpeg').convert()
        hood_image = pygame.transform.scale(hood_image, (800, 600))
        hood_image_rect = hood_image.get_rect()
        hood_image_rect.center = (screen_width // 2, screen_height // 2)
        buffer.blit(hood_image, hood_image_rect)

        location_text = "Hood Is Home."
        location_text_surface = font.render(location_text, True, BLACK)
        location_text_rect = location_text_surface.get_rect(center=(screen_width // 2, screen_height - 50))
        buffer.blit(location_text_surface, location_text_rect)

        leaving_text = "Leaving so soon? Or did you wanna keep going?"
        leaving_text_surface = font.render(leaving_text, True, BLACK)
        leaving_text_rect = leaving_text_surface.get_rect(center=(screen_width // 2, 30))
        buffer.blit(leaving_text_surface, leaving_text_rect)

        # Enable the Travel Onward button
        if len(visited) <= 19:
            buffer.blit(continue_button, continue_rect)
        else:
            inactive_continue_button = font.render("Travel Onward", True, LIGHT_GRAY)
            buffer.blit(inactive_continue_button, continue_rect)

    else:
        if len(visited) < 19:
            buffer.blit(welcome_text, welcome_text_rect)
            buffer.blit(exit_info_text, exit_info_text_rect)

        # Display the statement when the player has visited 19 locations
        if len(visited) >= 19:
            statement_text = "I'm afraid that is as far as we go today, come back another time!"
            statement_surface = font.render(statement_text, True, BLACK)
            statement_rect = statement_surface.get_rect(center=(screen_width // 2, 30))
            buffer.blit(statement_surface, statement_rect)


def draw_button(text, rect, text_color, button_color, action=None):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    buffer.blit(text_surface, text_rect)

    if action is not None:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(rect).collidepoint(event.pos):
                    action()


def draw_destination_screen():
    global screen_width, screen_height, current_gameman_image
    if location in destination_images:
        image = destination_images[location]
        image_rect = image.get_rect()
    else:
        pass
    image_rect.center = (screen_width // 2, screen_height // 2)
    buffer.blit(image, image_rect)

    # Display "Welcome to: _locationname_" at the top
    welcome_location_text = f"Welcome to: {location}"
    welcome_location_surface = font.render(welcome_location_text, True, BLACK)
    welcome_location_rect = welcome_location_surface.get_rect(center=(screen_width // 2, 50))
    buffer.blit(welcome_location_surface, welcome_location_rect)

    # Display location-specific text at the bottom
    if location in destinations_info:
        info_text = destinations_info[location]
        info_text_surface = font.render(info_text, True, BLACK)
        info_text_rect = info_text_surface.get_rect(center=(screen_width // 2, screen_height - 50))
        buffer.blit(info_text_surface, info_text_rect)

def draw_visited_destinations():
    header_text = "You've been to:"
    header_surface = font.render(header_text, True, BLACK)
    header_rect = header_surface.get_rect(topright=(screen_width - 10, 10))
    buffer.blit(header_surface, header_rect)

    for index, destination in enumerate(visited):
        destination_text = f"{index + 1}. {destination}"
        destination_surface = font.render(destination_text, True, BLACK)
        destination_rect = destination_surface.get_rect(topright=(screen_width - 10, 50 + index * 40))
        buffer.blit(destination_surface, destination_rect)


def draw_game_choice_screen():
    buffer.blit(connect4_button, connect4_rect)
    buffer.blit(tictactoe_button, tictactoe_rect)
    buffer.blit(tetris_button, tetris_rect)
    buffer.blit(continue_button, continue_rect)
    buffer.blit(return_home_button, return_home_rect)
    buffer.blit(game_choice_text, game_choice_text_rect)


    # Draw the current gameman image
    gameman_image_rect = current_gameman_image.get_rect()
    gameman_image_rect.center = (screen_width // 2, screen_height // 2)
    buffer.blit(current_gameman_image, gameman_image_rect)

    draw_visited_destinations()


    pygame.display.update()


def draw_game_over_screen(game_result):
    if game_result == "player_win":
        result_text = "You won! Shall we play again?"
    elif game_result == "player_lose":
        result_text = "You lost. Shall we play again?"
    else:
        result_text = "Right then- Let's GO!"

    win_lose_text = font.render(result_text, True, BLACK, LIGHT_GRAY)
    buffer.blit(win_lose_text, win_lose_text.get_rect(center=(screen_width // 2, screen_height // 2)))

    buffer.blit(continue_button, continue_rect)
    buffer.blit(play_another_game_button, play_another_game_rect)


def draw_exit_message_screen():
    screen.blit(exit_message_text, exit_message_rect)


def win_screen(result):
    if not pygame.font.get_init():
        pygame.font.init()
    if result.strip() == "":
        result = "Yay You won"
    win_text = font.render(f"{result}! Congratulations!", True, BLACK, LIGHT_GRAY)
    win_text_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2))

    pygame.time.delay(250)

    return win_text, win_text_rect


def handle_start_clicks(event):
    global current_screen, visited, location,back_to_base
    if start_rect.collidepoint(event.pos):
        current_screen = "destination"
        location = random.choice(destinations)
        visited.append(location)
        location_text = destinations_info[location]
    elif exit_rect.collidepoint(event.pos):
        current_screen = "exit_message"

        handle_exit_message_clicks(event)
    elif continue_rect.collidepoint(event.pos) and back_to_base:
        remaining_destinations = [x for x in destinations if x not in visited]
        if remaining_destinations and len(visited) < 19:
            location = random.choice(remaining_destinations)
            visited.append(location)
            location_text = destinations_info[location]
            current_screen = "destination"
            back_to_base = False
        else:
            current_screen = "start"
            visited = []
            back_to_base = False

    return True


def handle_destination_clicks(event):
    global current_screen, current_gameman_image
    if continue_rect.collidepoint(event.pos):
        current_screen = "game_choice"
        current_gameman_image = get_random_gameman_image()


def handle_game_choice_clicks(event):
    # Declare global variables
    global current_screen
    global winner
    global win_text, win_text_rect, location_text

    # Check which game button the user clicked on
    if connect4_rect.collidepoint(event.pos):
        # Run Connect 4 game and get the result
        winner = connect4_main()
    elif tictactoe_rect.collidepoint(event.pos):
        # Run Tic Tac Toe game and get the result
        winner = tictactoe_main()
    elif tetris_rect.collidepoint(event.pos):
        # Run Tetris game and get the result
        tetris_won = tetris_main()
        if tetris_won:
            winner = "player"
        else:
            winner = "computer"
    elif continue_rect.collidepoint(event.pos):
        # Set the current screen to "destination" if "continue" is clicked
        current_screen = "destination"
    elif return_home_rect.collidepoint(event.pos):
        # Set the current screen to "start" if "return home" is clicked
        current_screen = "start"
    else:
        # Set the winner to None if none of the above conditions are met
        winner = None

    # Check if there is a winner
    if winner is not None:
        if winner == "player":
            # Set the win text for all games
            win_text, win_text_rect = win_screen("You won the game!!")
            # Choose a random destination from the list of unvisited destinations
            location = random.choice([x for x in destinations if x not in visited])
            # Add the selected location to the visited list
            visited.append(location)
            # Get the information for the selected location
            location_text = destinations_info[location]
            # Set the current screen to "destination"
            current_screen = "destination"
        elif winner == "computer":
            # Set the current screen to "game_over" if the computer won
            current_screen = "game_over"
        # Set the current screen to "game_over" if there is a winner (either player or computer)
        current_screen = "game_over"


def handle_game_over_clicks(event):
    global current_screen, location, visited, back_to_base
    if continue_rect.collidepoint(event.pos):
        remaining_destinations = [x for x in destinations if x not in visited]
        if remaining_destinations and len(visited) < 19:
            location = random.choice(remaining_destinations)
            visited.append(location)
            location_text = destinations_info[location]
            current_screen = "destination"
            back_to_base = False
        else:
            current_screen = "start"
            visited = []
            back_to_base = True
    elif play_another_game_rect.collidepoint(event.pos):
        current_screen = "game_choice"
        visited = []
        back_to_base = False
    elif return_home_rect.collidepoint(event.pos):
        current_screen = "start"
        back_to_base = True
    else:
        pass


def handle_exit_message_clicks(event):
    global running
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        draw_exit_message_screen()
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False


def skip_track():
    global current_track
    current_track += 1
    if current_track >= len(soundtracks):
        current_track = 0
    pygame.mixer.music.load(soundtracks[current_track])
    pygame.mixer.music.play(-1)

def handle_skip_track_button(event):
    global current_track
    if skip_track_button.collidepoint(event.pos):
        current_track += 1
        if current_track >= len(soundtracks):
            current_track = 0
        pygame.mixer.music.load(soundtracks[current_track])
        pygame.mixer.music.play(-1)

skip_track_button = pygame.Rect(75, 200, 160, 40)



volume = 50  # Defines the volume variable
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start":
                handle_start_clicks(event)
            elif current_screen == "destination":
                handle_destination_clicks(event)
            elif current_screen == "game_choice":
                handle_game_choice_clicks(event)
            elif current_screen == "game_over":
                handle_game_over_clicks(event)
            handle_skip_track_button(event)

        if current_screen == "exit_message" and (
                event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN):
            running = False

    buffer.fill(LIGHT_GRAY)

    if current_screen == "start":
        draw_start_screen()
    elif current_screen == "destination":
        draw_destination_screen()
        buffer.blit(continue_button, continue_rect)
    elif current_screen == "game_choice":
        draw_game_choice_screen()
    elif current_screen == "game_over":
        draw_game_over_screen(winner)
        buffer.blit(return_home_button, return_home_rect)
    elif current_screen == "exit_message":
        draw_exit_message_screen()


    # Draw the skip track button
    draw_button("New Music", skip_track_button, BLACK, LIGHT_GRAY, action=skip_track)

    screen.blit(buffer, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
###
#slowjam1:  https://pixabay.com/music/pulses-relaxing-music-for-reflection-and-creativity-16102/
#slowjam2: https://pixabay.com/music/meditationspiritual-soothing-music-for-complete-relaxation-16103/
#slowjam2: https://pixabay.com/music/solo-piano-ambient-piano-check-link-in-description-prod-by-blackpybeats-109400/
#Play Tested by Taylor Brown. 28 April 2023 2200:She thinks she should play one more round of tetris.  (which was denied)
###