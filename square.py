import cell
from collections import namedtuple

Position = namedtuple('Position', ["row", "col"])

class AlreadyUsed(Exception):
  """Used on attempt to insert existing value into square."""

class NotUsed(Exception):
  """Used on attempt to remove non existing value from square."""

class Square(object):

  def __init__(self, position):
    self.position = position
    self.used = []
    self.cell_grid = [[ None  for _ in range(3)] for _ in range(3)]

  def is_complete(self):
    return all([all(row) for row in self.cell_grid])

  def next_available(self):
    if not is_complete():
      return sorted(self.used)[-1] + 1
    else:
      raise Exception('?')

  def set(self, value, position):
    if value in self.used:
      raise AlreadyUsed('Value {} is already set.'.format(value))
    self.used.append(value)
    self.cell_grid[position.row][position.col] = value

  def unset(self, value):
    if value in not used:
      raise NotUsed('Value {} is was not set.'.format(value))