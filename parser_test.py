import unittest
import parser
import sudoku

class TestParser(unittest.TestCase):

    def test_string_input(self):
      s_str = "000 000 000 000 000 000 000 000 000 \
               000 000 000 000 000 000 000 000 000 \
               000 000 000 000 000 000 000 000 000 "
      self.assertIsInstance(parser.from_string(s_str), sudoku.Sudoku)

if __name__ == '__main__':
  unittest.main()