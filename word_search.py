class BuildPuzzle:

    def populate_puzzle_lines(self, filename):

        lines_of_puzzle = []
        list_of_lines = []
        puzzle_file = open(filename, 'r')

        for line in puzzle_file:
            lines_of_puzzle.append(line.strip('\n'))

        for line in lines_of_puzzle:
            list_of_lines.append(line.split(','))

        return list_of_lines

    def create_words_list(self, filename):
        word_list = []
        list_of_lines = BuildPuzzle().populate_puzzle_lines(filename)

        for word in list_of_lines[0]:
            word_list.append(word)

        return word_list

    def create_puzzle_board_matrix(self, filename):
        puzzle_board = []
        list_of_lines = BuildPuzzle().populate_puzzle_lines(filename)

        for line in list_of_lines:
            puzzle_board.append(line)

        puzzle_board.pop(0)

        return puzzle_board

class WordFinder:



    def search_for_first_letter(self, filename):

        words = BuildPuzzle().create_words_list(filename)
        puzzle = BuildPuzzle().create_puzzle_board_matrix(filename)

        for word in words:
            for line in puzzle:
                for letter in line:
                    if letter == word[0]:
                        print puzzle.index(line)
                        print line.index(letter)

                        return word[0]











