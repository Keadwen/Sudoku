"""Sudoku module represets an interface to create Sudoku grid."""

class InvalidSudokuException(Exception):
  """Raises when invalid Sudoku tries to be inserted."""


class Sudoku(object):
  """Represents a Sudoku grid containing 9x9 matrix of cells."""

  # TODO(jakubm): Check if this is a correct way to init const in class.
  _SUDOKU_SIZE = 9

  def __init__(self):
    self._sudoku = [[] for _ in range(9)]  # 9x9 matrix of cells.

  class _Cell(object):
    """Represents Sudoku cell containing a single integer.

    Attributes:
      value: An integer, represents a value in a range <1,9>.
      mutable: A boolean, if true then a value can be changed.
    """
    _LOWER_BOUND = 1
    _UPPER_BOUND = 9

    def __init__(self, value=None, mutable=True):
      self._value = value
      self._mutable = mutable

    def set(self, value):
      """Sets a value to a cell, if the cell is mutable and in valid range."""
      if self._mutable and value >= _LOWER_BOUND and value <=_UPPER_BOUND:
        self._value = value

    def get(self, value):
      """Returns a current value of a cell."""
      return self._value

    def __repr__(self):
      return '{}'.format(self._value)


  def insert(self, grid):
    """Insert takes 9x9 integer grid and converts to internal structure.

    Args:
      grid: A two-dimensional list of integers, represents a Sudoku grid.
    
    Raises:
      sudoku.InvalidSudoku error, if incorrect grid has been provided.
    """

    # Validates if grid contains correct amount of rows.
    if len(grid) != self._SUDOKU_SIZE:
      raise InvalidSudokuException(
          'invalid length ({}), expected ({}).'.format(len(grid), _GRID_SIZE))
    
    for ri, row in enumerate(grid):
      # Validates if grid contains correct amount of columns.
      if len(row) != self._SUDOKU_SIZE:
        raise InvalidSudokuException(
            'invalid length ({}), expected ({}).'.format(len(row), _GRID_SIZE))

      for ci, col in enumerate(row):
        # For non-zero values, set a Cell as inmutable.
        if grid[ri][ci]:
          self._sudoku[ri].append(self._Cell(grid[ri][ci], False))

  def is_valid(self):
    # Three rules of valid Sudoku:
    # 1. No row should have duplicated values.
    # 2. No column should have duplicated values.
    # 3. No 3x3 grid should have dupliacted values.

    # Validate the requirement no. 1.
    for r in self._sudoku:
      if len(set(r)) != len(r):
        return False

    # Validate the requirement no. 2.
    for ri in range(_SUDOKU_SIZE):
      # Obtain and add values from each row.
      c_list = []
      c_set = set()
      for ci in range(_SUDOKU_SIZE):
        c_list.append(self._sudoku[ri][ci])
        c_set.add(self._sudoku[ri][ci])

      if len(set(c_set)) != len(c_list):
        return False

    # Validate the requirement no. 3.
    # TODO(jakubm): Workout the mapping for squares.
