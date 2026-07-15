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
        
field = Field()

field.create()

field.generate_problems(5)

for row in field.cells:

    for cell in row:

        if cell.state == "problem":

            print(
                "Problem at:",
                cell.row,
                cell.col
            )

