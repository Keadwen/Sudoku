import cell
import sudoku

valid_sudoku = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]]

s = sudoku.Sudoku()

for row_idx, row in enumerate(valid_sudoku):
    for col_idx, col in enumerate(row):
        s.set(cell.Cell(valid_sudoku[row_idx][col_idx]), sudoku.Position(row_idx, col_idx))

print("Sudoku is valid: {}".format(s.is_valid()))

# Parse to sudoku and validate.

