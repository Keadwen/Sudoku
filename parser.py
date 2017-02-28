import sudoku

def from_string(sudoku_str):
  sudoku_str = ''.join(sudoku_str.split())
  s = sudoku.Sudoku()
  for idx, val in enumerate(sudoku_str):
    row_idx = idx // 9
    col_idx = idx % 9
    s.set(cell.Cell(val), sudoku.Position(row_idx, col_idx))

  return s