import pygame
from PIL import Image
from conway import update_board

image_path = "cnw3.png"

if image_path is None:
    WIDTH, HEIGHT = 50, 50
else:
    im = Image.open(image_path)
    WIDTH, HEIGHT = im.width, im.height

CELL_SIZE = 7
PADDING = 1

FRAMERATE = 0

BG_COLOR = (100, 100, 100)

board = [[False for _ in range(HEIGHT)] for _ in range(WIDTH)]

if image_path is not None:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if im.getpixel((x, y))[0:3] != (255, 255, 255):
                board[x][y] = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode(
    ((WIDTH * (CELL_SIZE + PADDING)) + PADDING,
     (HEIGHT * (CELL_SIZE + PADDING)) + PADDING)
)

screen.fill(BG_COLOR)

new_board = board
first_run = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for x, column in enumerate(new_board):
        for y, cell in enumerate(column):
            if cell == board[x][y] and not first_run:
                continue

            if cell:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color,
                             (((x * (CELL_SIZE + PADDING)) + PADDING),
                              ((y * (CELL_SIZE + PADDING)) + PADDING),
                              CELL_SIZE,
                              CELL_SIZE))
    board = new_board

    pygame.display.flip()

    new_board = update_board(board)

    clock.tick(FRAMERATE)
    first_run = False
