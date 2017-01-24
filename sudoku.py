from collections import namedtuple

Position = namedtuple('Position', ["row", "col"])

class AlreadyUsed(Exception):
  """Used on attempt to overwrite cell."""

class NotUsed(Exception):
  """Used on attempt to remove non existing cell."""

class Sudoku(object):
  def __init__(self):
    self.grid = [[ None  for _ in range(9)] for _ in range(9)]

  def set(self, cell, position):
    if self.grid[position.row][position.col]:
      raise AlreadyUsed('Position row:{} col:{} is already set'.format(position))

    self.grid[position.row][position.col] = cell

  def unset(self, position):
    if not self.grid[position.row][position.col]:
      raise AlreadyUsed('Position row:{} col:{} is already empty'.format(position))

    self.grid[position.row][position.col] = None