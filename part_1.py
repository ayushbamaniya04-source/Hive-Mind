import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

ROWS = 10
COLS = 20
CELL_WIDTH = SCREEN_WIDTH//COLS
CELL_HEIGHT = SCREEN_HEIGHT//ROWS

grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]

def draw_grid(screen,grid):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT
            color = (139, 90, 43)
            if row % 2 == 0:
                color = (34, 139, 34)
            pygame.draw.rect(screen , color , (x,y,CELL_WIDTH,CELL_HEIGHT))
            pygame.draw.rect(screen, (0,0,0),(x,y,CELL_WIDTH,CELL_HEIGHT),1)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("HIVE_MIND")
    clock = pygame.time.Clock()

    running = True 
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0,0,0))
        draw_grid(screen,grid)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
