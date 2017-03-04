import sudoku

class IncorrectLengthException(Exception):
    """Used when from_string parser gets string  with wrong size"""

def from_string(sudoku_str):
  """Parses string into sudoku object.

  Args:
    sudoku_str: string representing consecutive values of sudoku

  Returns:
    A sudoku.Sudoku object

  Raises:
    IncorrectLengthException if string of wrong size was provided.
  """

  sudoku_str = ''.join(sudoku_str.split())
  if len(sudoku_str) != 81:
    raise IncorrectLengthException()

  grid =  [[None for i in range(9)] for j in range(9)]

  for idx, val in enumerate(sudoku_str):
    row_idx = idx // 9
    col_idx = idx % 9
    grid[row_idx][col_idx] = val

  s = sudoku.Sudoku()
  s.insert(grid)
  return s