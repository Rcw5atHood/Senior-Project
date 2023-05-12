import pygame
import random

pygame.font.init()

# GLOBALS VARS
s_width = 1425
s_height = 825
play_width = 300
play_height = 600
block_size = 30
difficulty = "Easy" # or "Hard"
selected_difficulty = 'Easy'  # start with 'Easy' as the default

top_left_x = (s_width - play_width) // 2
top_left_y = (s_height - play_height) // 2

from constants import shapes, shape_colors


class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def draw_difficulty_buttons(surface, current_difficulty):
    global selected_difficulty

    font = pygame.font.SysFont('comicsans', 30)
    easy_label = font.render('Easy', 1, (255, 255, 255))
    hard_label = font.render('Hard', 1, (255, 255, 255))

    # Define button dimensions
    button_width = 60
    button_height = 30

    # Define button positions
    easy_button_x = s_width - 2 * button_width - 50
    easy_button_y = s_height - button_height - 20

    hard_button_x = s_width - button_width - 20
    hard_button_y = s_height - button_height - 20

    easy_button = pygame.Rect(easy_button_x, easy_button_y, button_width, button_height)
    hard_button = pygame.Rect(hard_button_x, hard_button_y, button_width, button_height)

    # Draw a border around the selected button
    border_thickness = 5
    if current_difficulty == 'Easy':
        pygame.draw.rect(surface, (255, 0, 0), easy_button.inflate(border_thickness*2, border_thickness*2))
    elif current_difficulty == 'Hard':
        pygame.draw.rect(surface, (255, 0, 0), hard_button.inflate(border_thickness*2, border_thickness*2))

    # Draw the buttons
    pygame.draw.rect(surface, (0, 0, 0), easy_button)  # draw button
    pygame.draw.rect(surface, (0, 0, 0), hard_button)  # draw button
    surface.blit(easy_label, (easy_button_x, easy_button_y))
    surface.blit(hard_label, (hard_button_x, hard_button_y))

    # Check for mouse click on the difficulty buttons
    if pygame.mouse.get_pressed()[0]:
        if easy_button.collidepoint(pygame.mouse.get_pos()):
            selected_difficulty = 'Easy'
        elif hard_button.collidepoint(pygame.mouse.get_pos()):
            selected_difficulty = 'Hard'

    return easy_button, hard_button


def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color, x_offset=0, y_offset=0):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2) + x_offset, top_left_y + play_height / 2 - (label.get_height() / 2) + y_offset))


def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * 30), (sx + play_width, sy + i * 30))
        for j in range(col):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))


def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                del locked[(j, i)]

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                new_key = (x, y + inc)
                locked[new_key] = locked.pop(key)

    return inc


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_text_left(text, size, color, surface, y_offset):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x - label.get_width() - 10, top_left_y + y_offset))


def draw_window(surface, grid):
    surface.fill((200, 200, 200))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # Instructions
    draw_text_left("Up to Rotate", 30, (255, 255, 255), surface, 200)
    draw_text_left("Left and Right to Move", 30, (255, 255, 255), surface, 240)
    draw_text_left("Space to Drop", 30, (255, 255, 255), surface, 280)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)

    # draw grid and border
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)
    # pygame.display.update()


def main():
    global selected_difficulty
    selected_difficulty = difficulty
    game_won = False
    target_score = 50 if selected_difficulty.lower() == "easy" else 150

    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')
    locked_positions = {}

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    current_piece.rotation %= len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1
                        current_piece.rotation %= len(current_piece.shape)
                if event.key == pygame.K_SPACE:
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                    current_piece.y -= 1

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        easy_button, hard_button = draw_difficulty_buttons(win, selected_difficulty)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "Great Job!", 80, (255, 255, 255), x_offset=375, y_offset=100)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            game_won = True
        if score >= target_score:
            draw_text_middle(win, "You Won!", 80, (255, 255, 255), x_offset=375, y_offset=100)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            game_won = True
    return game_won, difficulty

difficulty = "Easy"
selected_difficulty = "Easy"


def main_menu(win, difficulty_param, selected_difficulty):
    global difficulty
    run = True
    while run:
        win.fill((0, 0, 0))
        draw_text_middle(win, "Press Any Key To Play", 60, (255, 255, 255))

        # Draw the buttons with the updated selected difficulty
        easy_button, hard_button = draw_difficulty_buttons(win, selected_difficulty)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                game_won, difficulty = main(difficulty)
                if game_won:
                    print("Game Won:", game_won)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(pos):
                    difficulty = "Easy"
                    selected_difficulty = "Easy"
                elif hard_button.collidepoint(pos):
                    difficulty = "Hard"
                    selected_difficulty = "Hard"



win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')


def tetris_main():
    main()


if __name__ == "__main__":
    main()