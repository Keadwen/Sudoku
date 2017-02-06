"""BruteForceStrategy module represents a strategy to solve Sudoku puzzles."""
import sudoku


# TODO(jakubm): Check how custom made exceptions are implemented in Py3.
class NoSolutionException(Exception):
  """Raises when Sudoku has no valid solution."""


class InvalidSudokuException(Exception):
  """Raises when Sudoku is not a valid sudoku.Sudoku object."""


class NotImplemented(Exception):
  """Raises when a functionality is not yet implemented."""


class BruteForceStrategy(object):
  """Represents a BruteForceStrategy module solving Sudoku grid."""

  def __init__(self, s):
    self._sudoku = None
    # TODO(jakubm): Strategies accept only sudoku.Sudoku objects.
    # if isinstance(s, sudoku.Sudoku).
    self._sudoku = s
    # else:
    #   raise InvalidSudokuException(
    #       'Provided sudoku grid is not sudoku.Sudoku object.')

  def solve(self):
    """Applies bruteforce algorithm to solve Sudoku."""
    raise NotImplemented('solve method is not yet implemented.')
