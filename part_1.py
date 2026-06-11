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

rows = []
y = 0
for i in range(9):
    if i % 2 == 0:
        rows.append({"y": y, "height": 88, "type": "crop"})
        y += 88
    else:
        rows.append({"y": y, "height": 40, "type": "pathways"})
        y += 40
def draw_grid(screen,rows):
    for row in rows:
        y = row["y"]
        height = row["height"]
        if row["type"] == "crop":
            for col in range(COLS):
                x = col * CELL_WIDTH
                color = (34, 139, 34)
                pygame.draw.rect(screen , color , (x,y,CELL_WIDTH,height))
                pygame.draw.rect(screen, (0,0,0),(x,y,CELL_WIDTH,height),1)
        else:
                color = (139, 90, 43)
                pygame.draw.rect(screen , color , (0,y,SCREEN_WIDTH,height))
                pygame.draw.rect(screen, (0,0,0),(0,y,SCREEN_WIDTH,height),1)

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
        draw_grid(screen,rows)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
