import pygame
import random
from connect4 import connect4_main
from constants import BLACK,  LIGHT_GRAY
from tictactoe import tictactoe_main
from tetris import tetris_main

# Initialize Pygame
pygame.init()

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
pygame.display.set_caption("Travel Adventure Game")
buffer = pygame.Surface((screen_width, screen_height))
# Create buttons
start_button = font.render("Start Here", True, BLACK, LIGHT_GRAY)
start_rect = start_button.get_rect()
start_rect.center = (150, 50)

exit_button = font.render("Exit", True, BLACK, LIGHT_GRAY)
exit_rect = exit_button.get_rect()
exit_rect.center = (150, 700)

continue_button = font.render("Travel Onward", True, BLACK, LIGHT_GRAY)
continue_rect = continue_button.get_rect()
continue_rect.center = (150, 300)

return_home_button = font.render("Back to Base", True, BLACK, LIGHT_GRAY)
return_home_rect = return_home_button.get_rect()
return_home_rect.center = (150, 600)

connect4_button = font.render("Connect 4", True, BLACK, LIGHT_GRAY)
connect4_rect = connect4_button.get_rect()
connect4_rect.center = (150, 350)

tictactoe_button = font.render("Tic Tac Toe", True, BLACK, LIGHT_GRAY)
tictactoe_rect = tictactoe_button.get_rect()
tictactoe_rect.center = (150, 400)

tetris_button = font.render("Tetris", True, BLACK, LIGHT_GRAY)
tetris_rect = tetris_button.get_rect()
tetris_rect.center = (150, 450)

play_another_game_button = font.render("Play Another Game?", True, BLACK, LIGHT_GRAY)
play_another_game_rect = play_another_game_button.get_rect()
play_another_game_rect.center = (175, 650)

welcome_font = pygame.font.SysFont('comicsans', 30)

gameman_images = ['gameman1.jpeg', 'gameman2.jpeg', 'gameman3.jpeg', 'gameman4.jpeg']


def get_random_gameman_image():
    return pygame.transform.scale(pygame.image.load(random.choice(gameman_images)).convert(), (800, 600))
current_gameman_image = get_random_gameman_image()


