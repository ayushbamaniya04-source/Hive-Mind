import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

uav_x = 20
uav_y = 44
uav_radius = 10
uav_speed = 2

direction = 1
current_row = 0
moving_down = False

ROWS = 10
COLS = 20
CELL_WIDTH = SCREEN_WIDTH//COLS
CELL_HEIGHT = SCREEN_HEIGHT//ROWS

class Cell:
    def __init__(self, row, col, x, y, width, height):
        self.row = row
        self.col = col

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.scanned = False
rows = []
y = 0
for i in range(9):
    if i % 2 == 0:
        rows.append({"y": y, "height": 88, "type": "crop"})
        y += 88
    else:
        rows.append({"y": y, "height": 40, "type": "pathways"})
        y += 40
        

grid = []

crop_row = 0

for row in rows:
    if row["type"] == "crop":

        cell_row = []

        for col in range(COLS):

            x = col * CELL_WIDTH
            y = row["y"]

            cell_row.append(
                Cell(
                    crop_row,
                    col,
                    x,
                    y,
                    CELL_WIDTH,
                    row["height"]
                )
            )

        grid.append(cell_row)
        crop_row += 1
        


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
    global uav_x, uav_y, direction, current_row, moving_down
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("HIVE_MIND")
    clock = pygame.time.Clock()

    running = True 
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if moving_down:

         uav_y += uav_speed

         if uav_y >= rows[current_row + 2]["y"] + rows[current_row + 2]["height"] // 2:
          current_row += 2
          moving_down = False
          direction *= -1

        else:
          uav_x += direction * uav_speed
          if direction == 1 and uav_x >= SCREEN_WIDTH - uav_radius:
           if current_row + 2 < len(rows):
            moving_down = True

          elif direction == -1 and uav_x <= uav_radius:
           if current_row + 2 < len(rows):
               moving_down = True
        screen.fill((0,0,0))
        draw_grid(screen,rows)
        pygame.draw.circle(screen, (0, 0, 0), (uav_x, uav_y), uav_radius)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
