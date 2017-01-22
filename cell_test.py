import unittest
import cell

class TestCell(unittest.TestCase):

  def testNotValidCellRaiseException(self):
    with self.assertRaises(cell.NotValidCell):
      for illegal_char in [10, 'A', ',', -123, 'A1']:
        c = cell.Cell(illegal_char)

  def testCellCanBeUnset(self):
    c = cell.Cell(2)
    c.unset()
    self.assertTrue(c.value == None)

  def testImplicitSetIsValidated(self):
    c = cell.Cell(1)
    c.unset()
    with self.assertRaises(cell.NotValidCell):
        c.set('A')

if __name__ == '__main__':
  unittest.main()
