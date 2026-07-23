import pygame
import random

class Field:
    
    def generate_problems(self, count):
        for _ in range(count):
            row = random.choice(self.crop_rows)
            col = random.randint(0, 19)

            self.cells[row][col].state = "problem"

    def __init__(self):
        self.cells = []
        self.rows = []
        self.crop_rows = [0, 2, 4]
        
    def create(self):
        for row in range(5):
            row_cells = []
            for col in range(20):
                cell = Cell(row, col)
                row_cells.append(cell)

            self.cells.append(row_cells)
           
    def draw(self):
        pass

    def get_cell(self, row, col):
        
        return self.cells[row][col]

    def update_cell(self, cell, state):
        cell.state = state
        

    def reset(self):
        pass
    
class Cell:
        
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = "healthy"
        
class UAV:

    def __init__(self):
        self.row = 0
        self.col = 0
        self.battery = 100
        self.status = "idle"

    def move(self):
        pass

    def scan_field(self, field, mission_control):
        for row in field.cells:
            for cell in row:
                if cell.state == "problem":
                    mission_control.receive_report(
                    cell.row,
                    cell.col
                )
        

    def report(self):
        pass

    def return_home(self):
        pass

class UGV:

    def __init__(self):

        self.row = 0
        self.col = 0
        self.home_row = 1
        self.home_col = 0

        self.battery = 100
        self.battery = 25

        self.status = "idle"

        self.current_task = None
        self.destination = None

    def receive_task(self):
        pass
    
    def battery_low(self):
        return self.battery <= 20

    def move(self):
        
        if self.current_task is None:
            return

        target_row, target_col = self.destination

        if self.row < target_row:
           self.row += 1
           self.battery -= 1

        elif self.row > target_row:
            self.row -= 1
            self.battery -= 1

        elif self.col < target_col:
            self.col += 1
            self.battery -= 1
        
        elif self.col > target_col:
            self.col -= 1
            self.battery -= 1

    def spray(self, field, mission_control):
        
        if self.current_task is not None:
            
            row, col = self.current_task
            
            cell = field.get_cell(row, col)
            
            cell.state = "healthy"
            
            print("Problem fixed at:", row, col)
            
            mission_control.complete_task(row, col)
            
        if self.current_task is not None:
            self.battery -= 2
            
    def get_spray_position(self, problem_row, problem_col):
        
        if problem_row == 0:
            return (1, problem_col)

        elif problem_row == 2:
            return (3, problem_col)
        
        elif problem_row == 4:
            return (3, problem_col)
    
    def charge(self):
        self.battery = 100

        print("Battery fully charged")
    
    def return_home(self):
        self.destination = (
            self.home_row,
            self.home_col
            )
class MissionControl:

    def __init__(self):
        self.known_problems = []
    
    def receive_report(self, row, col):
        self.known_problems.append((row, col))
    
    def assign_task(self, ugv):

        if len(self.known_problems) > 0:

            problem = self.known_problems[0]

            ugv.current_task = problem

            row, col = problem

            ugv.destination = ugv.get_spray_position(
                row,
                col
            )

            print("Task assigned:", ugv.current_task)

    def complete_task(self, row, col):
        if (row, col) in self.known_problems:
            self.known_problems.remove((row, col))

            print("Task completed:", (row, col))

field = Field()
field.create()
field.generate_problems(5)

pygame.init()

CELL_SIZE = 40

ROWS = 5
COLS = 20

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw(screen, field, ugv):

    screen.fill((30, 30, 30))

    for row in field.cells:
        for cell in row:

            x = cell.col * CELL_SIZE
            y = cell.row * CELL_SIZE

            if cell.row in [0, 2, 4]:

                color = (0, 180, 0)

                if cell.state == "problem":
                    color = (220, 0, 0)

            else:
                color = (150, 120, 80)

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )

    pygame.draw.rect(
        screen,
        (255, 255, 0),
        (
            ugv.home_col * CELL_SIZE,
            ugv.home_row * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
    )

    pygame.draw.rect(
        screen,
        (0, 0, 255),
        (
            ugv.col * CELL_SIZE + 5,
            ugv.row * CELL_SIZE + 5,
            CELL_SIZE - 10,
            CELL_SIZE - 10
        )
    )

    pygame.display.flip()

uav = UAV()
mission = MissionControl()

for row in field.cells:
    for cell in row:
        if cell.state == "problem":
            uav.row = cell.row
            uav.col = cell.col
            
            break

uav.scan_field(field, mission)

print(mission.known_problems)

ugv = UGV()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if ugv.current_task is None and len(mission.known_problems) > 0:
        mission.assign_task(ugv)

    if ugv.current_task is not None:
        if (ugv.row, ugv.col) != ugv.destination:
            ugv.move()

        else:
            ugv.spray(field, mission)
            ugv.current_task = None
        
    draw(
        screen,
        field,
        ugv
    )

    clock.tick(2)

pygame.quit()