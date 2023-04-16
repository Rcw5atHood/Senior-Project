import pygame
import random
from constants import  BLUE,BLACK, RED, WHITE

def tictactoe_main():
    # Initialize pygame
    pygame.init()

    # Constants
    CELL_SIZE = 256
    WIDTH, HEIGHT = CELL_SIZE * 3, CELL_SIZE * 3

    LINE_WIDTH = CELL_SIZE // 64
    # Initialize window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("X O Game")

    # Variables
    turn = "player"
    board = {i: "" for i in range(9)}
    player_symbol = "X"
    computer_symbol = "O"
    font = pygame.font.Font(None, 120)
    playing = True
    game_over = False

    def computer_move():
        nonlocal turn
        if turn == "computer":
            empty_cells = [i for i in range(9) if board[i] == ""]
            if empty_cells:
                selected_cell = random.choice(empty_cells)
                board[selected_cell] = computer_symbol
                turn = "player"

    def draw_board():
        for i in range(9):
            x, y = (i % 3) * CELL_SIZE, (i // 3) * CELL_SIZE
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            symbol = board[i]
            color = RED if symbol == "X" else BLUE
            if symbol != "":
                text = font.render(symbol, True, color)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

        # Draw the box around the grid
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), LINE_WIDTH)

    def get_cell(x, y):
        return (x // CELL_SIZE) + (y // CELL_SIZE) * 3

    def show_message(message):
        nonlocal game_over
        font_big = pygame.font.Font(None, 60)
        text = font_big.render(message, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.fill(WHITE)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        game_over = True
        return "player" if message == "You win!" else "computer"

    def rule():
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] and board[i] != "":
                return end_game(board[i])

        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] and board[i] != "":
                return end_game(board[i])

        if board[0] == board[4] == board[8] and board[0] != "":
            return end_game(board[0])

        if board[2] == board[4] == board[6] and board[2] != "":
            return end_game(board[2])

        return check_draw()

    def end_game(winner):
        return show_message("You win!") if winner == player_symbol else show_message("You lose!")

    def check_draw():
        if "" not in board.values():
            return show_message("It's a draw.")

    # Main game loop
    while playing:
        screen.fill(WHITE)
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.MOUSEBUTTONUP and turn == "player" and not game_over:
                x, y = pygame.mouse.get_pos()
                cell = get_cell(x, y)
                if board[cell] == "":
                    board[cell] = player_symbol
                    turn = "computer"
                    winner = rule()
                    if winner:
                        return winner
                    computer_move()
                    winner = rule()
                    if winner:
                        return winner

        pygame.display.flip()

    pygame.quit()

