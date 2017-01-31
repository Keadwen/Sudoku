from collections import namedtuple

Position = namedtuple('Position', ["row", "col"])

class AlreadyUsed(Exception):
  """Used on attempt to overwrite cell."""

class NotUsed(Exception):
  """Used on attempt to remove non existing cell."""

class Sudoku(object):
  def __init__(self):
    self.grid = [[None for _ in range(9)] for _ in range(9)]

  def set(self, cell, position):
    if self.grid[position.row][position.col]:
      raise AlreadyUsed('Position row:{} col:{} is already set'.format(position))

    self.grid[position.row][position.col] = cell

  def unset(self, position):
    if not self.grid[position.row][position.col]:
      raise AlreadyUsed('Position row:{} col:{} is already empty'.format(position))

    self.grid[position.row][position.col] = None

  def get_square(self, position):
    def _low_index(num):
      """Returns a starting index for a grid range.

      Args:
        num: An integer, represents an index value.
      """
      if num/3 == 0: return 0
      if num/3 == 1: return 3
      return 6

    lc = _low_index(position.col)
    lr = _low_index(position.row)
    return [self.grid[r][lc:lc+3] for r in range(lr, lr+3)]

  def get_row(self, position):
    return self.grid[position.row]

  def get_column(self, position):
    return [self.grid[position.row][col] for col in range(0, 9)]

  def _valid_squares(self):
    squares = [self.get_square(Position(r, c)) for r in [0, 3, 6] for c in [0, 3, 6]]
    print(len(squares))
    for s in squares:
      print(s)
      print(set(s))
      if len(set(s)) != len(s):
        return False
    return True

  def _valid_columns(self):
    for col in range(9):
      uniques = set()
      for row in range(9):
        if self.grid[row][col] in uniques:
          return False
        uniques.add(self.grid[row][col])
    return True

  def _valid_rows(self):
    for row in range(9):
      uniques = set()
      for col in range(9):
        if self.grid[row][col] in uniques:
          return False
        uniques.add(self.grid[row][col])
    return True

  def is_valid(self):
    return (self._valid_rows() and self._valid_columns())
      # and
      #       self._valid_squares())
