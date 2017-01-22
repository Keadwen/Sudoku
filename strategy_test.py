import unittest
import strategy


class TestStrategy(unittest.TestCase):

    def testSolve(self):
        s = strategy.Strategy()
        with self.assertRaises(strategy.NotImplementedException):
            s.solve(None)


if __name__ == '__main__':
    unittest.main()
