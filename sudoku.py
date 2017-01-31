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
    return [grid[r][lc:lc+2] for r in range(lr, lr+2)]


  def get_row(self, position):
    return self.grid[position.row]

  def get_column(self, position):
    return [self.grid[position.row][col] for col in range(0,9)]