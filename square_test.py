import unittest
import square
import cell

class TestSquare(unittest.TestCase):

  def testSquareCreation(self):
    s = square.Square(square.Position(row=0, col=1))
    s.cell_grid[0][0] = cell.Cell(value=2, permanent=True)
    s.cell_grid[0][1] = cell.Cell(value=8, permanent=True)
    s.cell_grid[0][2] = cell.Cell(value=9, permanent=True)
    s.cell_grid[1][0] = cell.Cell(value=9, permanent=True)
    s.cell_grid[1][1] = cell.Cell(value=9, permanent=True)
    s.cell_grid[1][2] = cell.Cell(value=9, permanent=True)
    s.cell_grid[2][0] = cell.Cell(value=9, permanent=True)
    s.cell_grid[2][1] = cell.Cell(value=9, permanent=True)
    s.cell_grid[2][2] = cell.Cell(value=9, permanent=True)
    print(s.cell_grid)
    print(s.is_complete())

if __name__ == '__main__':
  unittest.main()