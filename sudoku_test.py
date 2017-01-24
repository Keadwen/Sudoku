import unittest
import sudoku
import cell

class TestSudoku(unittest.TestCase):

  def testSudokuCreation(self):
    s = sudoku.Sudoku()
    my_cell = cell.Cell(3)
    s.set(my_cell, sudoku.Position(row=0,col=0))
    self.assertEqual(s.grid[0][0], my_cell)

if __name__ == '__main__':
  unittest.main()
