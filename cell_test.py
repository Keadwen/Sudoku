import unittest
import cell

class TestCell(unittest.TestCase):

  def test_not_valid_cell_raise_exception(self):
    with self.assertRaises(cell.NotValidCell):
      for illegal_char in [10, 'A', ',', -123, 'A1']:
        c = cell.Cell(illegal_char)

  def test_fail_set(self):
    test_cases = (
      # (Cell value, Cell permanent, Cell new value, Cell expected value, Expects to pass).
      # (1, True, cell.NotValidCell),
      (1, True, 2, 1, cell.PermanentCell),
      # (None, True, cell.NotValidCell),
    )

    for cv, cp, got, want, err in test_cases:
      c = cell.Cell(cv, cp)
      with self.assertRaises(err):
        c.set(got)

if __name__ == '__main__':
  unittest.main()
