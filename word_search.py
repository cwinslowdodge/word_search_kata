import sys

class BuildPuzzle:
    '''
    Class that creates word list and puzzle matrix
    '''

    def populate_puzzle_lines(self, filename):
        '''
        Reads text file and strips unnecessary characters
        :param filename: String .txt filename
        :return: list list_of_lines
        '''

        lines_of_puzzle = []
        list_of_lines = []
        puzzle_file = open(filename, 'r')

        for line in puzzle_file:
            lines_of_puzzle.append(line.strip('\n'))

        for line in lines_of_puzzle:
            list_of_lines.append(line.split(','))

        return list_of_lines

    def create_words_list(self, filename):
        '''
        Creates list of words to find in puzzle matrix
        :param filename: String .txt filename
        :return: list word_list
        '''

        word_list = []
        list_of_lines = BuildPuzzle().populate_puzzle_lines(filename)

        for word in list_of_lines[0]:
            word_list.append(word)

        return word_list

    def create_puzzle_board_matrix(self, filename):
        '''
        Creates puzzle matrix to be searched
        :param filename: String .txt filename
        :return: list puzzle_board
        '''

        puzzle_board = []
        list_of_lines = BuildPuzzle().populate_puzzle_lines(filename)

        for line in list_of_lines:
            puzzle_board.append(line)

        puzzle_board.pop(0)

        return puzzle_board

