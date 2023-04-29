import pygame
import random
import sys
import time
from constants import BLACK,  RED, NAVY, YELLOW, LIGHT_GRAY, screen_width,\
    screen_height, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT, GRID_MARGIN_X, \
    GRID_MARGIN_Y, FONT
# Initialize Pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Connect Four")

def create_game_board():
    game_board = []
    for i in range(6):
        row = []
        for j in range(7):
            x = GRID_MARGIN_X + j * CELL_SIZE
            y = GRID_MARGIN_Y + i * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            row.append(rect)
        game_board.append(row)
    return game_board

def connect4_init():
    global game_board, game_state, current_player, game_over, winner
    game_board = create_game_board()

    # Set up the game state
    game_state = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(0)
        game_state.append(row)

    # Variables
    current_player = 1
    game_over = False
    winner = None

#reset game function
def connect4_reset_game():
    global game_board, game_state, current_player, game_over, winner

# Set up the game state
game_state = []
for i in range(6):
    row = []
    for j in range(7):
        row.append(0)
    game_state.append(row)

# Variables
current_player = 1
game_over = False
winner = None

# Functions
def draw_rounded_rect(surface, rect, color, radius):
    pygame.draw.circle(surface, color, (rect.left+radius, rect.top+radius), radius)
    pygame.draw.circle(surface, color, (rect.right-radius, rect.top+radius), radius)
    pygame.draw.circle(surface, color, (rect.left+radius, rect.bottom-radius), radius)
    pygame.draw.circle(surface, color, (rect.right-radius, rect.bottom-radius), radius)
    pygame.draw.rect(surface, color, pygame.Rect(rect.left+radius, rect.top, rect.width-2*radius, rect.height))
    pygame.draw.rect(surface, color, pygame.Rect(rect.left, rect.top+radius, rect.width, rect.height-2*radius))


def draw_frames():
    # Draw frame around the grid
    grid_frame = pygame.Rect(GRID_MARGIN_X - 10, GRID_MARGIN_Y - 10, GRID_WIDTH + 20, GRID_HEIGHT + 20)
    pygame.draw.rect(screen, NAVY, grid_frame, 5)

    # Draw frame around the side text area
    side_text_margin = 20
    side_text_width = 300
    side_text_height = 100
    side_text_x = screen_width - side_text_margin - side_text_width
    side_text_y = GRID_MARGIN_Y - 10
    side_text_frame = pygame.Rect(side_text_x - side_text_margin, side_text_y - side_text_margin,
                                  side_text_width + 2 * side_text_margin, side_text_height + 2 * side_text_margin)# 2 2
    pygame.draw.rect(screen, NAVY, side_text_frame, 5)


