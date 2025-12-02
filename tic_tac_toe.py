import pygame


WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
CELL_W = WIDTH // COLS
CELL_H = HEIGHT // ROWS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_grid(screen):
    for x in range(1, COLS):
        pygame.draw.line(screen, BLACK, (x * CELL_W, 0), (x * CELL_W, HEIGHT), 5)
    for y in range(1, ROWS):
        pygame.draw.line(screen, BLACK, (0, y * CELL_H), (WIDTH, y * CELL_H), 5)


def draw_marks(screen, board, font):
    for r in range(ROWS):
        for c in range(COLS):
            mark = board[r][c]
            if mark:
                text = font.render(mark, True, BLACK)
                text_rect = text.get_rect(center=(c * CELL_W + CELL_W // 2, r * CELL_H + CELL_H // 2))
                screen.blit(text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, CELL_H // 2)

    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    player = "X"
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                row = my // CELL_H
                col = mx // CELL_W
                if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == "":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"

        screen.fill(WHITE)
        draw_grid(screen)
        draw_marks(screen, board, font)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
