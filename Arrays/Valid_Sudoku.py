"""
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # initiate a set that doesn't allow duplicates for row
        # this creates a list of 9 sets to hold for each row and column respectively
        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        # to handle 3 x 3, we need 3 sets of 3 (a list of lists)
        box_sets = [[set() for _ in range(3)] for _ in range(3)]


        # iterate across all rows in board (9)
        for row in range(9):
            # iterate across all columns in rows
            for column in range(9):
                # extract each cell
                num = board[row][column]

                # edge case to handle empty cells
                if num == ".":
                    continue  

                # check validity of rows
                # accesses the list of row sets with [row]
                if num in row_sets[row]:
                    return False
                # otherwise, we add num to the set at that row in list
                row_sets[row].add(num)

                # check validity of columns
                if num in column_sets[column]:
                    return False
                column_sets[column].add(num)

                # check validity of boxes
                # need to check each sublist
                # can do this by diving each subset
                box_row, box_col = row // 3, column // 3
                if num in box_sets[box_row][box_col]:
                    return False
                box_sets[box_row][box_col].add(num)

        # return true if all cases met
        return True







