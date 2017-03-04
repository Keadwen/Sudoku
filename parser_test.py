import unittest
import parser
import sudoku

class TestParser(unittest.TestCase):

    def test_string_input_yields_sudoku(self):
      s_str = "000 000 000 000 000 000 000 000 000 \
               000 000 000 000 000 000 000 000 000 \
               000 000 000 000 000 000 000 000 000 "
      self.assertIsInstance(parser.from_string(s_str), sudoku.Sudoku)

    def test_wrong_size_sudoku_raises_exception(self):
      too_short = "0"
      with self.assertRaises(parser.IncorrectLengthException):
        parser.from_string(too_short)

      too_long = "0" * 82
      with self.assertRaises(parser.IncorrectLengthException):
        parser.from_string(too_long)

if __name__ == '__main__':
  unittest.main()