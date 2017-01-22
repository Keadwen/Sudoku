"""Module Strategy contains a parents class for Sudoku solving strategies."""

class NotImplementedException(Exception):
    """Used in methods which are not implemented."""

class Strategy(object):
    """Top level class for all Sudoku solving method strategies."""
    def __init__(self):
        pass

    def solve(self, sudoku_grid):
        """Applies solving algorithm to find a solution in a given grid.

        Args:
          sudoku_grid: A sudoku.Sudoku object, represents a valid Sudoku grid.

        Returns:
          A sudoku.Sudoku object. If the solution for a given grid exists, 
          returned Sudoku grid is full, otherwise the same uncompleted object
          is returned.
        """ 
        raise NotImplementedException('Upsss. Seems like solve() is not yet'
                                      'implemented')