#Represents a word finder class
class WordFinder:
    '''
    Class that searches for words on puzzle matrix
    '''

    def search_for_words_by_first_letter_index(self, filename):
        '''
        Searches puzzle matrix by first letter in word
        for matches along each axis
        :param filename: String .txt filename
        :return: list word_coordinates
        '''

        words = BuildPuzzle().create_words_list(filename)
        puzzle = BuildPuzzle().create_puzzle_board_matrix(filename)
        index = []
        word_coordinates = {}

        for word in words:
            for line in puzzle:
                y_index = 0
                for letter in line:

                    if letter == word[0]:

                        index.append(y_index)
                        index.append(puzzle.index(line))

                        if WordFinder().search_for_word_descending_vertically(index, word, puzzle) is not None:
                            found_vert_des = WordFinder().search_for_word_descending_vertically(index, word, puzzle)
                            word_coordinates[word] = found_vert_des
                            pass

                        if WordFinder().search_for_word_ascending_vertically(index, word, puzzle) is not None:
                            found_vert_asc = WordFinder().search_for_word_ascending_vertically(index, word, puzzle)
                            word_coordinates[word] = found_vert_asc
                            pass

                        if WordFinder().search_for_word_ascending_horizontally(index, word, puzzle) is not None:
                            found_hrz_asc = WordFinder().search_for_word_ascending_horizontally(index, word, puzzle)
                            word_coordinates[word] = found_hrz_asc
                            pass

                        if WordFinder().search_for_word_descending_horizontally(index, word, puzzle) is not None:
                            found_hrz_des = WordFinder().search_for_word_descending_horizontally(index, word, puzzle)
                            word_coordinates[word] = found_hrz_des
                            pass

                        if WordFinder().search_for_word_ascending_diagonally_down(index, word, puzzle) is not None:
                            found_diag_asc_down = WordFinder().search_for_word_ascending_diagonally_down(index, word, puzzle)
                            word_coordinates[word] = found_diag_asc_down
                            pass

                        if WordFinder().search_for_word_descending_diagonally_up(index, word, puzzle) is not None:
                            found_diag_dsc_up = WordFinder().search_for_word_descending_diagonally_up(index, word, puzzle)
                            word_coordinates[word] = found_diag_dsc_up
                            pass

                        if WordFinder().search_for_word_descending_diagonally_down(index, word, puzzle) is not None:
                            found_diag_dsc_down = WordFinder().search_for_word_descending_diagonally_down(index, word, puzzle)
                            word_coordinates[word] = found_diag_dsc_down
                            pass

                        if WordFinder().search_for_word_ascending_diagonally_up(index, word, puzzle) is not None:
                            found_diag_asc_up = WordFinder().search_for_word_ascending_diagonally_up(index, word, puzzle)
                            word_coordinates[word] = found_diag_asc_up
                            pass

                        index = []

                    y_index = y_index + 1

        for key, value in sorted(word_coordinates.iteritems()):
            print key + ': ', value

        return word_coordinates

    def search_for_word_descending_vertically(self, index, word, puzzle):
        '''
        Searches for word vertically
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        y_index = index[1] + 1
        i = 1

        while i < len(word) and y_index < len(puzzle):

            if word[i] == puzzle[y_index][index[0]]:
                letter_coordinates.append(index[0])
                letter_coordinates.append(y_index)
                word_coordinates.append(letter_coordinates)
                y_index = y_index + 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_ascending_vertically(self, index, word, puzzle):
        '''
        Searches for word vertically backwards
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        y_index = index[1] - 1
        i = 1

        while i < len(word) and y_index >= 0:

            if word[i] == puzzle[y_index][index[0]]:
                letter_coordinates.append(index[0])
                letter_coordinates.append(y_index)
                word_coordinates.append(letter_coordinates)
                y_index = y_index - 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_ascending_horizontally(self, index, word, puzzle):
        '''
        Searches for word horizontally
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        x_index = index[0] + 1
        i = 1

        while i < len(word) and x_index < len(puzzle):

            if word[i] == puzzle[index[1]][x_index]:

                letter_coordinates.append(x_index)
                letter_coordinates.append(index[1])
                word_coordinates.append(letter_coordinates)
                x_index = x_index + 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_descending_horizontally(self, index, word, puzzle):
        '''
        Searches for word horizontally backwards
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        x_index = index[0] - 1
        i = 1

        while i < len(word) and x_index >= 0:

            if word[i] == puzzle[index[1]][x_index]:

                letter_coordinates.append(x_index)
                letter_coordinates.append(index[1])
                word_coordinates.append(letter_coordinates)
                x_index = x_index - 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_ascending_diagonally_down(self, index, word, puzzle):
        '''
        Searches for word diagonally down and to the right
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        index_x = index[0] + 1
        index_y = index[1] + 1
        i = 1

        while i < len(word) and index_x < len(puzzle) and index_y < len(puzzle):

            if word[i] == puzzle[index_y][index_x]:

                letter_coordinates.append(index_x)
                letter_coordinates.append(index_y)
                word_coordinates.append(letter_coordinates)
                index_x = index_x + 1
                index_y = index_y + 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_descending_diagonally_up(self, index, word, puzzle):
        '''
        Searches for word diagonally up and to the right
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        index_x = index[0] - 1
        index_y = index[1] - 1
        i = 1

        while i < len(word) and index_x >= 0 and index_y >= 0:

            if word[i] == puzzle[index_y][index_x]:

                letter_coordinates.append(index_x)
                letter_coordinates.append(index_y)
                word_coordinates.append(letter_coordinates)
                index_x = index_x - 1
                index_y = index_y - 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_descending_diagonally_down(self, index, word, puzzle):
        '''
        Searches for word diagonally down and to the left
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        index_x = index[0] - 1
        index_y = index[1] + 1
        i = 1

        while i < len(word) and index_x >= 0 and index_y < len(puzzle):

            if word[i] == puzzle[index_y][index_x]:

                letter_coordinates.append(index_x)
                letter_coordinates.append(index_y)
                word_coordinates.append(letter_coordinates)
                index_x = index_x - 1
                index_y = index_y + 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

    def search_for_word_ascending_diagonally_up(self, index, word, puzzle):
        '''
        Searches for word diagonally up and to the left
        :param index: starting coodinates to begin search
        :param word: current word that is being looked for
        :param puzzle: puzzle matrix to be searched
        :return: list of word_coordinates
        '''

        word_coordinates = [index]
        letter_coordinates = []
        index_x = index[0] + 1
        index_y = index[1] - 1
        i = 1

        while i < len(word) and index_x < len(puzzle) and index_y >= 0:

            if word[i] == puzzle[index_y][index_x]:

                letter_coordinates.append(index_x)
                letter_coordinates.append(index_y)
                word_coordinates.append(letter_coordinates)
                index_x = index_x + 1
                index_y = index_y - 1
                i = i + 1
                letter_coordinates = []

            else:
                break

        if len(word_coordinates) == len(word):
            return word_coordinates

try:
    WordFinder().search_for_words_by_first_letter_index(sys.argv[1])
except IndexError:
    WordFinder().search_for_words_by_first_letter_index('puzzle0.txt')



