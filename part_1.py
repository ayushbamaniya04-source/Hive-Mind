class Field:

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

print(len(field.cells))
crop = field.get_cell(2, 5)

print(crop.row)
print(crop.col)
print(crop.state)
field.update_cell(crop, "problem")

print(crop.state)
another_crop = field.get_cell(1, 3)

print(another_crop.state)