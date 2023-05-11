import pygame
pygame.init()
import pygame.font

pygame.init()

font = pygame.font.Font(None, 36)
FPS = 60


# constants.py
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
NAVY = (0, 0, 128)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

WIDTH = 1024
HEIGHT = 768
#tetris.py
# SHAPE FORMATS
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


#Connect4.py
# Screen settings
screen_width = 1024
screen_height = 768
CELL_SIZE = 75
GRID_WIDTH = 7 * CELL_SIZE
GRID_HEIGHT = 6 * CELL_SIZE
GRID_MARGIN_X = 40#20
GRID_MARGIN_Y = (screen_height - GRID_HEIGHT) // 2 - 40
BUTTON_HEIGHT = 50
# Fonts
FONT = pygame.font.Font(None, 30)

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


# Add game choice info text
game_choice_text = welcome_font.render("Would you like to play a game? Pick one of these.", True, BLACK)
game_choice_text_rect = game_choice_text.get_rect()
game_choice_text_rect.center = (750,650)

# Add welcome text
welcome_text = welcome_font.render("Greetings traveler, would you like to take an adventure with us?", True, BLACK)
welcome_text_rect = welcome_text.get_rect()
welcome_text_rect.center = (750,150)

# Add exit message info text
exit_info_text = welcome_font.render("If you'd like to adventure another time, "
                                     "press exit to be returned to your reality.", True, BLACK)
exit_info_text_rect = exit_info_text.get_rect()
exit_info_text_rect.center = (750, 750)#screen_width // 2


exit_message_text = font.render("Good Bye and thank you for adventuring with us", True, BLACK, LIGHT_GRAY)
exit_message_rect = exit_message_text.get_rect()
exit_message_rect.center = (750,475)

# Load the agent image from file
agent_image = pygame.image.load('agent.jpeg')
agent_image = pygame.transform.scale(agent_image, (screen_width // 1.5, screen_height // 1.5))
agent_rect = agent_image.get_rect()


# Load text and images
destinations = ["Paris", "New York", "Tokyo", "Sydney", "Cairo", "Agra", "Dubrovnik",
                "Copenhagen","Santorini", "Reykjavik", "Cinque Terre", "Rome", "Petra", "Oslo", "Svalbard", "Machu Picchu", "Lisbon",
                "Moscow", "Edinburgh", "Singapore City", "Cape Town", "Seoul", "Barcelona", "Granada", "Madrid",
                "Hanoi"
                ]

destinations_info = {
    "Paris": "Iconic landmarks, including the Eiffel Tower, Notre-Dame Cathedral, and the Arc de Triomphe.",
    "New York": "If you can make it here you can make it anywhere!",
    "Tokyo": "A vibrant and bustling city with sites like the Shibuya Crossing, the Tokyo Skytree.",
    "Sydney": "The largest city in Australia!",
    "Cairo": "Home of the ancient pyramids!",
    "Agra": "Taj Mahal: A white marble mausoleum built in the 17th century by Mughal Emperor Shah Jahan.",
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
    #"Hood College": "Hood is home.",

}
destination_filenames = {
        "Paris": 'paris.jpeg',
        "New York": 'newyork.jpeg',
        "Tokyo": 'Tokyo.jpeg',
        "Sydney": 'Sydney.jpeg',
        "Cairo": 'cairo.jpeg',
        "Agra": 'Agra.jpeg',
        "Dubrovnik": 'dubrovnik.jpeg',
        "Copenhagen": 'Copenhagen.jpeg',
        "Santorini": 'Santorini.jpeg',
        "Reykjavik": 'reykjavik.jpeg',
        "Cinque Terre": 'cinque terre.jpeg',
        "Rome": 'Rome.jpeg',
        "Petra": 'Petra.jpeg',
        "Oslo": 'Oslo.jpeg',
        "Svalbard": 'Svalbard.jpeg',
        "Machu Picchu": 'Machu Picchu.jpeg',
        "Lisbon": 'Lisbon.jpeg',
        "Moscow": 'Moscow.jpeg',
        "Edinburgh": 'Edinburgh.jpeg',
        "Singapore City": 'Singapore.jpeg',
        "Cape Town": 'Cape Town.jpeg',
        "Seoul": 'Seoul.jpeg',
        "Barcelona": 'Barcelona.jpeg',
        "Granada": 'Granada.jpeg',
        "Madrid": 'Madrid.jpeg',
        "Hanoi": 'Hanoi.jpeg',
        #"Hood College": 'Hood College.jpeg',
    }
####


