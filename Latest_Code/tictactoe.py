import pygame
import random
from constants import BLUE, BLACK, RED, WHITE,LIGHT_GRAY
COMPUTER_MOVE_EVENT = pygame.USEREVENT + 1

def tictactoe_main():
    # Initialize pygame
    pygame.init()

    # Constants
    CELL_SIZE = 225#was 250
    WIDTH, HEIGHT = CELL_SIZE * 3, CELL_SIZE * 3
    WINDOW_WIDTH, WINDOW_HEIGHT = 1425, 825
    LINE_WIDTH = CELL_SIZE // 64
    # Offset to center the Tic-Tac-Toe board in the window
    OFFSET_X = (WINDOW_WIDTH - WIDTH) // 2
    OFFSET_Y = (WINDOW_HEIGHT - HEIGHT) // 2
    # Initialize window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")


    # Variables
    turn = "player"
    board = {i: "" for i in range(9)}
    player_symbol = "X"
    computer_symbol = "O"
    font = pygame.font.Font(None, 120)
    playing = True
    game_over = False
    first_computer_move = True

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
            x, y = (i % 3) * CELL_SIZE + OFFSET_X, (i // 3) * CELL_SIZE + OFFSET_Y
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
            symbol = board[i]
            color = RED if symbol == "X" else BLUE
            if symbol != "":
                text = font.render(symbol, True, color)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE + OFFSET_X, OFFSET_Y), (i * CELL_SIZE + OFFSET_X, HEIGHT + OFFSET_Y), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (OFFSET_X, i * CELL_SIZE + OFFSET_Y), (WIDTH + OFFSET_X, i * CELL_SIZE + OFFSET_Y), LINE_WIDTH)
        # Draw the box around the grid
        pygame.draw.rect(screen, BLACK, (OFFSET_X, OFFSET_Y, WIDTH, HEIGHT), LINE_WIDTH)

    def get_cell(x, y):
        return ((x - OFFSET_X) // CELL_SIZE) + ((y - OFFSET_Y) // CELL_SIZE) * 3

    def show_message(message):
        nonlocal game_over
        font_big = pygame.font.Font(None, 60)
        text = font_big.render(message, True, BLACK)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.fill(LIGHT_GRAY)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)
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

    def draw_prompt(text):
        prompt_font = pygame.font.Font(None, 36)
        prompt_text = prompt_font.render(text, True, BLACK)
        prompt_rect = prompt_text.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        screen.blit(prompt_text, prompt_rect)

    # Main game loop
    while playing:
        screen.fill(LIGHT_GRAY)
        draw_board()

        if turn == "player":
            draw_prompt("Double Click to place your X")
        else:
            draw_prompt("I'm thinking...")

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

                    pygame.time.set_timer(COMPUTER_MOVE_EVENT, 1000)

            if event.type == COMPUTER_MOVE_EVENT:
                pygame.time.set_timer(COMPUTER_MOVE_EVENT, 0)

                computer_move()
                winner = rule()
                if winner:
                    return winner

            pygame.display.flip()

    pygame.quit()