# Add game choice info text
game_choice_text = welcome_font.render("Would you like to play a game? Pick one of these.", True, BLACK)
game_choice_text_rect = game_choice_text.get_rect()
game_choice_text_rect.center = (screen_width // 2, screen_height - 40)  # bottom of the screen

# Add welcome text
welcome_text = welcome_font.render("Greetings traveler, would you like to take an adventure with us?", True, BLACK)
welcome_text_rect = welcome_text.get_rect()
welcome_text_rect.center = (screen_width // 2, 150)

# Add exit message info text
exit_info_text = welcome_font.render("If you'd like to adventure another time, "
                                     "press exit to be returned to your reality.", True, BLACK)
exit_info_text_rect = exit_info_text.get_rect()
exit_info_text_rect.center = (screen_width // 2, screen_height - 40)

# Load text and images
destinations = ["Paris", "New York", "Tokyo", "Sydney", "Cairo", "Agra", "Banff National Park", "Dubrovnik", "Copenhagen",
               "Santorini", "Reykjavik", "Cinque Terre", "Rome", "Petra", "Oslo", "Svalbard", "Machu Picchu", "Lisbon",
               "Moscow", "Edinburgh", "Singapore City", "Cape Town", "Seoul", "Barcelona", "Granada", "Madrid", "Hanoi",
               "Hood College"]


destinations_info = {
    "Paris": "Iconic landmarks, including the Eiffel Tower, Notre-Dame Cathedral, and the Arc de Triomphe.",
    "New York": "If you can make it here you can make it anywhere!",
    "Tokyo": "A vibrant and bustling city with sites like the Shibuya Crossing, the Tokyo Skytree.",
    "Sydney": "The largest city in Australia!",
    "Cairo": "Home of the ancient pyramids!",
    "Agra": "Taj Mahal: A white marble mausoleum built in the 17th century by Mughal Emperor Shah Jahan.",
    "Banff National Park": "A stunning national park with turquoise lakes, soaring mountains, and abundant wildlife.",
    "Dubrovnik": "Walled city on the Adriatic Sea that is known for its stunning architecture and historic Old Town.",
    "Copenhagen": "Gorgeous city with colorful buildings, charming canals, and beautiful parks like Tivoli Gardens.",
    "Santorini": "Greek island known for white-washed buildings, blue-domed churches, sitting on the Aegean Sea.",
    "Reykjavik": "Quite a quirky city with colorful houses, street art, and the iconic Hallgrimskirkja church.",
    "Cinque Terre": "Five colorful seaside villages perched on the rugged coastline of the Italian Riviera.",
    "Rome": "Home to ancient ruins and monuments, including the Colosseum, the Pantheon, and the Roman Forum.",
    "Petra": "Ancient city carved into rock, with magnificent temples, tombs, dating back to the 4th century BC.",
    "Oslo": "Surrounded by beautiful natural scenery, including the Oslofjord and nearby forests and mountains.",
    "Svalbard": "An Arctic archipelago known for its stunning natural beauty, glaciers, icebergs, and wildlife.",
    "Machu Picchu": "An ancient Incan city perched high in the Andes Mountains, surrounded by stunning views.",
    "Lisbon": "Known for colorful and historic neighborhoods, and scenic views like the Miradouro de Santa Luzia.",
    "Moscow": "Home to many iconic landmarks, including Red Square, St. Basil's Cathedral, and the Moscow Kremlin.",
    "Edinburgh": "Known for its stunning architecture, including the historic Edinburgh Castle and the Royal Mile.",
    "Singapore City": "Modern futuristic this city boasts of having the Marina Bay Sands and the Supertree Grove.",
    "Cape Town": "Known for its stunning natural scenery, including Table Mountain and the Cape of Good Hope.",
    "Seoul": "Known for futuristic architecture, including the Dongdaemun Design Plaza and the Lotte World Tower.",
    "Barcelona": "Known for unique architecture, such as the Sagrada Familia cathedral designed by Antoni Gaudi.",
    "Granada": "The Alhambra palace and gardens, known for intricate Islamic architecture and beautiful courtyards.",
    "Madrid": "Grand plazas, like the Plaza Mayor and the Puerta del Sol, surrounded by historic buildings.",
    "Hanoi": "Known for beautiful lakes and parks, including Hoan Kiem Lake and the Hanoi Botanical Garden.",
    "Hood College": "Hood is home."
}

destination_images = {
    "Paris": pygame.transform.scale(pygame.image.load('paris.jpeg').convert(), (800, 600)),
    "New York": pygame.transform.scale(pygame.image.load('newyork.jpeg').convert(), (800, 600)),
    "Tokyo": pygame.transform.scale(pygame.image.load('Tokyo.jpeg').convert(), (800, 600)),
    "Sydney": pygame.transform.scale(pygame.image.load('Sydney.jpeg').convert(), (800, 600)),
    "Cairo": pygame.transform.scale(pygame.image.load('cairo.jpeg').convert(), (800, 600)),
    "Agra": pygame.transform.scale(pygame.image.load('Agra.jpeg').convert(), (800, 600)),
    "Banff National Park": pygame.transform.scale(pygame.image.load('Banff National Park.jpeg').convert(), (800, 600)),
    "Dubrovnik": pygame.transform.scale(pygame.image.load('dubrovnik.jpeg').convert(), (800, 600)),
    "Copenhagen": pygame.transform.scale(pygame.image.load('Copenhagen.jpeg').convert(), (800, 600)),
    "Santorini": pygame.transform.scale(pygame.image.load('Santorini.jpeg').convert(), (800, 600)),
    "Reykjavik": pygame.transform.scale(pygame.image.load('reykjavik.jpeg').convert(), (800, 600)),
    "Cinque Terre": pygame.transform.scale(pygame.image.load('cinque terre.jpeg').convert(), (800, 600)),
    "Rome": pygame.transform.scale(pygame.image.load('Rome.jpeg').convert(), (800, 600)),
    "Petra": pygame.transform.scale(pygame.image.load('Petra.jpeg').convert(), (800, 600)),
    "Oslo": pygame.transform.scale(pygame.image.load('Oslo.jpeg').convert(), (800, 600)),
    "Svalbard": pygame.transform.scale(pygame.image.load('Svalbard.jpeg').convert(), (800, 600)),
    "Machu Picchu": pygame.transform.scale(pygame.image.load('Machu Picchu.jpeg').convert(), (800, 600)),
    "Lisbon": pygame.transform.scale(pygame.image.load('Lisbon.jpeg').convert(), (800, 600)),
    "Moscow": pygame.transform.scale(pygame.image.load('Moscow.jpeg').convert(), (800, 600)),
    "Edinburgh": pygame.transform.scale(pygame.image.load('Edinburgh.jpeg').convert(), (800, 600)),
    "Singapore City": pygame.transform.scale(pygame.image.load('Singapore.jpeg').convert(), (800, 600)),
    "Cape Town": pygame.transform.scale(pygame.image.load('Cape Town.jpeg').convert(), (800, 600)),
    "Seoul": pygame.transform.scale(pygame.image.load('Seoul.jpeg').convert(), (800, 600)),
    "Barcelona": pygame.transform.scale(pygame.image.load('Barcelona.jpeg').convert(), (800, 600)),
    "Granada": pygame.transform.scale(pygame.image.load('Granada.jpeg').convert(), (800, 600)),
    "Madrid": pygame.transform.scale(pygame.image.load('Madrid.jpeg').convert(), (800, 600)),
    "Hanoi": pygame.transform.scale(pygame.image.load('Hanoi.jpeg').convert(), (800, 600)),
    "Hood College": pygame.transform.scale(pygame.image.load('Hood College.jpeg').convert(), (800, 600))
}

exit_message_text = font.render("Good Bye and thank you for adventuring with us", True, BLACK, LIGHT_GRAY)
exit_message_rect = exit_message_text.get_rect()
exit_message_rect.center = (screen_width // 2, screen_height // 2)

# Load the agent image from file
agent_image = pygame.image.load('agent.jpeg')
agent_image = pygame.transform.scale(agent_image, (screen_width // 1.5, screen_height // 1.5))
agent_rect = agent_image.get_rect()

visited = []
location = ""
location_text = ""
win_text, win_text_rect = None, None
current_screen = "start"
winner = None


def set_caption(title):
    pygame.display.set_caption(title)

def draw_start_screen():
    agent_rect.center = (800, 500)
    buffer.blit(agent_image, agent_rect)
    buffer.blit(start_button, start_rect)
    buffer.blit(exit_button, exit_rect)
    buffer.blit(welcome_text, welcome_text_rect)
    buffer.blit(exit_info_text, exit_info_text_rect)


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

    pygame.display.update()


def draw_game_over_screen(game_result):
    if game_result == "player_win":
        result_text = "You won! Shall we play again?"
    elif game_result == "player_lose":
        result_text = "You lost. Shall we play again?"
    else:
        result_text = "That was Fun! Shall we play again?"

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

    # Add a delay before moving to the next destination
    pygame.time.delay(500)

    return win_text, win_text_rect


def handle_start_clicks(event):
    global current_screen
    global location
    if start_rect.collidepoint(event.pos):
        current_screen = "destination"
        location = random.choice(destinations)
        visited.append(location)
        location_text = destinations_info[location]
    elif exit_rect.collidepoint(event.pos):
        current_screen = "exit_message"

        handle_exit_message_clicks(event)

    return True


def handle_destination_clicks(event):
    global current_screen, current_gameman_image
    if continue_rect.collidepoint(event.pos):
        current_screen = "game_choice"
    if continue_rect.collidepoint(event.pos):
        current_screen = "game_choice"
        current_gameman_image = get_random_gameman_image()


def handle_game_choice_clicks(event):
    global current_screen
    global winner
    global win_text, win_text_rect, location_text

    if connect4_rect.collidepoint(event.pos):
        winner = connect4_main()
    elif tictactoe_rect.collidepoint(event.pos):
        winner = tictactoe_main()
    elif tetris_rect.collidepoint(event.pos):
        winner = tetris_main()
        win_text, win_text_rect = win_screen("Great Job")  # Always show "Great Job" after Tetris game
    elif continue_rect.collidepoint(event.pos):
        current_screen = "destination"
    elif return_home_rect.collidepoint(event.pos):
        current_screen = "start"
    else:
        winner = None

    if winner == "player":
        if not (tetris_rect.collidepoint(event.pos)):
            win_text, win_text_rect = win_screen("You won the game")
        location = random.choice([x for x in destinations if x not in visited])
        visited.append(location)
        location_text = destinations_info[location]
        current_screen = "destination"
    elif winner == "computer":
        current_screen = "game_over"

    if winner is not None:
        current_screen = "game_over"


def handle_game_over_clicks(event):
    global current_screen
    global location
    if continue_rect.collidepoint(event.pos):
        remaining_destinations = [x for x in destinations if x not in visited]
        if remaining_destinations:
            location = random.choice(remaining_destinations)
            visited.append(location)
            location_text = destinations_info[location]
            current_screen = "destination"
        else:
            # Handle the case when all destinations have been visited
            location_text = "All Currently available destinations have been visited."
            current_screen = "destination"
    elif play_another_game_rect.collidepoint(event.pos):
        current_screen = "game_choice"
    elif return_home_rect.collidepoint(event.pos):
        current_screen = "start"


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


def set_volume(volume):
    pygame.mixer.music.set_volume(volume)


def handle_skip_track_button(event):
    global current_track
    if skip_track_button.collidepoint(event.pos):
        current_track += 1
        if current_track >= len(soundtracks):
            current_track = 0
        pygame.mixer.music.load(soundtracks[current_track])
        pygame.mixer.music.play(-1)


skip_track_button = pygame.Rect(75, 200, 160, 40)


def draw_volume_buttons():
    pygame.draw.rect(buffer, LIGHT_GRAY, skip_track_button)

    skip_track_text = font.render("New Music", True, BLACK)
    buffer.blit(skip_track_text, skip_track_button)


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
        draw_game_over_screen(winner)  # Pass winner here
        buffer.blit(return_home_button, return_home_rect)
    elif current_screen == "exit_message":
        draw_exit_message_screen()

    draw_volume_buttons()

    screen.blit(buffer, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)
###
#slowjam1:  https://pixabay.com/music/pulses-relaxing-music-for-reflection-and-creativity-16102/
#slowjam2: https://pixabay.com/music/meditationspiritual-soothing-music-for-complete-relaxation-16103/
#slowjam2: https://pixabay.com/music/solo-piano-ambient-piano-check-link-in-description-prod-by-blackpybeats-109400/
#Play Tested by Taylor Brown. 28 April 2023 2200:She thinks she should play one more round of tetris.  (which was denied)
