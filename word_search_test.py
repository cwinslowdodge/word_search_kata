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

    def test_puzzle_board_is_correct_length(self):
        file = word_search.BuildPuzzle().create_puzzle_board_matrix('puzzle0.txt')
        self.assertEqual(len(file[0]), 15)

    def test_find_index_of_first_letter_of_first_word_on_puzzle_board(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['BONES'][0], [0,6])

    def test_word_coordinates_found_descending_vertically(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['BONES'], [[0,6], [0,7], [0,8], [0,9], [0,10]])

    def test_word_coordinates_found_ascending_vertically(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['KHAN'], [[5,9], [5,8], [5,7], [5,6]])

    def test_word_coordinates_found_ascending_horizontally(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['SCOTTY'], [[0,5], [1,5], [2,5], [3,5], [4,5], [5,5]])

    def test_word_coordinates_found_descending_horizontally(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['KIRK'], [[4, 7],[3, 7],[2, 7],[1, 7]])

    def test_word_coordinates_found_ascending_diagonally_down(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['SPOCK'], [[2,1],[3,2],[4,3],[5,4],[6,5]])

    def test_word_coordinates_found_descending_diagonally_up(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['SULU'], [[3,3],[2,2],[1,1],[0,0]])

    def test_word_coordinates_found_descending_diagonally_down(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')
        self.assertEqual(file['UHURA'], [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]])

    def test_word_coordinates_found_ascending_diagonally_up(self):
        file = word_search.WordFinder().search_for_words_by_first_letter_index('puzzle1.txt')
        self.assertEqual(file['LEARNING'], [[4, 7], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1], [11, 0]])

if __name__ == '__main__':
    unittest.main()
