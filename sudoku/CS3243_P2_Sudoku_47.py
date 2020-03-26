import sys
import copy
import time
import random

# Running script: given code can be run with the command:
# python file.py, ./path/to/init_state.txt ./output/output.txt

class Sudoku(object):
    def __init__(self, puzzle):
        # you may add more attributes if you need
        self.puzzle = puzzle # self.puzzle is a list of lists
        self.ans = copy.deepcopy(puzzle) # self.ans is a list of lists


    # you may add more classes/functions if you think is useful
    # However, ensure all the classes/functions are in this file ONLY
    # Note that our evaluation scripts only call the solve method.
    # Any other methods that you write should be used within the solve() method.

    def solve(self):
        # Call the the Sudoku solver method
        start = time.time()
        # self.csp_1()
        self.csp_2()
        end = time.time()

        print("Time taken to finish: " + str(end - start))
        # Return the final result of the Sudoku board
        return self.ans


    def csp_1(self):
        # Initialise the constraints on the initial given Sudoku board
        self.constraints = self.get_constraints();
        # Call the helper function to solve Sudoku by performing backtracking on the constraints
        self.csp1_helper()
        

    def csp1_helper(self):
        """
        Perform backtracking to fill each empty cell with value that satisfies the 
        constraints of Sudoku.
        """
        for x in range(len(self.ans)):
            for y in range(len(self.ans[0])):
                # When we find an empty cell
                if (self.ans[x][y] == 0):
                    # Use the coordinates of the current empty cell to form the key
                    # The key is used to get the corresponding list of candidate values
                    location = (x, y)
                    # Get a list of valid candidate values for the current empty cell
                    candidates = self.constraints.get(location)

                    for c in candidates:
                        # Among all valid candidates for the current empty cell, try the value c
                        self.ans[x][y] = c

                        self.print_table()
                        # Keep a copy of the old constraints
                        old_constraints = copy.deepcopy(self.constraints)
                        # Update the constraints with newly assigned value c
                        self.constraints = self.get_constraints()

                        # Proceed to the next empty cell by filling the current empty cell with value c
                        if (self.csp1_helper()):
                            return True;

                        # The value c is not a valid trial, backtrack by resetting this cell to empty again
                        # in order to try other values
                        self.ans[x][y] = 0
                        # Revert back to the old constraint
                        self.constraints = old_constraints

                    # We have exhausted the candidates for this cell
                    # There is no way to solve the puzzle with the current setting
                    # We need to go back to the previous step
                    return False;
        
        # We have solved the puzzle with every cell filled with valid value
        return True;


    def csp_2(self):
        # Initialise the constraints on the initial given Sudoku board
        self.constraints = self.get_constraints();
        # Call the helper function to solve Sudoku by performing backtracking on the constraints
        self.csp2_helper()
        

    def csp2_helper(self):
        """
        Perform backtracking to fill each empty cell with value that satisfies the 
        constraints of Sudoku.
        """
        for x in range(len(self.ans)):
            for y in range(len(self.ans[0])):
                # When we find an empty cell
                if (self.ans[x][y] == 0):
                    # Use the coordinates of the current empty cell to form the key
                    # The key is used to get the corresponding list of candidate values
                    location = (x, y)
                    # Get a list of valid candidate values for the current empty cell
                    candidates = self.constraints.get(location)
                    # Try out the candidate in random order
                    random.shuffle(candidates)

                    for c in candidates:
                        # Among all valid candidates for the current empty cell, try the value c
                        self.ans[x][y] = c

                        self.print_table()
                        # Keep a copy of the old constraints
                        old_constraints = copy.deepcopy(self.constraints)
                        # Update the constraints with newly assigned value c
                        self.constraints = self.get_constraints()

                        # Proceed to the next empty cell by filling the current empty cell with value c
                        if (self.csp1_helper()):
                            return True;

                        # The value c is not a valid trial, backtrack by resetting this cell to empty again
                        # in order to try other values
                        self.ans[x][y] = 0
                        # Revert back to the old constraint
                        self.constraints = old_constraints

                    # We have exhausted the candidates for this cell
                    # There is no way to solve the puzzle with the current setting
                    # We need to go back to the previous step
                    return False;
        
        # We have solved the puzzle with every cell filled with valid value
        return True;


    def identify_candidates(self, i, j):
        """
        Input: coordinates of the empty cell in check
        Output: list of valid values that can be assigned to the given empty cell

        This function returns a list of valid values based on the row, column
        and 3*3 square unique number constraints.
        """

        candidate_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # check the column
        for x in range(len(self.ans)):
            curr = self.ans[x][j]
            if (curr in candidate_list):
                candidate_list.remove(curr)

        # check the row
        for y in range(len(self.ans[0])):
            curr = self.ans[i][y]
            if (curr in candidate_list):
                candidate_list.remove(curr)

        # check the 3*3 square
        row = (i // 3) * 3;
        col = (j // 3) * 3;
        for x in range(row, row + 3):
            for y in range(col, col + 3):
                curr = self.ans[x][y]
                if (curr in candidate_list):
                    candidate_list.remove(curr)


        return candidate_list


    def get_constraints(self):
        """
        Input: the current Sudoku table (self.ans)
        Output: the dictionary with key as the coordinates of all empty cells on the table
            and value is the list of valid numbers that can be assigned to this cell

        This function finds the valid numbers for each empty cell on the current Sudoku board setting.
        """
        constraints = {}

        for i in range(len(self.ans)):
            for j in range(len(self.ans[0])):
                if (self.ans[i][j] == 0):
                    location = (i, j)
                    constraint_list = self.identify_candidates(i, j);
                    constraints[location] = constraint_list

        return constraints


    def print_table(self):
        # Utility function to print the current Sudoku table
        print("----------------------")
        for row in self.ans:
            for j in row:
                print("{:4}".format(str(j)), end='')
            print()
        print("----------------------")


if __name__ == "__main__":
    # STRICTLY do NOT modify the code in the main function here
    if len(sys.argv) != 3:
        print ("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
        raise ValueError("Wrong number of arguments!")

    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print ("\nUsage: python CS3243_P2_Sudoku_XX.py input.txt output.txt\n")
        raise IOError("Input file not found!")

    puzzle = [[0 for i in range(9)] for j in range(9)]
    lines = f.readlines()

    i, j = 0, 0
    for line in lines:
        for number in line:
            if '0' <= number <= '9':
                puzzle[i][j] = int(number)
                j += 1
                if j == 9:
                    i += 1
                    j = 0

    sudoku = Sudoku(puzzle)
    ans = sudoku.solve()

    with open(sys.argv[2], 'a') as f:
        for i in range(9):
            for j in range(9):
                f.write(str(ans[i][j]) + " ")
            f.write("\n")
