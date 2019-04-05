import unittest
import word_search

class TestWordSearch(unittest.TestCase):

    def test_populate_puzzle_lines_are_not_empty(self):
        file = word_search.BuildPuzzle().populate_puzzle_lines('puzzle0.txt')
        self.assertNotEqual(len(file), 0)
        file = word_search.BuildPuzzle().populate_puzzle_lines('puzzle1.txt')
        self.assertNotEqual(len(file), 0)

    def test_word_list_has_correct_number_of_words(self):
        file = word_search.BuildPuzzle().create_words_list('puzzle0.txt')
        self.assertEqual(len(file), 7)
        file = word_search.BuildPuzzle().create_words_list('puzzle1.txt')
        self.assertEqual(len(file), 10)

    def test_first_and_last_words_in_word_list(self):
        file = word_search.BuildPuzzle().create_words_list('puzzle0.txt')
        self.assertEqual(file[0], 'BONES')
        self.assertEqual(file[len(file)-1], 'UHURA')
        file = word_search.BuildPuzzle().create_words_list('puzzle1.txt')
        self.assertEqual(file[0], 'AWESOME')
        self.assertEqual(file[len(file) - 1], 'TEST')

    def test_puzzle_board_is_square(self):
        file = word_search.BuildPuzzle().create_puzzle_board_matrix('puzzle0.txt')
        self.assertEqual(len(file), len(file[0]))
        file = word_search.BuildPuzzle().create_puzzle_board_matrix('puzzle1.txt')
        self.assertEqual(len(file), len(file[0]))



if __name__ == '__main__':
    unittest.main()