def draw_game_board():
    screen.fill(LIGHT_GRAY)
    for i in range(6):
        for j in range(7):
            rect = game_board[i][j]
            draw_rounded_rect(screen, rect, NAVY, CELL_SIZE // 2 - 2)
            if game_state[i][j] != 0:
                color = RED if game_state[i][j] == 1 else YELLOW
                pygame.draw.circle(screen, color, rect.center, CELL_SIZE // 2 - 10)
    draw_player_buttons(current_player)
    draw_side_text(current_player, winner)
    draw_frames()
    pygame.display.update()


def get_color(player):
    return RED if player == 1 else YELLOW


def is_draw():
    for i in range(6):
        for j in range(7):
            if game_state[i][j] == 0:
                return False
    return True


def check_winner(player):
    # Check horizontal
    for row in range(6):
        for col in range(4):
            if game_state[row][col] == player and game_state[row][col + 1] == player and game_state[row][col + 2] == player and game_state[row][col + 3] == player:
                return True, [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]

    # Check vertical
    for col in range(7):
        for row in range(3):
            if game_state[row][col] == player and game_state[row + 1][col] == player and game_state[row + 2][col] == player and game_state[row + 3][col] == player:
                return True, [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]

    # Check diagonal (bottom-left to top-right)
    for row in range(3):
        for col in range(4):
            if game_state[row][col] == player and game_state[row + 1][col + 1] == player and game_state[row + 2][col + 2] == player and game_state[row + 3][col + 3] == player:
                return True, [(row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)]

    # Check diagonal (top-left to bottom-right)
    for row in range(3, 6):
        for col in range(4):
            if game_state[row][col] == player and game_state[row - 1][col + 1] == player and game_state[row - 2][col + 2] == player and game_state[row - 3][col + 3] == player:
                return True, [(row, col), (row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)]

    return False, []


def flash_winning_tiles(winning_tiles):
    for _ in range(5):
        for row, col in winning_tiles:
            rect = game_board[row][col]
            color = game_state[row][col] == 1 and RED or YELLOW
            pygame.draw.circle(screen, color, rect.center, CELL_SIZE // 2 - 10)
        pygame.display.update()
        pygame.time.delay(200)
        for row, col in winning_tiles:
            rect = game_board[row][col]
            draw_rounded_rect(screen, rect, NAVY, CELL_SIZE // 2 - 2)
        pygame.display.update()
        pygame.time.delay(200)


def draw_player_buttons(current_player):
    color = get_color(current_player)
    for col in range(7):
        x = GRID_MARGIN_X + col * CELL_SIZE + CELL_SIZE // 2
        y = GRID_MARGIN_Y + GRID_HEIGHT + 50
        pygame.draw.circle(screen, color, (x, y), CELL_SIZE // 2 - 10)


def drop_piece(col, player):
    for row in range(5, -1, -1):
        if game_state[row][col] == 0:
            game_state[row][col] = player
            return True
    return False

def get_column_from_mouse_pos(mouse_pos):
    for col in range(7):
        if GRID_MARGIN_X + col * CELL_SIZE <= mouse_pos[0] < GRID_MARGIN_X + (col + 1) * CELL_SIZE:
            return col
    return -1

def cpu_move():
    return random.choice([col for col in range(7) if game_state[0][col] == 0])


def wrap_text(text, font, max_width):
    words = text.split(' ')
    wrapped_lines = []
    current_line = words[0]

    for word in words[1:]:
        if font.size(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            wrapped_lines.append(current_line)
            current_line = word

    wrapped_lines.append(current_line)
    return wrapped_lines


def draw_side_text(current_player, winner):
    if winner:
        message = "Yay You win!" if winner == 1 else "Sorry I won"
    elif current_player == 1:
        message = "Click in any column to drop your piece. You are playing Red."
    else:
        message = "I'm thinking..."

    max_text_width = 260
    wrapped_text = wrap_text(message, FONT, max_text_width)

    # Position the text in the top right corner
    side_text_margin = 30
    side_text_width = 300
    side_text_x = screen_width - side_text_margin - side_text_width
    side_text_y = GRID_MARGIN_Y - 10

    total_text_height = len(wrapped_text) * FONT.get_height()
    side_text_box_height = 100

    for idx, line in enumerate(wrapped_text):
        text = FONT.render(line, True, BLACK)
        text_rect = text.get_rect()
        text_rect.centerx = side_text_x + side_text_width // 2
        text_rect.centery = side_text_y + side_text_box_height // 2 - total_text_height // 2 + (idx * FONT.get_height())
        screen.blit(text, text_rect)


def reset_board():
    global game_state, current_player, game_over, winner
    game_state = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(0)
        game_state.append(row)
    current_player = 1
    game_over = False
    winner = None


# Game loop
def connect4_main(window_caption="Connect Four"):
    global game_over, current_player, winner
    current_player = 1
    game_over = False
    winner = None

    connect4_init()

    while not game_over:
        draw_game_board()

        if current_player == 2:
            pygame.time.delay(550)
            col = cpu_move()
            if drop_piece(col, current_player):
                win, winning_tiles = check_winner(current_player)
                if win:
                    flash_winning_tiles(winning_tiles)
                    winner = current_player
                    game_over = True
                elif is_draw():
                    winner = "draw"
                    game_over = True
                else:
                    current_player = 3 - current_player
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not game_over:
                        mouse_pos = pygame.mouse.get_pos()
                        col = get_column_from_mouse_pos(mouse_pos)

                        if col != -1 and drop_piece(col, current_player):
                            win, winning_tiles = check_winner(current_player)
                            if win:
                                flash_winning_tiles(winning_tiles)
                                winner = current_player
                                game_over = True
                            elif is_draw():
                                winner = "draw"
                                game_over = True
                            else:
                                current_player = 3 - current_player

    if winner == "draw":
        return "draw"
    elif winner == 1:
        return "player_win"
    else:
        return "player_lose"


if __name__ == "__main__":
    connect4_main()
