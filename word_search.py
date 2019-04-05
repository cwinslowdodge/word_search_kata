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
