class Field:

    def __init__(self):
        self.cells = []
        self.rows = []
        
    def create(self):
            for row in range(5):
                for col in range(20):
                    cell = Cell(row, col)
                    self.cells.append(cell)
                    
    def draw(self):
        pass

    def get_cell(self, x, y):
        pass

    def update_cell(self, cell, state):
        pass

    def reset(self):
        pass
    
class Cell:
        
        
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = "healthy"
        
field = Field()

field.create()

print(len(field.cells))