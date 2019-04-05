import unittest
import word_search

class TestWordSearch(unittest.TestCase):

    def test_populate_puzzle_lines_are_not_empty(self):
        file = word_search.BuildPuzzle().populate_puzzle_lines('puzzle0.txt')
        self.assertNotEqual(len(file), 0)


if __name__ == '__main__':
    unittest.main()
