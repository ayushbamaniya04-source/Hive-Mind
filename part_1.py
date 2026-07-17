import random

class Field:
    
    def generate_problems(self, count):
        for _ in range(count):
            row = random.randint(0, 4)
            col = random.randint(0, 19)

            self.cells[row][col].state = "problem"

    def __init__(self):
        self.cells = []
        self.rows = []
        
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

    def scan(self, field, mission_control):
        cell = field.get_cell(self.row, self.col)
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

        self.battery = 100

        self.status = "idle"

        self.current_task = None

    def receive_task(self):
        pass

    def move(self):
        pass

    def spray(self, field):
        
        if self.current_task is not None:
            
            row, col = self.current_task
            
            cell = field.get_cell(row, col)
            
            cell.state = "healthy"
            
            print("Problem fixed at:", row, col)

    def return_home(self):
        pass
class MissionControl:

    def __init__(self):
        self.known_problems = []
    
    def receive_report(self, row, col):
        self.known_problems.append((row, col))
    
    def assign_task(self, ugv):

        if len(self.known_problems) > 0:

            ugv.current_task = self.known_problems[0]

            print("Task assigned:", ugv.current_task)



field = Field()
field.create()
field.generate_problems(5)

uav = UAV()
mission = MissionControl()

for row in field.cells:
    for cell in row:
        if cell.state == "problem":
            uav.row = cell.row
            uav.col = cell.col
            break

uav.scan(field, mission)

print(mission.known_problems)

ugv = UGV()

mission.assign_task(ugv)

ugv.spray(field)

print(ugv.current_task)

row, col = ugv.current_task

print(field.get_cell(row, col).state)

